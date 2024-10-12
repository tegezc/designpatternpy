# Template Mehod Pattern

Template Method pattern adalah sebuah pattern behavioral yang mendefinisikan algoritma dasar dalam suatu operasi, tetapi menunda beberapa langkah implementasinya ke subkelas. Dengan kata lain, kelas induk menyediakan kerangka umum suatu algoritma, sementara kelas turunan dapat mengoverride langkah-langkah tertentu untuk menyesuaikan perilaku sesuai kebutuhan.

## Kapan Menggunakan Template Method?

- Ketika kamu ingin memiliki algoritma yang sebagian besar sudah terdefinisi, tetapi ingin memberikan fleksibilitas pada subkelas untuk mengimplementasikan beberapa bagian dari algoritma tersebut.
- Ketika kamu ingin memastikan bahwa semua subkelas mengikuti urutan langkah yang sama, tetapi dengan implementasi yang berbeda pada langkah-langkah tertentu.

## Contoh: Membuat Kopi

Mari kita ambil contoh sederhana membuat kopi. Algoritma dasarnya adalah:

1. Rebus air
2. Tambahkan kopi bubuk
3. Saring
4. Tambahkan gula (opsional)
5. Tambahkan susu (opsional)

Kelas induk Coffee akan mendefinisikan kerangka algoritma ini, sementara kelas turunan seperti BlackCoffee, Latte, dan Cappuccino akan mengoverride langkah-langkah opsional (menambahkan gula dan susu) untuk menyesuaikan jenis kopi yang berbeda.

``` python
class Coffee:
    def make_coffee(self):
        self.boil_water()
        self.brew_coffee_with_water()
        self.pour_in_cup()
        self.add_suger()
        self.add_milk()

    def boil_water(self):
        print("Rebus air")

    def brew_coffee_with_water(self):
        print("Seduh kopi dengan air")

    def pour_in_cup(self):
        print("Tuang ke dalam cangkir")

    def add_suger(self):
        pass

    def add_milk(self):
        pass

class BlackCoffee(Coffee):
    pass  # Tidak ada penambahan gula atau susu

class Latte(Coffee):
    def add_milk(self):
        print("Tambahkan susu")

class Cappuccino(Latte):
    def add_milk(self):
        print("Tambahkan busa susu")

# Penggunaan
black_coffee = BlackCoffee()
black_coffee.make_coffee()

latte = Latte()
latte.make_coffee()

cappuccino = Cappuccino()
cappuccino.make_coffee()
```
## Penjelasan:

* Kelas Coffee:
    - Metode make_coffee() adalah metode template yang mendefinisikan urutan langkah membuat kopi.
    - Metode add_suger() dan add_milk() diimplementasikan sebagai kosong, karena bersifat opsional.
* Kelas BlackCoffee:
    - Tidak mengoverride metode apa pun, sehingga tidak ada penambahan gula atau susu.
* Kelas Latte:
    - Mengoverride metode add_milk() untuk menambahkan susu.
*Kelas Cappuccino:
    - Menurun dari Latte dan mengoverride add_milk() lagi untuk menambahkan busa susu.

## Keuntungan Menggunakan Template Method:

- Koding yang lebih bersih dan terstruktur: Memisahkan algoritma umum dengan variasi implementasi.
- Fleksibilitas: Subkelas dapat menyesuaikan perilaku tanpa mengubah kelas induk.
- Kemudahan pemeliharaan: Perubahan pada algoritma umum hanya perlu dilakukan sekali di kelas induk.

## Contoh Lain:

- Framework web: Banyak framework web menggunakan Template Method untuk mengatur alur permintaan (request) dan respons (response).
- Algoritma sorting: Quick sort, merge sort, dll., memiliki struktur umum yang sama tetapi berbeda dalam implementasi partisi atau penggabungan.