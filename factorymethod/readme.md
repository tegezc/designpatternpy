# Factory Method

## Apa itu Factory Pattern?
Factory Pattern adalah salah satu design pattern dalam pemrograman yang bertujuan untuk menyembunyikan logika pembuatan objek. Dengan kata lain, kita tidak perlu lagi menulis new secara langsung untuk membuat objek baru, melainkan menggunakan sebuah factory yang akan membuatkan objek tersebut untuk kita.

## Mengapa menggunakan Factory Pattern?

* Abstraksi: Memisahkan pembuatan objek dari penggunaan objek.
* Fleksibelitas: Memungkinkan kita untuk mengubah implementasi objek tanpa mengubah kode yang menggunakannya.
* Ekstensibilitas: Mudah menambahkan jenis objek baru tanpa mengubah struktur kode yang sudah ada.

## Kapan Menggunakan Factory Pattern?

* Saat ingin menyembunyikan kompleksitas pembuatan objek.
* Saat ingin membuat objek berdasarkan konfigurasi atau kondisi tertentu.
* Saat ingin membuat hirarki kelas yang fleksibel.