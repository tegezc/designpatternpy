Apa itu Singleton?
Singleton adalah pola desain creational yang memastikan hanya ada satu instance (objek) dari suatu kelas selama program berjalan. Ini berguna ketika kita hanya membutuhkan satu objek tunggal untuk mengelola sumber daya atau konfigurasi tertentu.

Contoh Kasus Penggunaan:

Koneksi database: Hanya perlu ada satu koneksi database untuk seluruh aplikasi.
Logger: Satu objek logger untuk mencatat semua aktivitas aplikasi.
Konfigurasi: Satu objek konfigurasi untuk menyimpan semua pengaturan aplikasi.
Implementasi Singleton di Python
Ada beberapa cara untuk mengimplementasikan Singleton di Python. Berikut adalah beberapa metode yang umum digunakan: