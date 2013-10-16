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
<?php
    
    if($_SERVER["HTTPS"] != "on")
    {
      header("Location: https://" . $_SERVER["HTTP_HOST"] . $_SERVER["REQUEST_URI"]);
      exit();
    }

    $auth_realm = 'MIDS Realm';

    require_once 'auth.php';
?>

<body>
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
    <p>Go to: <a href="livestream.php">Livestream</a></p>

    </div>

    <div id="main_pane">
	<h1>MIDS - Mobile Intruder Detection System</h1>
	<a class="toggle_right_pane" href="#">[Show menu]</a>


<h2>View Images</h2>
<?php

$dirname = "/home/pi/MIDS/";
$images = glob($dirname."*.*");

foreach ($images as $img) {
  echo '<img src="data:image/jpg;base64,'.base64_encode(file_get_contents($img)).'" />&nbsp;';
  $count++;

  if ($count == 5) {
    $count = 0;
    echo '<br /><br />';
  }
}
?>


    </div>
</div>
</body>
</html>
