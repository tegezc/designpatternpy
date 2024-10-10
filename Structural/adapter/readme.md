# Adapter Pattern

Adapter Pattern adalah salah satu pola desain struktural yang memungkinkan kelas atau objek dengan antarmuka yang berbeda untuk bekerja sama. Bayangkan Anda memiliki dua buah objek dengan bentuk colokan yang berbeda. Adapter akan berfungsi sebagai "penghubung" agar kedua objek tersebut dapat terhubung dan bekerja sama.

## Tujuan utama Adapter Pattern:

* Mengadaptasi antarmuka: Membuat antarmuka yang tidak kompatibel menjadi kompatibel.
* Meningkatkan reusabilitas kode: Memungkinkan penggunaan kelas yang sudah ada tanpa perlu mengubah kodenya.
* Meningkatkan fleksibilitas: Memudahkan integrasi antara kelas-kelas yang berbeda.

## Contoh Implementasi dalam Python
Mari kita ambil contoh sederhana: kita memiliki kelas OldShape dengan metode draw() yang menggunakan koordinat (x, y), sedangkan kita memiliki kelas NewShape dengan metode draw() yang menggunakan objek Point.

``` 
class OldShape:
    def draw(self, x, y):
        print(f"Drawing old shape at ({x}, {y})")

class NewShape:
    def draw(self, point):
        print(f"Drawing new shape at ({point.x}, {point.y})")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

Untuk membuat kedua kelas ini dapat bekerja sama, kita akan membuat sebuah adapter: