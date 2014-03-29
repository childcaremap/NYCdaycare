<?php
include('functions.inc.php');

// get page offset number
$page = isset($_GET['page']) ? $_GET['page'] : 0;

if (!is_numeric($page)) {
    $page = 0;
}

$userAgent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36';
$referer = 'https://a816-healthpsi.nyc.gov/ChildCare/SearchAction2.do';
$poststring = 'linkPK=0&getNewResult=true';
$url = 'https://a816-healthpsi.nyc.gov/ChildCare/SearchAction2.do?pager.offset='.$page;

$gresult = getData($url, $postString, $userAgent, $referer);

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
