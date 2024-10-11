# Flyweight Pattern

Flyweight Pattern adalah desain pola yang bertujuan untuk mengurangi penggunaan objek dengan cara berbagi objek yang memiliki state intrinsik yang sama. Dengan kata lain, kita membuat banyak objek yang terlihat berbeda, tetapi sebenarnya hanya berbagi sebagian kecil dari data internal mereka. Ini sangat berguna ketika kita memiliki banyak objek yang hampir identik, tetapi dengan sedikit variasi.

## Kapan Menggunakan Flyweight Pattern?
* Banyak objek dengan state intrinsik yang sama: Misalnya, banyak pohon dalam sebuah game dengan jenis yang sama.
* Memori terbatas: Pola ini sangat efektif untuk menghemat memori, terutama ketika kita berurusan dengan sejumlah besar objek.
* Kinerja penting: Dengan berbagi objek, kita mengurangi jumlah objek yang perlu dibuat dan dikelola, sehingga meningkatkan kinerja aplikasi.

## Contoh Praktis: Membuat Pohon dalam Game

Mari kita buat contoh sederhana di mana kita membuat banyak pohon dalam sebuah game. Setiap pohon memiliki jenis yang sama (misalnya, pohon pinus), tetapi berada di posisi yang berbeda.

``` python
class Tree:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type

    def draw(self):
        # Logika untuk menggambar pohon berdasarkan jenisnya
        print(f"Menggambar pohon {self.type} di ({self.x}, {self.y})")

# Flyweight factory
class TreeFactory:
    _tree_types = {}

    def get_tree(self, type):
        tree_type = self._tree_types.get(type)
        if not tree_type:
            tree_type = TreeType(type)
            self._tree_types[type] = tree_type
        return Tree(0, 0, tree_type)

class TreeType:
    def __init__(self, type):
        self.type = type

# Penggunaan
tree_factory = TreeFactory()

# Membuat banyak pohon pinus
for i in range(100):
    tree = tree_factory.get_tree("pinus")
    tree.x = i * 10
    tree.y = i
    tree.draw()
```
## Penjelasan:
* TreeType: Kelas ini mewakili state intrinsik dari sebuah pohon (jenisnya).
* TreeFactory: Kelas ini bertindak sebagai factory untuk membuat objek Tree. Ia menyimpan referensi ke objek TreeType yang sudah ada untuk menghindari pembuatan duplikat.
* Tree: Kelas ini mewakili sebuah pohon individual. Ia memiliki posisi (x, y) dan referensi ke TreeType.

## Bagaimana Cara Kerjanya?
1. Ketika kita membuat pohon baru, kita meminta TreeFactory untuk memberikannya.
2. TreeFactory memeriksa apakah jenis pohon tersebut sudah ada.
3. Jika sudah ada, ia mengembalikan objek Tree yang sudah ada dengan posisi yang baru.
4. Jika belum ada, ia membuat objek TreeType baru dan mengembalikan objek Tree baru.


## Keuntungan:
* Menghemat memori: Hanya ada satu objek TreeType untuk setiap jenis pohon, meskipun kita membuat banyak objek Tree.
* Meningkatkan kinerja: Tidak perlu membuat objek TreeType yang sama berulang kali.

## Penting:

* State intrinsik (dalam contoh ini, jenis pohon) harus benar-benar tidak berubah setelah objek dibuat.
* State ekstrinsik (dalam contoh ini, posisi) dapat berubah dan tidak memengaruhi sharing objek.

## Contoh Lain:

* Karakter dalam game: Banyak karakter dengan tampilan yang sama tetapi posisi dan animasi yang berbeda.
* Button dalam aplikasi GUI: Banyak button dengan teks dan tampilan yang sama tetapi fungsi yang berbeda.


## Kesimpulan
Flyweight Pattern adalah alat yang sangat berguna untuk mengoptimalkan penggunaan memori dan meningkatkan kinerja aplikasi, terutama ketika kita berurusan dengan sejumlah besar objek yang hampir identik. Dengan memahami konsep ini, Anda dapat menerapkannya dalam berbagai situasi untuk membuat aplikasi yang lebih efisien.

## Contoh Lain Flyweight Pattern:

1. Karakter dalam Game Online:

* State Intrinsik: Jenis karakter (human, orc, elf), ras, kelas, statistik dasar (strength, agility, intelligence).
* State Ekstrinsik: Posisi, peralatan, level, pengalaman, kesehatan, mana.
* Penerapan: Setiap jenis karakter hanya perlu dibuat satu kali. Saat pemain membuat karakter baru, sistem hanya perlu membuat instance baru dengan nilai state ekstrinsik yang berbeda-beda. Ini menghemat memori, terutama dalam game online dengan banyak pemain.

2. Font dalam Aplikasi Pengolah Kata:

* State Intrinsik: Jenis font (Times New Roman, Arial, Helvetica), ukuran, gaya (bold, italic).
* State Ekstrinsik: Teks yang ditulis, posisi dalam dokumen.
* Penerapan: Setiap kombinasi jenis font, ukuran, dan gaya hanya perlu dibuat satu kali. Saat pengguna mengetik teks dengan pengaturan font tertentu, sistem hanya perlu membuat instance baru dengan teks yang berbeda.

3. Icon dalam Aplikasi:

* State Intrinsik: Jenis icon (folder, file, user), ukuran, warna.
* State Ekstrinsik: Posisi di layar.
* Penerapan: Setiap jenis icon hanya perlu dibuat satu kali. Saat aplikasi menampilkan banyak icon yang sama, sistem hanya perlu membuat instance baru dengan posisi yang berbeda.

4. Produk dalam E-commerce:

* State Intrinsik: Nama produk, deskripsi, kategori, harga dasar.
* State Ekstrinsik: Jumlah yang dipesan, diskon, pajak.
* Penerapan: Setiap produk hanya perlu disimpan satu kali dalam database. Saat pelanggan menambahkan produk ke keranjang belanja, sistem hanya perlu membuat instance baru dengan jumlah dan diskon yang berbeda.

## Hal Penting yang Perlu Diingat:

* Identifikasi State Intrinsik dan Ekstrinsik: Membedakan dengan jelas antara state intrinsik dan ekstrinsik sangat penting untuk menerapkan Flyweight Pattern dengan benar.
* Factory Pattern: Seringkali, Flyweight Pattern dikombinasikan dengan Factory Pattern untuk membuat dan mengelola objek Flyweight.
* Trade-off: Flyweight Pattern mungkin memerlukan sedikit overhead tambahan untuk mengelola objek Flyweight. Namun, keuntungannya dalam hal penghematan memori dan peningkatan kinerja biasanya jauh lebih besar.