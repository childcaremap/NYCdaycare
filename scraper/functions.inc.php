<?php
function connectDB($host, $dbname, $user, $pass)
{
	try {
	  return new PDO("mysql:host=$host;dbname=$dbname", $user, $pass);
	}
	catch(PDOException $e) {
	    return false; // $e->getMessage();
	}
}

function getData($url, $postString, $userAgent, $referer)
{
	$ch = curl_init();
	curl_setopt($ch, CURLOPT_COOKIEJAR, 'cookie.txt');
	curl_setopt($ch, CURLOPT_URL, $url);
	curl_setopt($ch, CURLOPT_USERAGENT, $userAgent);
	curl_setopt($ch, CURLOPT_HEADER, 0);
	curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);// allow redirects 
	curl_setopt($ch, CURLOPT_RETURNTRANSFER,1); // return into a variable
	curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
	curl_setopt($ch, CURLOPT_TIMEOUT, 15); // times out after 15s
	curl_setopt($ch, CURLOPT_REFERER, $referer);
	curl_setopt($ch, CURLOPT_COOKIEFILE, 'cookie.txt');
	if ($postString != '') {
		curl_setopt($ch, CURLOPT_POSTFIELDS, $postString);
	}

	$gresult = curl_exec ($ch); // execute the curl command

	#print_r(curl_getinfo($ch));
	#echo curl_errno($ch) . '-' .
	#        curl_error($ch);

	curl_close($ch);
	unset($ch);

	return $gresult;
}
?>