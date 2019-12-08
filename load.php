<!--  -->
<html>
<head> 
<link rel="icon" href="img/logo1.png" type="image/gif" sizes="16x16">
<title>Quru
</title>
</head>
<!-- scriptFunc(); -->
<body onload="scriptFunc()">


	

	<div id="lo" style = "background-image:url('img/icon.gif'); height: 100%; width: 100%; background-size:auto; background-position: center; background-repeat: no-repeat; display: block;">
		
	</div>
	<div id = "contents">

	</div>

<script type="text/javascript">
	
	// window.setTimeout(function(){
	// 	document.getElementById("lo").style.display="None";
	// 	window.location.replace("result.html");
	// },10000);
	// function hideDiv(){

		
	// 	alert();
	// }

	function scriptFunc(){
		var xhttp = new XMLHttpRequest();
  		xhttp.onreadystatechange = function() {
    	if (this.readyState == 4 && this.status == 200) {
			window.location.replace("result.html");
    }
  };
  xhttp.open("GET", "script.php", true);
  xhttp.send();
	}
</script>
</body>

<!-- <script type="text/javascript">
	
document.onreadystatechange = function () {
  var state = document.readyState
  if (state == 'interactive') {
       document.getElementById('contents').style.visibility="hidden";
  } else if (state == 'complete') {
      setTimeout(function(){
         document.getElementById('interactive');
         document.getElementById('load').style.visibility="hidden";
         document.getElementById('contents').style.visibility="visible";
      },2000);
  }
}

</script> -->