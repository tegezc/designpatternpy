# Chain Of Responsibility

Chain of Responsibility adalah pattern yang memungkinkan kita menghubungkan beberapa objek secara berurutan. Setiap objek dalam rantai ini memiliki kesempatan untuk menangani permintaan. Jika sebuah objek tidak dapat menangani permintaan tersebut, maka permintaan tersebut akan diteruskan ke objek berikutnya dalam rantai.

## Contoh Praktis: Persetujuan Dokumen

Bayangkan sebuah proses persetujuan dokumen di sebuah perusahaan. Dokumen harus melalui beberapa tahap persetujuan, seperti:

1. Manajer Langsung: Memeriksa apakah dokumen sudah lengkap dan benar secara teknis.
2. Kepala Departemen: Memeriksa apakah dokumen sesuai dengan kebijakan departemen.
3. Direktur: Memeriksa dampak finansial dari dokumen tersebut.
Setiap tahap memiliki tanggung jawab yang berbeda. Jika seorang manajer langsung menyetujui dokumen, maka proses selesai. Jika tidak, dokumen akan diteruskan ke kepala departemen, dan seterusnya.

``` python
class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle_request(self, request):
        if self._successor is not None:
            self._successor.handle_request(request)

class Manager(Handler):
    def handle_request(self, request):
        if request.is_complete():
            print("Dokumen disetujui oleh manajer.")
        else:
            print("Dokumen belum lengkap. Diteruskan ke atasan.")
            super().handle_request(request)

class DepartmentHead(Handler):
    def handle_request(self, request):
        if request.is_compliant():
            print("Dokumen sesuai dengan kebijakan departemen. Diteruskan ke direktur.")
            super().handle_request(request)
        else:
            print("Dokumen tidak sesuai dengan kebijakan departemen.")

class Director(Handler):
    def handle_request(self, request):
        if request.is_financially_sound():
            print("Dokumen disetujui oleh direktur.")
        else:
            print("Dokumen tidak disetujui karena alasan finansial.")

# Contoh penggunaan
request = DocumentRequest()  # Simulasi dokumen yang akan diajukan
manager = Manager()
department_head = DepartmentHead(manager)
director = Director(department_head)

director.handle_request(request)
```
## Penjelasan Kode:

- Kelas Handler: Kelas dasar yang mendefinisikan metode handle_request. Setiap handler memiliki successor untuk meneruskan permintaan jika tidak dapat diproses.
- Kelas Manager, DepartmentHead, dan Director: Turunan dari kelas Handler, masing-masing memiliki logika penanganan permintaan yang berbeda.
- Contoh Penggunaan:
    - Dibuat objek request untuk merepresentasikan dokumen yang akan diajukan.
    - Dibuat objek manager, department_head, dan director, dan dihubungkan membentuk rantai.
    - Permintaan diajukan ke director. Permintaan akan diteruskan ke handler berikutnya hingga ada yang dapat memprosesnya atau sampai akhir rantai.

## Keuntungan Chain of Responsibility:

- Fleksibel: Mudah menambahkan atau menghapus handler tanpa mengubah struktur keseluruhan.
- Terbuka: Setiap handler dapat membuat keputusan berdasarkan kriteria yang berbeda.
- Tanggung Jawab yang Terpisah: Setiap handler fokus pada tugasnya masing-masing.

## Kapan Menggunakan Chain of Responsibility?

- Ketika terdapat beberapa objek yang dapat menangani permintaan, tetapi tidak diketahui sebelumnya objek mana yang akan memprosesnya.
- Ketika ingin membuat sistem yang fleksibel dan mudah diperluas.
- Ketika ingin memisahkan tanggung jawab antara objek-objek dalam sistem.

## Penting:

- DocumentRequest adalah kelas yang merepresentasikan dokumen yang akan diajukan. Kelas ini harus memiliki metode - untuk memeriksa kelengkapan, kepatuhan terhadap kebijakan, dan dampak finansial.
Anda dapat menambahkan lebih banyak jenis handler dan kriteria untuk menyesuaikan dengan kebutuhan aplikasi Anda.


## Contoh lain dengan Java

Bayangkan sebuah sistem pemrosesan pembayaran. Setiap transaksi harus melalui beberapa tahap verifikasi, seperti:

1. Verifikasi Saldo: Memastikan saldo cukup.
2. Verifikasi Limit: Memastikan transaksi tidak melebihi limit kartu.
3. Verifikasi Keamanan: Memastikan transaksi aman dari kecurangan.

``` Java
interface PaymentHandler {
    void setNextHandler(PaymentHandler handler);
    boolean handlePayment(Payment payment);
}

class BalanceVerificationHandler implements PaymentHandler {
    private PaymentHandler nextHandler;

    @Override
    public void setNextHandler(PaymentHandler handler) {
        this.nextHandler = handler;
    }

    @Override
    public boolean handlePayment(Payment payment) {
        if (payment.getAmount() > payment.getAccount().getBalance()) {
            System.out.println("Saldo tidak cukup.");
            return false;
        }
        return nextHandler != null && nextHandler.handlePayment(payment);
    }
}

class LimitVerificationHandler implements PaymentHandler {
    // ... (Implementasi serupa dengan BalanceVerificationHandler)
}

class SecurityVerificationHandler implements PaymentHandler {
    // ... (Implementasi serupa dengan BalanceVerificationHandler)
}

class Payment {
    private double amount;
    private Account account;
    // ... (atribut lainnya)

    // ... (konstruktor dan getter/setter)
}

class Account {
    private double balance;
    private double limit;
    // ... (atribut lainnya)

    // ... (konstruktor dan getter/setter)
}

public class ChainOfResponsibilityExample {
    public static void main(String[] args) {
        PaymentHandler balanceHandler = new BalanceVerificationHandler();
        PaymentHandler limitHandler = new LimitVerificationHandler();
        PaymentHandler securityHandler = new SecurityVerificationHandler();

        balanceHandler.setNextHandler(limitHandler);
        limitHandler.setNextHandler(securityHandler);

        Payment payment = new Payment(1000);
        Account account = new Account(500, 1500);
        payment.setAccount(account);

        if (balanceHandler.handlePayment(payment)) {
            System.out.println("Pembayaran berhasil.");
        } else {
            System.out.println("Pembayaran gagal.");
        }
    }
}
```
## Penjelasan:

1. Interface PaymentHandler: Mendefinisikan dua metode: setNextHandler untuk menghubungkan handler berikutnya dan handlePayment untuk memproses pembayaran.
2. ConcreteHandler: Masing-masing handler (BalanceVerificationHandler, LimitVerificationHandler, SecurityVerificationHandler) melakukan verifikasi spesifik. Jika verifikasi gagal, metode handlePayment mengembalikan false dan berhenti proses. Jika berhasil, permintaan diteruskan ke handler berikutnya.
3. Payment dan Account: Kelas untuk mewakili data pembayaran dan akun.
4. Main Method: Membuat objek handler, menghubungkannya dalam rantai, dan membuat objek pembayaran untuk diproses.

## Konsep Penting:

- Short-circuiting: Jika salah satu handler mengembalikan false, proses akan berhenti dan tidak perlu mengecek handler selanjutnya.
- Responsibility: Setiap handler bertanggung jawab atas satu aspek verifikasi.
- Flexibility: Mudah menambahkan atau menghapus handler untuk menambahkan jenis verifikasi baru.

## note
short-circuiting bukanlah syarat untuk pattern ini, ini hanyalah logika bisnis sesuai kebutuhan, jadi bisa saja rantai eksekusi tetap di jalankan meskipun salah satu tahap ada kegagalan (tergantung proses bisnis)