<?php
/* TODO:
    - google map geocoder
    - no reload, just 1 long call
*/

include('config.inc.php');
include('functions.inc.php');

if (!$db = connectDB($config['host'], $config['dbname'], $config['user'], $config['pass'])) {
    die('Database connection error.');
}

// get page offset number
$page = isset($_GET['page']) ? $_GET['page'] : 0;

if (!is_numeric($page)) {
    $page = 0;
}

$userAgent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36';
$referer = 'https://a816-healthpsi.nyc.gov/ChildCare/SearchAction2.do';
$postString = 'linkPK=0&getNewResult=true&facilityName=&permitNo=&borough=&zipCode=&neighborhood=';
$url = 'https://a816-healthpsi.nyc.gov/ChildCare/SearchAction2.do?pager.offset='.$page;

$gresult = getData($url, $postString, $userAgent, $referer);

// regular expression to get the daycare table rows of the current page
if ($gresult) {
    if (preg_match_all('/<BR \/>\s*No match is found/', $gresult, $matches)) {
        // no results found on https://a816-healthpsi.nyc.gov
        $found = false;
    } else {

        if (preg_match_all('/<BR \/>\s*(\d+) child care services match your search criteria/', $gresult, $matches)) {
            $numberOfCenters = $matches[1][0];
        }
        
        if (preg_match_all('/<TR>\s*<TD CLASS="cell_leftborder" VALIGN="top"><A HREF=\'#\' onclick=\'redirectHistory\("(.*)"\); return false;\' rel="external">(.*)&nbsp;<\/a><\/TD>\s*<TD CLASS="cell_border" VALIGN="top">(.*)&nbsp;<\/TD>\s*<TD CLASS="cell_border" VALIGN="top">(\d+)&nbsp;<\/TD>\s*<TD CLASS="cell_border" VALIGN="top">(.*)&nbsp;<\/TD>\s*<TD CLASS="cell_border" VALIGN="top">(.*)&nbsp;<\/TD>\s*<TD CLASS="cell_border" VALIGN="top"><A HREF=\'#\' onclick=\'redirectHistory\(".*"\); return false;\' rel="external">More info<\/A><\/TD>\s*<\/TR>/', $gresult, $matches)) {
            $centerIdArray = $matches[1];
            $namesArray = $matches[2];
            $addressArray = $matches[3];
            $zipArray = $matches[4];
            $telArray = $matches[5];
            $statusArray = $matches[6];
            $found = true;
        }

    }
}

// if there are results, loop them
if (!empty($namesArray)) {
    $n = 0;
    foreach ($namesArray as $name) {
        // check if name + address combination already exists in DB
        $stmt = $db->prepare('SELECT id FROM centers WHERE name = :name AND address = :address');
        $stmt->execute(array(':name' => $name, ':address' => trim($addressArray[$n])));
        $row = $stmt->fetch(PDO::FETCH_ASSOC);
        if ($row) {
            // if name + address combination exists, do an update for only phone and status field
            $stmt = $db->prepare("UPDATE centers SET phone = :phone, status = :status WHERE id = :id");
            $stmt->execute( array(':phone' => trim($telArray[$n]),
                                ':status' => trim($statusArray[$n]),
                                ':id' => $row['id']
                                )
                            );
            echo 'Update: '.$name."<br>\n";
        } else {
            // check to see if geocoding is needed
            if ($config['geocode']) {
                $geoAddress = urlencode( trim($addressArray[$n]).', '.trim($zipArray[$n]).', New York' );
                $geoUrl = 'https://maps.googleapis.com/maps/api/geocode/json?address='.$geoAddress.'&sensor=false&key='.$config['googleKey'];
                $geoResult = getData($geoUrl, '', $userAgent, '');
                if ($geoResult != '') {
                    $geoResult = json_decode($geoResult);
                    if ($geoResult->status == 'OK') {
                        $latitude = $geoResult->results[0]->geometry->location->lat;
                        $longitude = $geoResult->results[0]->geometry->location->lng;
                    }
                }
            } else {
                $latitude = $longitude = '';
            }

            // get individual center data
            $postString = 'linkPK='.$centerIdArray[$n];
            $url = 'https://a816-healthpsi.nyc.gov/ChildCare/WDetail.do';

            $gresult = getData($url, $postString, $userAgent, $referer);
            $borough = $permitNo = '';
            if ($gresult) {
                if (preg_match_all('/<tr><td class="cell_border_leftbottom" valign="top">Borough<\/td>\s*<td class="cell_border" valign="top">(.*)&nbsp;<\/td>/', $gresult, $matches)) {
                    $borough = $matches[1][0];
                }
                if (preg_match_all('/<tr><td class="cell_border_leftbottom" valign="top">Permit Number<\/td>\s*<TD class="cell_border" valign="top">(\d+)&nbsp;<\/TD>/', $gresult, $matches)) {
                    $permitNo = $matches[1][0];
                }
            }

            // if name + address combination does not exist, insert data
            $stmt = $db->prepare("INSERT INTO centers (name, address, borough, zipcode, phone, status, latitude, longitude, permitno, lastupdate) VALUES (:name, :address, :borough, :zipcode, :phone, :status, :latitude, :longitude, :permitno, NOW())");
            $stmt->execute( array(':name' => trim($name),
                                ':address' => trim($addressArray[$n]),
                                ':borough' => trim($borough),
                                ':zipcode' => trim($zipArray[$n]),
                                ':phone' => trim($telArray[$n]),
                                ':status' => trim($statusArray[$n]),
                                ':latitude' => $latitude,
                                ':longitude' => $longitude,
                                ':permitno' => $permitNo
                                )
                            );
            // print_r($db->errorInfo());
            echo 'Insert: '.$name."<br>\n";
        }
        $n++;
    }
}

// if results are found, increase page offset
if ($found) {
    // a816-healthpsi.nyc.gov increases the page results by 10
    $page += 10;
    // calculate last page offset
    $lastOffset = floor($numberOfCenters / 10) * 10;
} else {
    // set high last page offset so the script keeps running
    $lastOffset = 99999;
    echo 'No results found. Trying again...';
}

// keep reloading until last page offset
if ($page < $lastOffset + 1) {
    // reload the script after 5 seconds with the next page offset
    ?>
    <META HTTP-EQUIV="refresh" content="<?php echo $config['delay']; ?>;url=daycare.php?page=<?php echo $page; ?>">
    <?php
} else {
    // done
    echo 'Finished';
    exit();
}
?>
