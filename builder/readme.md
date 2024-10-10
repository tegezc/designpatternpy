# Builder Pattern

Builder pattern adalah sebuah pola desain creational yang bertujuan untuk memisahkan konstruksi objek kompleks dari representasi akhirnya. Pola ini sangat berguna ketika proses pembuatan objek melibatkan banyak langkah atau memiliki banyak variasi konfigurasi.

## Keuntungan Builder Pattern:

* Memisahkan konstruksi: Proses pembuatan objek dipisahkan dari representasi akhirnya, membuat kode lebih modular dan mudah dipahami.
* Fleksibel: Kita bisa membuat berbagai variasi objek dengan mudah dengan mengganti parameter pada metode-metode builder.
* Membuat kode lebih bersih: Builder pattern membantu mengurangi parameter pada konstruktor kelas.

## Kapan Menggunakan Builder Pattern?


* Objek memiliki banyak parameter konstruktor.
* Proses pembuatan objek melibatkan banyak langkah.
* Kita ingin membuat objek dengan berbagai variasi konfigurasi.

## Contoh Kasus Lain:

* Membangun rumah dengan berbagai tipe kamar, ukuran, dan material.
* Membangun menu makanan dengan berbagai pilihan lauk, sayur, dan minuman.
* Membangun karakter dalam game dengan berbagai atribut dan skill.