<?php

   if($_SERVER["HTTPS"] != "on")
   {
      header("Location: https://" . $_SERVER["HTTP_HOST"] . $_SERVER["REQUEST_URI"]);
      exit();
   }
   
// Use python script to send out an int value as signal
// to tell the sensor to toggle the arming state
// and switch on the motion stream

$action = $_POST['action'];

$filepath = "/home/pi/livestream.txt";

if ($action=="on") {
    file_put_contents($filepath, "1");   
    system('python /home/pi/sensor_client.py 2');
}
else {
    file_put_contents($filepath, "0");
    system('python /home/pi/sensor_client.py 3'); 
}

sleep(1.5); // to allow some time for the camera to go live

header('Location: livestream.php');
?>
