<?php
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
        
        if (preg_match_all('/<TR>\s*<TD CLASS="cell_leftborder" VALIGN="top"><A HREF=\'#\' onclick=\'redirectHistory\(".*"\); return false;\' rel="external">(.*)&nbsp;<\/a><\/TD>\s*<TD CLASS="cell_border" VALIGN="top">(.*)&nbsp;<\/TD>\s*<TD CLASS="cell_border" VALIGN="top">(\d+)&nbsp;<\/TD>\s*<TD CLASS="cell_border" VALIGN="top">(.*)&nbsp;<\/TD>\s*<TD CLASS="cell_border" VALIGN="top">(.*)&nbsp;<\/TD>\s*<TD CLASS="cell_border" VALIGN="top"><A HREF=\'#\' onclick=\'redirectHistory\(".*"\); return false;\' rel="external">More info<\/A><\/TD>\s*<\/TR>/', $gresult, $matches)) {
            $namesArray = $matches[1];
            $addressArray = $matches[2];
            $zipArray = $matches[3];
            $telArray = $matches[4];
            $statusArray = $matches[5];
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
            $stmt = $db->prepare("UPDATE centers SET phone = :phone, status = :status");
            $stmt->execute( array(':phone' => trim($telArray[$n]),
                                ':status' => trim($statusArray[$n]))
                            );
            echo 'Update: '.$name."<br>\n";
        } else {
            // if name + address combination does not exist, insert data
            $stmt = $db->prepare("INSERT INTO centers (name, address, zipcode, phone, status, lastupdate) VALUES (:name, :address, :zipcode, :phone, :status, NOW())");
            $stmt->execute( array(':name' => trim($name),
                                ':address' => trim($addressArray[$n]),
                                ':zipcode' => trim($zipArray[$n]),
                                ':phone' => trim($telArray[$n]),
                                ':status' => trim($statusArray[$n]))
                            );
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
