# Facade Pattern

Facade Pattern adalah sebuah pattern struktural yang menyediakan antarmuka yang terpadu dan sederhana untuk sebuah sistem yang kompleks. Bayangkan Anda memiliki sebuah sistem yang terdiri dari banyak kelas dan metode yang saling berhubungan. Dengan menggunakan Fasad, Anda bisa menyembunyikan kompleksitas tersebut di balik sebuah kelas tunggal, sehingga klien (kode yang menggunakan sistem) hanya perlu berinteraksi dengan kelas Fasad ini.

## Mengapa kita perlu Fasad?

* Sederhana: Menyembunyikan kompleksitas sistem yang besar.
* Mudah digunakan: Menyediakan antarmuka yang mudah dipahami.
* Fleksibel: Memungkinkan perubahan pada sistem internal tanpa mempengaruhi klien.
* Tingkat abstraksi yang lebih tinggi: Memungkinkan klien untuk fokus pada fungsionalitas utama tanpa harus memahami detail implementasi.

## Contoh Penerapan Fasad dalam Python
Misalkan kita memiliki sebuah sistem pemutar musik sederhana yang terdiri dari beberapa kelas:

* Player: Kelas utama yang mengontrol pemutaran musik.
* Amplifier: Mengatur volume.
* CDPlayer: Memutar CD.
* Tuner: Menyetel radio.

``` python
class Amplifier:
    def on(self):
        print("Amplifier on")
    # ...

class CDPlayer:
    def play(self):
        print("CD playing")
    # ...

class Tuner:
    def on(self):
        print("Tuner on")
    # ...

class Player:
    def __init__(self):
        self.amplifier = Amplifier()
        self.cd_player = CDPlayer()
        self.tuner = Tuner()

    def play_cd(self):
        self.amplifier.on()
        self.cd_player.play()
```

Jika klien ingin memutar CD, mereka harus memanggil beberapa metode: menghidupkan amplifier, lalu memutar CD player. Ini bisa menjadi rumit jika sistem semakin kompleks.

## Dengan menggunakan Fasad:
``` python
class HomeTheaterFacade:
    def __init__(self):
        self.player = Player()

    def watch_movie(self):
        print("Get ready to watch a movie...")
        self.player.play_cd()
        # ... (langkah-langkah lainnya)

# Klien hanya perlu memanggil satu metode
home_theater = HomeTheaterFacade()
home_theater.watch_movie()
```
## Penjelasan:

* Kelas HomeTheaterFacade bertindak sebagai fasad untuk sistem pemutar musik.
* Klien hanya perlu memanggil metode watch_movie() untuk menjalankan seluruh rangkaian tindakan.
* Detail implementasi seperti menghidupkan amplifier dan memutar CD player disembunyikan di dalam metode watch_movie().

## Kapan Menggunakan Pola Fasad?
* Sistem yang kompleks: Ketika Anda memiliki sistem yang terdiri dari banyak kelas dan metode yang saling terkait.
* Abstraksi yang lebih tinggi: Ketika Anda ingin menyembunyikan kompleksitas implementasi dari klien.
* Multiple subsystems: Ketika Anda memiliki beberapa subsistem yang berbeda yang perlu dikoordinasikan.
