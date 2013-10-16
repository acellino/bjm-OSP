<?php

   if($_SERVER["HTTPS"] != "on")
   {
      header("Location: https://" . $_SERVER["HTTP_HOST"] . $_SERVER["REQUEST_URI"]);
      exit();
   }
   
// Use python script to send out an int value as signal
// to tell the sensor to toggle the arming state

system('python /home/pi/sensor_client.py 1');

header('Location: index.php');
?>
