<?php
// get page offset number
$page = isset($_GET['page']) ? $_GET['page'] : 0;

if (!is_numeric($page)) {
    $page = 0;
}

// set vars to POST
$poststring = "linkPK=0&getNewResult=true";

// get page contents with cURL
$url = "https://a816-healthpsi.nyc.gov/ChildCare/SearchAction2.do?pager.offset=".$page;
$ch = curl_init();
curl_setopt($ch, CURLOPT_COOKIEJAR, "cookie.txt");
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_USERAGENT, "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36");
curl_setopt($ch, CURLOPT_HEADER, 0);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);// allow redirects 
curl_setopt($ch, CURLOPT_RETURNTRANSFER,1); // return into a variable
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
curl_setopt($ch, CURLOPT_TIMEOUT, 15); // times out after 15s
curl_setopt($ch, CURLOPT_REFERER, "https://a816-healthpsi.nyc.gov/ChildCare/SearchAction2.do");
curl_setopt($ch, CURLOPT_COOKIEFILE, "cookie.txt");
curl_setopt($ch, CURLOPT_POSTFIELDS, $poststring);

$gresult = curl_exec ($ch); // execute the curl command

#print_r(curl_getinfo($ch));
#echo curl_errno($ch) . '-' .
#        curl_error($ch);

curl_close($ch);
unset($ch);

// regular expression to get the daycare table rows of the current page
if ($gresult) {
    if (preg_match_all('/<TR>\s*<TD CLASS="cell_leftborder" VALIGN="top"><A HREF=\'#\' onclick=\'redirectHistory\(".*"\); return false;\' rel="external">(.*)&nbsp;<\/a><\/TD>\s*<TD CLASS="cell_border" VALIGN="top">(.*)&nbsp;<\/TD>\s*<TD CLASS="cell_border" VALIGN="top">(\d+)&nbsp;<\/TD>\s*<TD CLASS="cell_border" VALIGN="top">(.*)&nbsp;<\/TD>\s*<TD CLASS="cell_border" VALIGN="top">(.*)&nbsp;<\/TD>\s*<TD CLASS="cell_border" VALIGN="top"><A HREF=\'#\' onclick=\'redirectHistory\(".*"\); return false;\' rel="external">More info<\/A><\/TD>\s*<\/TR>/', $gresult, $matches)) {
        $namesArray = $matches[1];
        $addressArray = $matches[2];
        $zipArray = $matches[3];
        $telArray = $matches[4];
        $statusArray = $matches[5];
    }
}


// open file daycarenyc.csv to append(!) scraped data
if (!empty($namesArray)) {
    $fp = fopen('daycarenyc.csv', 'a') or die('cannot open file daycarenyc.csv');
    $n = 0;
    foreach ($namesArray as $name) {
        $fields = array();
        $fields = array( trim($name), trim($addressArray[$n]), trim($zipArray[$n]), trim($telArray[$n]), trim($statusArray[$n]) );
        fputcsv($fp, $fields);
        var_dump($fields); // output the array which will be written to the csv
        $n++;
    }
    fclose($fp);
}

// a816-healthpsi.nyc.gov increases the page results by 10
$page += 10;

// hardcoded when to stop. current last page offset is 2220
if ($page < 2221) {
    // reload the script after 5 seconds with the next page offset
    ?>
    <META HTTP-EQUIV="refresh" content="5;url=daycare.php?page=<?php echo $page; ?>">
    <?php
} else {
    // done
    echo 'ready';
    exit();
}
?>
