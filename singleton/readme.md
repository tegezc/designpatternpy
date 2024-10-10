#Singleton

Apa itu Singleton?
Singleton adalah pola desain creational yang memastikan hanya ada satu instance (objek) dari suatu kelas selama program berjalan. Ini berguna ketika kita hanya membutuhkan satu objek tunggal untuk mengelola sumber daya atau konfigurasi tertentu.

Contoh Kasus Penggunaan:

*Koneksi database: Hanya perlu ada satu koneksi database untuk seluruh aplikasi.
*Logger: Satu objek logger untuk mencatat semua aktivitas aplikasi.
*Konfigurasi: Satu objek konfigurasi untuk menyimpan semua pengaturan aplikasi.

Kapan Menggunakan Singleton?
Meskipun Singleton memiliki kegunaan, ada beberapa hal yang perlu dipertimbangkan sebelum menggunakannya:

*Testabilitas: Singleton dapat membuat kode sulit untuk diuji karena ketergantungan global.
*Ketergantungan: Penggunaan Singleton yang berlebihan dapat membuat kode menjadi sangat terkait satu sama lain.
*Multithreading: Dalam lingkungan multithreading, Singleton mungkin memerlukan mekanisme locking untuk menghindari masalah konkurensi.