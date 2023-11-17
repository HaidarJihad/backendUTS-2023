<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form method="POST">
    Nama : <input type="text" name="nama" value="" size="30"><br>
    Mata Kuliah : 
    <select name="matkul">
        <option value="DDP">Dasar-Dasar Pemograman</option>
        <option value="BDI">Basis Data 1</option>
        <option value="WEB1">Pemograman Web</option>
    </select><br>
    Nilai UTS : <input type="text" name="nilai_uts" value="" size="6"><br>
    Nilai UAS : <input type="text" name="nilai_uas" value="" size="6"><br>
    Nilai Tugas/Praktikum : <input type="text" name="nilai_tugas" value="" size="6"><br>
    <button name="proses">Simpen</button>
    </form>

<?php
error_reporting(0);
$proses = $_POST['proses'];
$nama_siswa = $POST['nama'];
$mata_kuliah = $_POST['matkul'];
$nilai_uts = $_POST['nilai_uts'];
$nilai_uas = $_POST['nilai_uas'];
$nilai_tugas = $_POST['nilai_tugas'];

if(!empty($proses)) {
?>

<?= $proses ?>
Nama Siswa <?= $nama_siswa ?>
<br>Matakuliah <?= $mata_kuliah ?>
<br>nilai UTS <?= $nilai_uts ?>
<br>nilai UAS <?= $nilai_uas ?>
<br>nilai tugas <?= $nilai_tugas ?>

<?php } ?>
</body>
</html>