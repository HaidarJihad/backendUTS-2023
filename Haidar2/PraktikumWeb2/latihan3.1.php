<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form Registrasi</title>
</head>
<body>
<?php

$ar_prodi = ["SI"=>"Sistem Informasi", "IT"=> "Teknik Informatika", "BD"=>"Bisnis Digital"];
$ar_skill = ["HTML"=>10, "CSS"=>10, "JavaScript"=>20, "RWD Bootstrap"=>20, "PHP"=>30, "Python"=>30, "Java"=>50];
$ar_domisili = ["Jakarta","Depok","Bogor","Tangerang","Bekasi","Lainnya"];

?>
    <fieldset style="background-color: #B0C4DE;">
        <legend>Form Registrasi It club Data Science</legend>

        <table>
            <tr>
                <th>Form Registrasi</th>
            </tr>
            <tr>
                <th>
                    <form method="POST"></form>
                </th>
            </tr>
            <tr>
                <td>NIM</td>
                <td><input type="text" name="nim" value="" size="30"></td>
            </tr>
            <tr>
                <td>Nama</td>
                <td><input type="text" name="nama" value="" size="30"></td>
            </tr>
            <tr>
                <td>Jenis Kelamin</td>
                <td><input type="radio" name="jk" value="" size="30">Laki-laki
                <input type="radio" name="jk" value="" size="30">Perempuan</td>
            </tr>
            <tr>
                <td>Program Studi</td>
                <td>
                    <select name="prodi">
                        <?php

                            foreach($ar_prodi as $prodi => $p){ ?>

                        <option value="<?= $prodi ?>"><?= $p ?></option>
                        
                        <?php }?>
                    </select>
                </td>
            </tr>
            <tr>
                <td>Skill Programming</td>
                <td>
                <?php
                 foreach($ar_skill as $skill => $s){
                ?>
                <input type="checkbox" name="skill[]" value="<?= $s ?>"><?= $skill ?>
                <?php } ?>
                 </td>
            </tr>
            <tr>
                <td>Tempat Domisili </td>
                <td>
                    <select name="Domilisi">
                        <?php
                
                            foreach($ar_domisili as $domisili){  ?>

                        <option value="<?= $domisili ?>"><?= $domisili ?></option>

                        <?php }?>
                    </select>
                </td>
            </tr>
            <tr>
                <td>
                    <button name="proses">Simpan</button>
                    
                </td> 
            </tr>
        </table>

    </fieldset>
    
    <?php
    if(isset($_POST['proses'])){

    $nim = $_POST['nim'];
    $nama = $_POST['nama'];
    $jk = $_POST['jk'];
    $prodi = $_POST['prodi'];
    $skill = $_POST['skill'];
    ?>
    <br>NIM                    : <?= $nim ?>
    <br>Nama                     : <?= $nama ?>
    <br>Jenis Kelamin           : <?= $jk ?>
    <br>Program Studi           : <?= $prodi ?>
    <br>Skill Web & Programming : <?= $skill ?>
<?php
    function skor_skill($total){
        if($total >= 100 && $total <= 159 ) {
            return "Sangat Baik";
        } elseif ($total >= 60 && $total <= 150 ) {
            return "Baik";
        } elseif ($total >= 40 && $total <= 100) {
            return "Cukup";
        
        } else {
            return "Tidak Memadai";
        }
    }
}
?>

</body>
</html>