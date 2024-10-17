# Interpreter Pattern

pattern rancangan interpreter adalah sebuah pattern desain perilaku yang memungkinkan kita untuk membuat sebuah bahasa sederhana (mini-language) dalam sebuah bahasa pemrograman yang lebih besar. Intinya, kita membangun sebuah parser yang dapat memahami dan mengeksekusi sintaks bahasa sederhana tersebut.

## Kapan kita menggunakannya?

- Membuat bahasa khusus domain (DSL): Ketika kita ingin membuat bahasa yang sangat spesifik untuk memecahkan masalah tertentu, misalnya bahasa untuk mengekspresikan query pada database atau konfigurasi aplikasi.
- Implementasi kalkulator: Membuat kalkulator sederhana dengan operasi aritmatika.
- Kompilator sederhana: Meskipun biasanya kompilator lebih kompleks, pattern interpreter bisa menjadi dasar untuk membuat kompilator sederhana.

## Contoh Implementasi dalam Python

Mari kita buat sebuah interpreter sederhana untuk bahasa ekspresi aritmatika dasar. Bahasa ini hanya akan mendukung penjumlahan, pengurangan, perkalian, dan pembagian.

``` python
from abc import ABC, abstractmethod

class Node(ABC):
    @abstractmethod
    def evaluate(self):
        pass

class Number(Node):
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value

class BinaryOperation(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Add(BinaryOperation):
    def evaluate(self):
        return self.left.evaluate() + self.right.evaluate()

class Subtract(BinaryOperation):
    def evaluate(self):
        return self.left.evaluate() - self.right.evaluate()

class Multiply(BinaryOperation):
    def evaluate(self):
        return self.left.evaluate() * self.right.evaluate()

class Divide(BinaryOperation):
    def evaluate(self.
        try:
            return self.left.evaluate() / self.right.evaluate()
        except ZeroDivisionError:
            return float('inf')

# Contoh penggunaan
# Ekspresi: (3 + 5) * 2
expression = Multiply(
    Add(Number(3), Number(5)),
    Number(2)
)
result = expression.evaluate()
print(result)  # Output: 16
```
## Penjelasan Kode:

1. Hierarki Kelas:
    - Node: Kelas abstrak sebagai akar dari hirarki.
    - Number: Kelas untuk merepresentasikan angka.
    - BinaryOperation: Kelas abstrak untuk operasi biner (penjumlahan, pengurangan, dll.).
    - Kelas-kelas turunan dari BinaryOperation untuk setiap operasi.
2. Metode evaluate:
Setiap kelas yang mewarisi dari Node harus mengimplementasikan metode evaluate untuk menghitung nilai ekspresi.

3. Membangun Pohon Parse:
Kita membangun sebuah pohon parse (parse tree) untuk merepresentasikan ekspresi. Setiap node dalam pohon adalah sebuah objek dari kelas yang sesuai.

4. Mengevaluasi Ekspresi:
Metode evaluate secara rekursif mengevaluasi pohon parse dari bawah ke atas.

## Kelebihan dan Kekurangan pattern Interpreter
### Kelebihan:
- Fleksibel untuk membuat bahasa sederhana.
- Mudah untuk menambahkan fitur baru.
- Mudah untuk diubah.
### Kekurangan:
- Performanya umumnya lebih lambat dibandingkan dengan kode yang dikompilasi.
- Implementasinya bisa menjadi kompleks untuk bahasa yang lebih besar.

## Kesimpulan
pattern rancangan interpreter sangat berguna ketika kita ingin membuat bahasa khusus domain atau bahasa sederhana untuk keperluan tertentu. Meskipun performanya mungkin tidak secepat kode yang dikompilasi, fleksibilitasnya membuatnya menjadi pilihan yang baik untuk banyak kasus penggunaan.