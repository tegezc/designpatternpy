# Observer Pattern

Design Pattern Observer adalah pattern perilaku yang mendefinisikan hubungan satu-ke-banyak di antara objek sehingga ketika satu objek mengubah statusnya, semua objek dependen diberitahu dan diperbarui secara otomatis. Sederhananya, ini seperti sebuah sistem berlangganan, di mana beberapa objek "berlangganan" pada objek lain untuk mendapatkan notifikasi ketika terjadi perubahan.

## Contoh Praktis: Aplikasi Cuaca

Bayangkan sebuah aplikasi cuaca. Ada kelas WeatherData yang menyimpan data cuaca (suhu, kelembaban, tekanan udara), dan beberapa kelas lain seperti CurrentConditionsDisplay, StatisticsDisplay, dan ForecastDisplay yang menampilkan data cuaca dalam format yang berbeda. Ketika data cuaca berubah, semua tampilan ini harus diperbarui secara otomatis.

``` python
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

class Observer:
    def update(self, subject):
        pass

class WeatherData(Subject):
    def __init__(self):
        super().__init__()
        self._temperature = None
        self._humidity = None
        self._pressure = None

    def measurements_changed(self):
        self.notify()

    def set_measurements(self, temperature, humidity, pressure):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.measurements_changed()

class CurrentConditionsDisplay(Observer):
    def __init__(self, weather_data):
        self._weather_data = weather_data
        weather_data.attach(self)

    def update(self, subject):
        if isinstance(subject, WeatherData):
            self._temperature = subject._temperature
            self._humidity = subject._humidity
            self.display()

    def display(self):
        print("Current conditions: ", self._temperature, "F degrees and ", self._humidity, "% humidity")

# Contoh penggunaan
weather_data = WeatherData()
current_display = CurrentConditionsDisplay(weather_data)

# Simulasi perubahan data cuaca
weather_data.set_measurements(80, 65, 30.4)
```
## Penjelasan Kode:

- Subject: Kelas abstrak yang merepresentasikan objek yang dapat diobservasi. Memiliki metode untuk menambahkan, menghapus, dan memberitahu observer.
- Observer: Kelas abstrak yang merepresentasikan objek yang mengamati perubahan pada subject.
- WeatherData: Kelas konkrit yang mewarisi dari Subject. Menyimpan data cuaca dan memiliki metode untuk memberitahu observer ketika data berubah.
- CurrentConditionsDisplay: Kelas konkrit yang mewarisi dari Observer. Menampilkan kondisi cuaca saat ini.

## Cara Kerja:

1. WeatherData menyimpan daftar observer.
2. Ketika data cuaca berubah, WeatherData memanggil metode notify() untuk memberitahu semua observer.
3. Setiap observer (misalnya CurrentConditionsDisplay) akan memanggil metode update() dan memperbarui tampilannya sesuai dengan data terbaru.

## Keuntungan Pola Observer:

- Dekoupling: Mengurangi ketergantungan antara objek, membuat kode lebih modular dan mudah diuji.
- Fleksibelitas: Mudah menambahkan atau menghapus observer tanpa mengubah kode inti.
- Efisiensi: Observer hanya diinformasikan ketika ada perubahan yang relevan.

## Contoh Penggunaan Lain:

- GUI: Mengupdate tampilan ketika data berubah.
- Event-driven programming: Menangani event dari berbagai sumber.
- Sistem notifikasi: Mengirim notifikasi ketika terjadi peristiwa tertentu.

## Perbedaan Observer dan Mediator

## Perbedaan Utama:

- Fokus Komunikasi:

    - Observer: Fokus pada hubungan satu-ke-banyak. Satu objek (Subject) memberitahu banyak objek (Observer) tentang perubahan statusnya.
    - Mediator: Fokus pada komunikasi yang lebih kompleks antara banyak objek. Mediator bertindak sebagai perantara, mengkoordinasikan komunikasi antara semua objek.


- Tingkat Keterlibatan:

    - Observer: Observer hanya bereaksi terhadap perubahan pada Subject.
    - Mediator: Mediator memiliki peran yang lebih aktif, bisa memulai komunikasi, dan bahkan mengubah perilaku objek lain.


### Kapan Menggunakan Masing-Masing:

- Observer:
    - Cocok untuk situasi di mana ada objek pusat yang sering berubah dan perlu memberitahu banyak objek lain.
    - Contoh: Aplikasi cuaca, event handling di GUI.

- Mediator:
    - Cocok untuk situasi di mana banyak objek saling berinteraksi dan komunikasi antar mereka kompleks.
    - Contoh: Aplikasi chat dengan banyak fitur (private message, group chat, file sharing), sistem kontrol lalu lintas.

### Contoh Sederhana untuk Membedakan:

- Observer: Sebuah tombol (Subject) memberitahu semua label (Observer) untuk memperbarui tampilan ketika tombol ditekan.
- Mediator: Dalam sebuah aplikasi chat, Mediator mengelola semua percakapan antara pengguna, termasuk mengirim pesan, menambahkan pengguna, dan mengelola grup.


### Kesimpulan:

- Observer lebih sederhana dan cocok untuk hubungan satu-ke-banyak yang relatif sederhana.
- Mediator lebih fleksibel dan cocok untuk sistem yang kompleks dengan banyak interaksi antar objek.


### Pilihan Antara Keduanya:

Pilihan antara Observer dan Mediator tergantung pada kompleksitas sistem dan kebutuhan spesifik. Jika hubungan antar objek relatif sederhana dan satu-ke-banyak, Observer mungkin lebih cocok. Namun, jika komunikasi antar objek lebih kompleks dan membutuhkan koordinasi yang lebih baik, Mediator adalah pilihan yang lebih baik.