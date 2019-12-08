<?php 

require('fpdf/fpdf.php'); 
$xml=simplexml_load_file("questions22.xml") or die("Error: Cannot create object");
// New object created and constructor invoked 
$pdf = new FPDF(); 

$xml=simplexml_load_file("questions22.xml") or die("Error: Cannot create object");

$counter =  $xml->question->count();
// echo $counter;
// for ($i=0;$i<$counter;$i++){
// echo $xml->question[$i]->ques . "<br>";
// echo $xml->question[$i]->option1 . "<br>";
// echo $xml->question[$i]->option2 . "<br>";
// echo $xml->question[$i]->option3 . "<br>";
// echo $xml->question[$i]->option4 . "<br>";
// }

// Add new pages. By default no pages available. 
$pdf->AddPage(); 

// Set font format and font-size 
$pdf->SetFont('Times', 'B', 20); 

// Framed rectangular area 
$pdf->Cell(176, 5, 'Multiple Choice Questions', 0, 0, 'C'); 

// Set it new line 
$pdf->Ln(); 

// Set font format and font-size 
$pdf->SetFont('Times', 'B', 12); 

// Framed rectangular area 
$pdf->Cell(176, 10, 'Test Generated from Quru', 0, 0, 'C'); 

$pdf->SetFont('Times', 'B', 10); 
$pdf->Ln(); 
// $pdf->Ln(); 

for ($i=0;$i<$counter;$i++){
    // $ques = "Question "+($i+1)+": "+question[$i]
    $pdf->Multicell(176, 5,'Q'.($i+1).': '. $xml->question[$i]->ques);
    // $pdf->Ln();  
    // echo $xml->question[$i]->ques . "<br>";
    
    $pdf->Multicell(176, 5,'A. '. $xml->question[$i]->option1);
    $pdf->Multicell(176, 5,"B. ".$xml->question[$i]->option2);
    $pdf->Multicell(176, 5,"C. ".$xml->question[$i]->option3);
    $pdf->Multicell(176, 5,"D. ".$xml->question[$i]->option4);
    // echo $xml->question[$i]->option1 . "<br>";
    // echo $xml->question[$i]->option2 . "<br>";
    // echo $xml->question[$i]->option3 . "<br>";
    // echo $xml->question[$i]->option4 . "<br>";
    $pdf->Ln();  
    }
    

// Close document and sent to the browser 
$pdf->Output(); 

?> 
