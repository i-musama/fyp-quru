<?php
$xml=simplexml_load_file("questions22.xml") or die("Error: Cannot create object");

$counter =  $xml->question->count();
echo $counter;
for ($i=0;$i<$counter;$i++){
echo $xml->question[$i]->ques . "<br>";
echo $xml->question[$i]->option1 . "<br>";
echo $xml->question[$i]->option2 . "<br>";
echo $xml->question[$i]->option3 . "<br>";
echo $xml->question[$i]->option4 . "<br>";
}
// foreach($xml->children() as $books) {
//     echo $books;
//     echo "<br>";
//     foreach($books->children() as $book){
//     echo $books;
//     echo "<br>";}
// }
?>
