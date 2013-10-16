<html>
<head>

<script type="text/javascript" src="jquery-1.4.3.js"></script>

<script>
  $(function() {
  	$("#left_pane").css("left","-220px");
  	$("#main_pane").css("left","0px");

  	$(".toggle_right_pane").toggle(function() {       
      	    $('#left_pane').animate({ left: '0' }, 500);
      	    $('#main_pane').animate({ left: '240' }, 500);
  	}, function() {       
      	    $('#left_pane').animate({ left: '-240' }, 500);
            $('#main_pane').animate({ left: '0' }, 500);
  	});
  });

</script>

<link rel="stylesheet" type="text/css" href="simple.css">

</head>
<body>
<?php
   
    if($_SERVER["HTTPS"] != "on")
    {
      header("Location: https://" . $_SERVER["HTTP_HOST"] . $_SERVER["REQUEST_URI"]);
      exit();
    }

    $auth_realm = 'MIDS Realm';

    require_once 'auth.php';
?>
  
<div id="container">

    <div id="left_pane">

	<?php

	echo "Welcome, <b>".$_SESSION['username']."</b>.<br />";
	echo '<p><a href="?action=logout">Logout</a></p>';

	?>
	<hr />
	<h2 style="margin-left:10px">Arm/Disarm State</h2>
<?php
    $filepath = "/home/pi/armed.txt";
    $fp = fopen($filepath, "r");
    $state = fread($fp, filesize($filepath));
	 
    if ($state == 1) {
        echo '<img style="margin-left:40px" src="img/red_light.png" />';
	echo '<h3 style="margin-left:20px" >State: <br />ARMED</h3>';
        echo 'Action:   <a href="toggle.php" >Disarm</a>';
    }
    else {
	echo '<img style="margin-left:40px" src="img/green_light.png" />';
	echo '<h3 style="margin-left:20px" >State: DISARMED</h3>';
        echo 'Action:   <a href="toggle.php" >Arm</a>';
    }

    echo '<br />';

    fclose($fp);

    
?>
    <p>Go to: <a href="index.php">View Image</a></p>
    </div>

    <div id="main_pane">
	<h1>MIDS - Mobile Intruder Detection System</h1>
	<a class="toggle_right_pane" href="#">[Show menu]</a>

<br /><br />
<h2>Livestream</h2>
<ul>
    <li>Switching on livestream will turn arming state to DISARMED.</li>
    <li>Switching off livestream will automatically ARM the sensor.</li>
    <li>When switching on livestream, it has a 1.5 seconds delay for the cam to setup before loading the page.</li>
</ul>
<form action="toggleStream.php" method="post">
<?php 
    $filepath = "/home/pi/livestream.txt";
    $fp = fopen($filepath, "r");
    $state = fread($fp, filesize($filepath));
	
    if ($state == 0) {
	echo '<input type="hidden" name="action" value="on" />';
	echo '<button type="submit" id="action">Switch On</button>';
    }
    else {
	echo '<input type="hidden" name="action" value="off" />';
	echo '<button type="submit" id="action">Switch Off</button>';
    }

    fclose($fp);
?>

</form>

<iframe sandbox scrolling="no" style="border:0; width:280px; height:360px;" src="http://192.168.43.52:8085"></iframe>

    </div>
</div>

</body>
</html>
