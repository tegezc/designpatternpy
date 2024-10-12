# Mediator Pattern

Mediator adalah pola desain perilaku yang bertujuan mengurangi ketergantungan langsung antara objek-objek dalam suatu sistem. Dengan kata lain, alih-alih objek-objek berkomunikasi langsung satu sama lain, mereka akan berkomunikasi melalui objek mediator. Hal ini membuat sistem menjadi lebih fleksibel dan mudah diubah.

## Contoh Kasus:

Bayangkan sebuah aplikasi chat sederhana dengan beberapa pengguna. Setiap pengguna dapat mengirim dan menerima pesan. Tanpa mediator, setiap pengguna harus mengetahui dan menyimpan referensi ke semua pengguna lainnya untuk bisa saling mengirim pesan. Ini akan membuat kode menjadi kompleks dan sulit dipelihara.

Implementasi dalam Python:
``` python
class User:
    def __init__(self, name):
        self.name = name
        self.chatroom = None

    def send(self, message):
        self.chatroom.send(message, self)

    def receive(self, message):
        print(f"{self.name}: {message}")

class Chatroom:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.name] = user
        user.chatroom = self

    def send(self, message, user):
        for u in self.users.values():
            if u != user:
                u.receive(message)

# Contoh penggunaan
user1 = User("Alice")
user2 = User("Bob")
chatroom = Chatroom()

chatroom.add_user(user1)
chatroom.add_user(user2)

user1.send("Hello, Bob!")
user2.send("Hi, Alice!")
```
## Penjelasan:

- Kelas User:
    - Setiap pengguna memiliki nama dan referensi ke chatroom.
    - Metode send digunakan untuk mengirim pesan ke chatroom.
    - Metode receive digunakan untuk menerima pesan.
- Kelas Chatroom:
    - Chatroom menyimpan daftar pengguna.
    - Metode add_user digunakan untuk menambahkan pengguna ke chatroom.
    - Metode send digunakan untuk mengirim pesan ke semua pengguna kecuali pengirim.

## Keuntungan Menggunakan Mediator Pattern:

- Decoupling: Objek-objek tidak perlu tahu tentang implementasi internal objek lain.
- Fleksibelitas: Mudah menambahkan atau menghapus pengguna tanpa mengubah kode yang sudah ada.
- Kemudahan Pemeliharaan: Kode menjadi lebih terstruktur dan mudah dipahami.

## Kekurangan Menggunakan Pola Mediator:
- Over Engineering: Jika digunakan secara berlebihan, Mediator dapat membuat desain menjadi terlalu kompleks dan sulit dipahami.
- Single Point of Failure: Jika terjadi kesalahan pada Mediator, seluruh sistem dapat terpengaruh.

## Kapan Menggunakan Mediator Pattern:

- Ketika banyak objek saling berinteraksi dalam sistem yang kompleks.
- Ketika mengubah satu objek berdampak pada banyak objek lainnya.
- Ketika ingin membuat sistem lebih fleksibel dan mudah diubah.
