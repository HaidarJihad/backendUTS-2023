<?php
$ns1 = ['id'=>1,'nim'=>'01111', 'uts'=>80, 'uas'=>80, 'tugas'=>78];
$ns2 = ['id'=>2,'nim'=>'01112', 'uts'=>81, 'uas'=>81, 'tugas'=>79];
$ns3 = ['id'=>3,'nim'=>'01113', 'uts'=>82, 'uas'=>82, 'tugas'=>80];
$ns4 = ['id'=>4,'nim'=>'01114', 'uts'=>83, 'uas'=>83, 'tugas'=>81];
$ar_nilai = [$ns1,$ns2,$ns3,$ns4];
?>

<h3>Daftar nilai Siswa</h3>
<table>
    <thead>
        <tr>
            <th>NO</th>
            <th>NIM</th>
            <th>UTS</th>
            <th>Tugas</th>
            <th>Nilai Akhir</th>
        </tr>
    </thead>
    <tbody>
        <?php
        $no = 1;
        foreach ($ar_nilai as $ns) {
            echo "<tr><td>".$no."<td>";
            echo "<td>".$ns['nim']."</td>";
            echo "<td>".$ns['uts']."</td>";
            echo "<td>".$ns['uas']."</td>";
            echo "<td>".$ns['tugas']."</td>";
            $nilai_akhir = ($ns['uts'] + $ns['uas']+$ns['tugas'])/3;
            echo '<td>'.number_format($nilai_akhir,2,',','.').'</td>';
            echo '<tr/>';
            $no++;
        }
        ?>
    </tbody>


</table>