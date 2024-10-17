# Iterator Pattern
Iterator Pattern adalah pola desain perilaku yang memungkinkan kita untuk menelusuri elemen-elemen dalam suatu koleksi data (seperti list, tuple, atau struktur data kustom) secara berurutan, tanpa perlu mengetahui detail implementasi internal dari koleksi tersebut. Ini memberikan cara yang seragam untuk mengakses elemen-elemen dari berbagai jenis koleksi.

## Komponen Utama:

- Iterable: Objek yang dapat diiterasi, memiliki metode __iter__() yang mengembalikan iterator.
- Iterator: Objek yang digunakan untuk menelusuri elemen-elemen, memiliki metode __next__() yang mengembalikan elemen berikutnya dan __iter__() yang mengembalikan dirinya sendiri.

## Mengapa Menggunakan Iterator Pattern?

- Abstraksi: Menyembunyikan kompleksitas struktur data internal.
- Fleksibilitas: Memungkinkan berbagai cara untuk menelusuri koleksi yang sama.
- Efisiensi: Memungkinkan penelusuran elemen secara bertahap, tidak perlu memuat seluruh data ke dalam memori sekaligus.

``` python
class MyList:
    def __init__(self, data):
        self._data = data
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._data):
            raise StopIteration
        else:
            item = self._data[self._index]
            self._index += 1
            return item

# Penggunaan
my_list = MyList([1, 2, 3])
for item in my_list:
    print(item)
```
## Penjelasan:

1. Kelas MyList:
- __iter__(): Mengembalikan objek MyList itu sendiri, karena MyList juga berperan sebagai iterator.
- __next__(): Mengembalikan elemen berikutnya dalam daftar, dan meningkatkan indeks. Jika tidak ada elemen lagi, raise StopIteration.
2. Penggunaan:
for loop secara otomatis memanggil __iter__() dan __next__() untuk menelusuri elemen-elemen dalam my_list.

## Contoh lain: Iterator di pohon biner

``` python
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeIterator:
    def __init__(self, root):
        self.nodes = [root]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.nodes:
            raise StopIteration
        current = self.nodes.pop(0)
        if current.left:
            self.nodes.append(current.left)
        if current.right:
            self.nodes.append(current.right)
        return current.value

# Penggunaan
root = Node(1, Node(2), Node(3))
for value in TreeIterator(root):
    print(value)
```
## Penjelasan:

Kelas TreeIterator:
- Menggunakan stack untuk melakukan traversal inorder pada pohon biner.
- __next__(): Mengambil node dari atas stack, dan menambahkan anak-anaknya ke dalam stack.
Iterator Built-in di Python

## Python menyediakan banyak iterator built-in:
- range(): Untuk menghasilkan urutan angka.
- enumerate(): Untuk mengembalikan indeks dan nilai elemen dalam suatu iterable.
- zip(): Untuk menggabungkan beberapa iterable menjadi satu.
- Dan masih banyak lagi.

## Penggunaan Iterator dalam Praktik
- Generator: Fungsi yang menghasilkan nilai secara bertahap menggunakan yield.
- Comprehension: List, set, dan dictionary comprehension.
- Library: Banyak library seperti Pandas, NumPy, dan Scikit-learn menggunakan iterator secara ekstensif untuk efisiensi.