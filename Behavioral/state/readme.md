# State Pattern

State Pattern adalah salah satu design pattern dalam pemrograman yang memungkinkan suatu objek mengubah perilakunya saat state internalnya berubah. Sederhananya, sebuah objek dapat memiliki berbagai keadaan (state), dan setiap keadaan memiliki perilaku yang berbeda.

## Kapan kita perlu menggunakan State Pattern?

- Ketika sebuah objek memiliki banyak keadaan yang berbeda dan perilaku yang terkait dengan masing-masing keadaan tersebut.
- Ketika kondisi suatu objek dapat berubah secara dinamis dan mempengaruhi bagaimana objek tersebut merespons peristiwa.
- Ketika kita ingin menghindari penggunaan banyak conditional statements (if-else) untuk mengelola berbagai keadaan.

## Contoh Implementasi dalam Python: Mesin Cuci

Mari kita ambil contoh sederhana sebuah mesin cuci. Mesin cuci memiliki beberapa state, seperti:

- OFF: Mesin mati
- FILLING: Mesin mengisi air
- WASHING: Mesin sedang mencuci
- RINSING: Mesin membilas
- SPINNING: Mesin memutar untuk mengeringkan

Setiap state memiliki perilaku yang berbeda, misalnya saat state adalah "FILLING", maka mesin akan mengisi air, dan jika state adalah "WASHING", mesin akan mulai memutar drum.

``` python
class Context:
    def __init__(self):
        self._state = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state
        self._state.context = self

    def request(self):
        self._state.handle()

class State:
    def __init__(self, context):
        self._context = context

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context):
        self._context = context

    def handle(self):
        pass

class OffState(State):
    def handle(self):
        print("Mesin dimatikan")
        # Logic untuk mematikan mesin

class FillingState(State):
    def handle(self):
        print("Mesin mengisi air")
        # Logic untuk mengisi air
        # Jika air sudah penuh, ubah state ke WashingState

class WashingState(State):
    def handle(self):
        print("Mesin sedang mencuci")
        # Logic untuk mencuci
        # Setelah selesai mencuci, ubah state ke RinsingState

# ... dan seterusnya untuk state lainnya (RinsingState, SpinningState)

# Contoh penggunaan
context = Context()
context.state = OffState(context)

context.request()  # Output: Mesin dimatikan

context.state = FillingState(context)
context.request()  # Output: Mesin mengisi air

# ... dan seterusnya
```
## Penjelasan Kode:

- Context: Kelas ini merepresentasikan mesin cuci itu sendiri. Ia memiliki atribut state yang menyimpan state saat ini.
- State: Kelas abstrak ini adalah kelas dasar untuk semua state. Setiap state memiliki method handle() yang akan dipanggil ketika state tersebut aktif.
- OffState, FillingState, WashingState, ...: Kelas-kelas ini adalah turunan dari kelas State dan merepresentasikan masing-masing state.

## Kelebihan State Pattern:

- Kode lebih terstruktur: Setiap state memiliki tanggung jawabnya sendiri.
- Mudah untuk menambahkan state baru: Tinggal buat kelas turunan dari State.
- Meningkatkan fleksibilitas: Perilaku objek dapat berubah secara dinamis berdasarkan state-nya.