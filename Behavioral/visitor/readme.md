# Visitor Pattern

Visitor Pattern adalah design pattern dalam pemrograman yang memisahkan algoritma dari struktur data. Pattern ini memungkinkan kita untuk menambahkan operasi baru ke struktur data yang sudah ada tanpa mengubah kelas-kelas dalam struktur data tersebut.

## Kapan kita menggunakan Visitor Pattern?

- Ketika kita memiliki banyak kelas yang memiliki struktur data serupa tetapi operasi yang berbeda.
- Ketika kita ingin menambahkan operasi baru ke struktur data tanpa mengubah kelas-kelas yang ada.
- Ketika kita ingin melakukan operasi yang kompleks pada struktur data yang hierarkis.

## Komponen Utama Visitor Pattern:

- Visitor: Interface yang mendefinisikan metode untuk setiap kelas dalam struktur data.
ConcreteVisitor: Implementasi dari interface Visitor yang berisi logika spesifik untuk setiap operasi.
- Element: Interface untuk elemen dalam struktur data.
- ConcreteElement: Implementasi dari interface Element yang mewakili elemen-elemen konkret dalam struktur data.

## Contoh Implementasi dalam Python
Mari kita buat contoh sederhana dengan struktur data yang mewakili bentuk geometri (lingkaran dan persegi panjang). Kita akan membuat visitor untuk menghitung luas dan keliling setiap bentuk.

``` python
from abc import ABC, abstractmethod

# Interface untuk elemen
class Shape(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

# Implementasi elemen konkret
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def accept(self, visitor):
        visitor.visit_circle(self)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def accept(self, visitor):
        visitor.visit_rectangle(self)

# Interface untuk visitor
class ShapeVisitor(ABC):
    @abstractmethod
    def visit_circle(self, circle):
        pass

    @abstractmethod
    def visit_rectangle(self, rectangle):
        pass

# Implementasi visitor konkret
class AreaCalculator(ShapeVisitor):
    def visit_circle(self, circle):
        return 3.14 * circle.radius**2

    def visit_rectangle(self, rectangle):
        return rectangle.width * rectangle.height

# Penggunaan
circle = Circle(5)
rectangle = Rectangle(4, 6)

calculator = AreaCalculator()
print(circle.accept(calculator))  # Output: 78.5
print(rectangle.accept(calculator))  # Output: 24
```
## Penjelasan:

- Shape: Interface untuk semua bentuk geometri.
- Circle dan Rectangle: Implementasi konkret dari Shape.
- ShapeVisitor: Interface untuk semua visitor.
- AreaCalculator: Implementasi konkret dari ShapeVisitor untuk menghitung luas.
- accept() method pada setiap elemen memanggil metode visit yang sesuai pada visitor.

## Kelebihan Visitor Pattern:

- Pemisahan tanggung jawab: Algoritma (visitor) dipisahkan dari struktur data (elemen).
- Ekstensibilitas: Mudah menambahkan operasi baru dengan membuat visitor baru.
- Reusabilitas: Visitor dapat digunakan pada berbagai struktur data yang memiliki interface yang sama.

## Kekurangan Visitor Pattern:

- Kompleksitas: Dapat membuat kode menjadi lebih kompleks, terutama untuk struktur data yang besar dan kompleks.
- Ketergantungan: Visitor menjadi sangat terikat dengan struktur data.


## Kapan sebaiknya tidak menggunakan Visitor Pattern:

- Untuk struktur data yang sederhana dan tidak sering berubah.
- Ketika menambahkan operasi baru tidak sering dilakukan.

## Lain lain

 Nama "Visitor" dalam Visitor Pattern memang terdengar sedikit membingungkan pada awalnya. mengapa nama ini digunakan dan mengapa mungkin terasa kurang intuitif.

Konotasi Terlalu Literal: Kata "visitor" mungkin terlalu kaku dan membatasi pemahaman kita tentang pola ini. Istilah seperti "operator", "aksi", atau "perintah" mungkin lebih menggambarkan esensi dari visitor.
Peran Aktif: Visitor tidak hanya "mengunjungi" tetapi juga "melakukan sesuatu" pada elemen yang dikunjungi.
Analogi yang Lebih Tepat

Meskipun nama "Visitor" mungkin kurang intuitif, konsep di baliknya sangat kuat dan berguna. Intinya adalah memisahkan algoritma (visitor) dari struktur data (elemen). Dengan memahami konsep ini, Anda dapat menggunakan Visitor Pattern untuk membuat kode yang lebih fleksibel, mudah dipelihara, dan mudah diperluas.

## Tapi, Kenapa Nama Ini Tetap Dipakai?

### Mungkin karena:
- Sudah Jadi Standar: Namanya udah terlanjur populer, jadi susah diganti.
- Konsep Abstrak: Mungkin yang bikin nama ini susah dicerna adalah konsepnya yang memang agak abstrak. "Visitor" dianggap bisa mewakili konsep "mengunjungi" setiap elemen dalam struktur data untuk melakukan operasi tertentu.