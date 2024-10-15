# Strategy Pattern

Strategy Pattern adalah salah satu pola desain dalam pemrograman yang memungkinkan kita untuk mengganti algoritma pada saat runtime. Dengan kata lain, kita bisa mengubah perilaku suatu objek tanpa mengubah struktur kelasnya. Ini sangat berguna ketika kita memiliki beberapa cara berbeda untuk menyelesaikan suatu masalah, dan kita ingin memilih cara yang tepat pada saat eksekusi program.

## Contoh Sederhana:

Misalkan kita ingin membuat aplikasi kalkulator sederhana. Kita bisa memiliki beberapa operasi seperti penjumlahan, pengurangan, perkalian, dan pembagian. Dengan Strategy Pattern, kita bisa membuat setiap operasi sebagai sebuah strategi (strategy) yang terpisah.

## Implementasi dalam Python:

``` python
from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

class OperationAdd(Strategy):
    def execute(self, a, b):
        return a + b

class OperationSubtract(Strategy):
    def execute(self, a, b):
        return a - b

class OperationMultiply(Strategy):
    def execute(self, a, b):
        return a * b

class OperationDivide(Strategy):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def execute_strategy(self, a, b):
        return self._strategy.execute(a, b)

# Contoh penggunaan
context = Context(OperationAdd())
print(context.execute_strategy(2, 3))  # Output: 5

context = Context(OperationMultiply())
print(context.execute_strategy(2, 3))  # Output: 6
```
## Penjelasan:

1. Interface Strategy: Kita definisikan sebuah interface Strategy dengan metode abstrak execute. Ini akan menjadi kontrak untuk semua kelas strategi.
2. Kelas-kelas Strategi: Setiap operasi (penjumlahan, pengurangan, dll.) diimplementasikan sebagai kelas yang mewarisi dari Strategy dan mengimplementasikan metode execute.
3. Kelas Context: Kelas Context menyimpan referensi ke objek strategi yang sedang digunakan. Metode execute_strategy akan memanggil metode execute dari objek strategi tersebut.

## Keuntungan Menggunakan Strategy Pattern:

- Keterbukaan untuk ekstensi: Mudah menambahkan strategi baru tanpa mengubah struktur kelas yang ada.
- Ketergantungan yang rendah: Kelas Context tidak terlalu bergantung pada implementasi konkret dari strategi.
- Meningkatkan kemampuan pengujian: Setiap strategi dapat diuji secara independen.


## Kapan Menggunakan Strategy Pattern?

- Ketika kamu memiliki algoritma yang berbeda untuk menyelesaikan suatu masalah, dan kamu ingin memilih algoritma yang tepat pada saat runtime.
- Ketika kamu ingin membuat kode yang lebih fleksibel dan mudah diuji.
- Ketika kamu ingin menghindari conditional statements yang rumit untuk memilih algoritma.

## Contoh Penggunaan Lain:

- Algoritma sorting: Quick sort, merge sort, bubble sort, dll.
- Algoritma pencarian: Binary search, linear search, dll.
- Rendering grafis: Algoritma rendering yang berbeda untuk platform yang berbeda.

## Kesimpulan

Strategy Pattern adalah alat yang sangat berguna dalam pemrograman berorientasi objek. Dengan memahami pola ini, kamu dapat menulis kode yang lebih modular, fleksibel, dan mudah dipelihara.

## Contoh Lain :  Sistem Pembayaran
Bayangkan kita sedang membangun sebuah sistem e-commerce. Sistem ini harus mendukung berbagai metode pembayaran seperti kartu kredit, transfer bank, atau pembayaran digital. Setiap metode pembayaran memiliki alur dan logika yang berbeda. Dengan menggunakan Strategy Pattern, kita bisa membuat sistem pembayaran yang fleksibel dan mudah diperluas.

``` python
from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardStrategy(PaymentStrategy):
    def pay(self, amount):
        print(f"Membayar {amount} menggunakan kartu kredit")
        # Logika pembayaran kartu kredit (misalnya, validasi kartu, otorisasi, dll.)

class BankTransferStrategy(PaymentStrategy):
    def pay(self, amount):
        print(f"Membayar {amount} melalui transfer bank")
        # Logika pembayaran transfer bank (misalnya, generate nomor rekening, instruksi transfer)

class DigitalPaymentStrategy(PaymentStrategy):
    def pay(self, amount):
        print(f"Membayar {amount} menggunakan pembayaran digital")
        # Logika pembayaran digital (misalnya, integrasi dengan gateway pembayaran)

class Order:
    def __init__(self, amount, strategy):
        self._amount = amount
        self._strategy = strategy

    def checkout(self):
        self._strategy.pay(self._amount)

# Contoh penggunaan
order1 = Order(100000, CreditCardStrategy())
order1.checkout()

order2 = Order(50000, BankTransferStrategy())
order2.checkout()
```
## Penjelasan:

- Interface PaymentStrategy: Mendefinisikan metode pay yang harus diimplementasikan oleh semua strategi pembayaran.
- Kelas-kelas Strategi: Setiap metode pembayaran (kartu kredit, transfer bank, pembayaran digital) memiliki kelas strategi sendiri yang mengimplementasikan metode pay dengan logika spesifik.
- Kelas Order: Kelas Order menyimpan informasi tentang jumlah pembayaran dan strategi pembayaran yang digunakan. Metode checkout akan memanggil metode pay dari strategi yang dipilih.


## Keuntungan dalam Contoh ini:

- Fleksibel: Mudah menambahkan metode pembayaran baru tanpa mengubah struktur kelas Order.
- Teruji: Setiap strategi pembayaran dapat diuji secara independen.
- Terkelola: Logika pembayaran dipisahkan ke dalam kelas-kelas yang berbeda, sehingga lebih mudah dikelola dan diubah.

## Contoh Lain yang Mungkin:

- Algoritma routing: Memilih rute terbaik berdasarkan kondisi lalu lintas, jarak, dll.
- Logika autentikasi: Menggunakan berbagai metode autentikasi seperti password, OTP, biometrik, dll.
- Format laporan: Menghasilkan laporan dalam berbagai format seperti PDF, Excel, HTML, dll.

## Konsep Penting Lain:

- Open-Closed Principle: Kelas harus terbuka untuk ekstensi (menambahkan strategi baru), tetapi tertutup untuk modifikasi (tidak mengubah kelas yang sudah ada).
- Dependency Injection: Menyuntikkan strategi ke dalam kelas Order pada saat pembuatan objek, sehingga memungkinkan fleksibilitas dalam memilih strategi.