# Adapter Pattern

Adapter Pattern adalah salah satu pola desain struktural yang memungkinkan kelas atau objek dengan antarmuka yang berbeda untuk bekerja sama. Bayangkan Anda memiliki dua buah objek dengan bentuk colokan yang berbeda. Adapter akan berfungsi sebagai "penghubung" agar kedua objek tersebut dapat terhubung dan bekerja sama.

## Tujuan utama Adapter Pattern:

* Mengadaptasi antarmuka: Membuat antarmuka yang tidak kompatibel menjadi kompatibel.
* Meningkatkan reusabilitas kode: Memungkinkan penggunaan kelas yang sudah ada tanpa perlu mengubah kodenya.
* Meningkatkan fleksibilitas: Memudahkan integrasi antara kelas-kelas yang berbeda.

## Contoh Implementasi dalam Python
Mari kita ambil contoh sederhana: kita memiliki kelas OldShape dengan metode draw() yang menggunakan koordinat (x, y), sedangkan kita memiliki kelas NewShape dengan metode draw() yang menggunakan objek Point.

```python
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

```python
class ShapeAdapter:
    def __init__(self, new_shape):
        self.new_shape = new_shape

    def draw(self, x, y):
        point = Point(x, y)
        self.new_shape.draw(point)
```

## * Penjelasan:

* ShapeAdapter: Kelas ini bertindak sebagai adapter. Ia memiliki atribut new_shape yang merujuk ke objek NewShape.
* Metode draw: Metode ini menerima parameter yang sama dengan metode draw() pada OldShape. Di dalam metode ini, kita membuat objek Point baru berdasarkan parameter yang diberikan, lalu memanggil metode draw() pada objek NewShape.

## Penggunaan

```python
old_shape = OldShape()
new_shape = NewShape()
adapter = ShapeAdapter(new_shape)

old_shape.draw(10, 20)  # Output: Drawing old shape at (10, 20)
adapter.draw(30, 40)  # Output: Drawing new shape at (30, 40)
```
## Penjelasan:

* Kita membuat objek dari ketiga kelas.
* Saat kita memanggil adapter.draw(), sebenarnya kita sedang memanggil metode draw() pada objek NewShape melalui adapter.

## Kapan Menggunakan Adapter Pattern?
* Ketika Anda ingin menggunakan kelas yang sudah ada tetapi memiliki antarmuka yang berbeda.
* Ketika Anda ingin membuat kelas-kelas yang berbeda dapat bekerja sama tanpa mengubah kode internalnya.
* Ketika Anda ingin menyediakan antarmuka yang seragam untuk beberapa kelas yang berbeda.


## Contoh Kasus Nyata:

1. Mengadaptasi library pihak ketiga: Anda mungkin ingin menggunakan library yang memiliki antarmuka yang berbeda dengan proyek Anda. Adapter dapat membantu Anda mengadaptasi library tersebut.
2. Mengubah format data: Anda mungkin perlu mengubah format data dari satu sistem ke sistem lainnya. Adapter dapat membantu Anda melakukan konversi data tersebut.
