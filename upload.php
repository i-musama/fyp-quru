<?php
$target_dir = "backEnd/";
// $target_file = $target_dir . "input.pptx";
echo $target_file = $target_dir . "input.".strtolower(pathinfo($_FILES["fileToUpload"]["name"],PATHINFO_EXTENSION));
$uploadOk = 1;
 $imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));
// Check if image file is a actual image or fake image
if(isset($_POST["uploadBtn"]) == "Generate") {

    if($imageFileType != "txt"){
    echo "Sorry, only .txt files are allowed."; 
    $uploadOk = 0;
  }
  else
  {
    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
        echo "The file has been uploaded.";
        // if($imageFileType == "txt"){
        //   echo "in TXT";
        //   // exec("server_txt.bat > server_txt_log.txt");
        //   header("Location:load.php");
        // }
          header("Location:load.php");
      } else {
        echo "Sorry, there was an error uploading your file.";
      }
  }
}

else if(isset($_POST["paste"]))
{

   $text = $_POST["setText"];
  //echo "in text";
   // if($text == "")
   // {
   //  header("Location:index.html");
   // }
   // else{

  $myfile = fopen("backEnd/input.txt", "w") or die("Unable to open file!");
  //$txt = "user id date";
  fwrite($myfile, "\n". $text);
  fclose($myfile);
  // exec("server_txt.bat > server_txt_log.txt");
  header("Location:load.php");
// }
  
}



?>