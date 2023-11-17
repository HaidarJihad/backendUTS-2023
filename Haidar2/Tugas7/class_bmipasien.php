<?php
class Bmipasien {
    public $nama;
    public $umur;
    public $jenis_kelamin;
    public $berat;
    public $tinggi;

public function hasilBMI() {
    $tinggi_m = $this-> tinggi / 100;
    $bmi = $this->berat / ($tinggi_m ** 2);
    return $bmi;
}

public function statusBMI() {
    $bmi = $this->hasilBMI();
    if ($bmi < 18.5) {
        return "Kekurangan berat badan";
    } elseif ($bmi < 25) {
        return "Normal (ideal)";
    } elseif ($bmi < 30) {
        return "Kelebihan berat badan";
    } else {
        return "obesitas";
    }
}
}
?>