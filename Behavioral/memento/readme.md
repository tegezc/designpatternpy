# Memento Pattern

Pattern Memento adalah sebuah teknik dalam desain perangkat lunak yang memungkinkan kita untuk menyimpan keadaan (state) suatu objek pada suatu titik waktu tertentu, sehingga kita dapat mengembalikan objek tersebut ke keadaan sebelumnya. Bayangkan seperti membuat snapshot dari suatu objek. Pattern ini sangat berguna untuk fitur undo/redo, menyimpan versi dokumen, atau memulihkan sistem ke konfigurasi sebelumnya.

## Komponen Utama:

- Originator: Objek yang memiliki state yang ingin disimpan.
- Memento: Objek yang menyimpan snapshot dari state Originator. Memento biasanya bersifat immutable, artinya tidak dapat diubah setelah dibuat.
- Caretaker: Objek yang menyimpan dan mengembalikan Memento.

## Contoh Implementasi dalam Python
Mari kita ambil contoh sederhana: sebuah text editor. Kita ingin menambahkan fitur undo/redo untuk teks yang sedang diedit.

```
class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

class Editor:
    def __init__(self):
        self._state = ""
        self._history = []

    def set_content(self, content):
        self._state = content
        self.save_to_history()

    def restore(self, memento):
        self._state = memento.get_state()

    def save_to_history(self):
        self._history.append(Memento(self._state))

    def undo(self):
        if not self._history:
            return
        self._history.pop()
        if self._history:
            self.restore(self._history[-1])
        else:
            self._state = ""

# Penggunaan
editor = Editor()
editor.set_content("Hello, world!")
editor.set_content("This is a new content.")

editor.undo()  # Mengembalikan ke "Hello, world!"
print(editor._state)
```
## Penjelasan:

- Kelas Memento: Menyimpan state dari editor (teks yang sedang diedit).
- Kelas Editor:
    - set_content: Mengubah konten editor dan menyimpan state ke dalam history.
    - restore: Mengembalikan editor ke state yang disimpan dalam memento.
    - save_to_history: Menyimpan state saat ini ke dalam history.
    - undo: Memulihkan state sebelumnya dari history.

1. Originator:
- Editor adalah originator dalam contoh ini.
- Editor memiliki state internal (yaitu, konten teks) yang ingin disimpan dan dipulihkan.
- Editor bertanggung jawab untuk membuat dan mengembalikan memento, serta memulihkan state dari memento.

2. Caretaker:
- Editor juga berperan sebagai caretaker dalam contoh ini.
- Editor menyimpan memento dalam list _history.
- Editor bertanggung jawab untuk mengelola memento, seperti menambahkan memento baru ke dalam history dan menghapus memento lama.

3. Memento:
- Memento adalah kelas yang merepresentasikan snapshot dari state editor pada suatu titik waktu tertentu.
- Memento menyimpan state sebagai atribut _state dan tidak menyediakan cara untuk memodifikasi state secara langsung.

## Mengapa Editor menjadi kedua-duanya?

Dalam contoh yang sederhana ini, Editor mengambil peran ganda sebagai originator dan caretaker. Ini memungkinkan Editor untuk mengelola state-nya sendiri dan menyimpan history perubahan. Namun, dalam implementasi yang lebih kompleks, kita bisa memisahkan tanggung jawab ini menjadi kelas yang berbeda. Misalnya, kita bisa membuat kelas HistoryManager sebagai caretaker yang terpisah untuk mengelola memento.

## Penting untuk diingat:

- Memento dirancang untuk menjadi immutable (tidak dapat diubah setelah dibuat). Ini memastikan bahwa state yang disimpan tidak akan terkontaminasi oleh perubahan di luar memento.
- Caretaker tidak perlu tahu detail tentang struktur internal memento. Caretaker hanya perlu tahu cara menyimpan dan mengambil memento.

## Kapan Menggunakan Pattern Memento?
- Saat Anda ingin menyimpan snapshot dari status objek untuk digunakan nanti.
- Fitur undo/redo: Memungkinkan pengguna untuk membatalkan perubahan yang telah dilakukan.
- Simulasi: Untuk menyimpan state sistem pada titik waktu tertentu sehingga dapat diulang kembali.
- Game: Untuk menyimpan progress permainan sehingga pemain dapat melanjutkan dari titik sebelumnya.
- Konfigurasi sistem: Untuk menyimpan konfigurasi sebelumnya sehingga dapat dipulihkan jika terjadi kesalahan.
- Versi kontrol: Untuk menyimpan berbagai versi dari suatu dokumen atau proyek.

## Kelebihan Pattern Memento:
- Memisahkan tanggung jawab antara originator, memento, dan caretaker.
- Memungkinkan untuk menyimpan banyak state tanpa mempengaruhi objek asli.
- Fleksibel untuk berbagai macam penggunaan.

## Kekurangan Pattern Memento:
- Membutuhkan memori tambahan untuk menyimpan memento.
- Implementasi bisa menjadi kompleks jika ada banyak state yang perlu disimpan.

## Contoh lain menggunakan Java: 
``` Java
// 1. Memento class
class Memento {
    private final String state;

    public Memento(String state) {
        this.state = state;
    }

    public String getState() {
        return state;
    }
}

// 2. Originator class
class Originator {
    private String state;

    public void setState(String state) {
        this.state = state;
        System.out.println("State is set to: " + state);
    }

    public String getState() {
        return state;
    }

    public Memento saveStateToMemento() {
        return new Memento(state);
    }

    public void getStateFromMemento(Memento memento) {
        state = memento.getState();
        System.out.println("State restored to: " + state);
    }
}

// 3. Caretaker class
class Caretaker {
    private List<Memento> mementoList = new ArrayList<>();

    public void add(Memento state) {
        mementoList.add(state);
    }

    public Memento get(int index) {
        return mementoList.get(index);
    }
}

// 4. Client code (Main)
public class MementoPatternDemo {
    public static void main(String[] args) {
        Originator originator = new Originator();
        Caretaker caretaker = new Caretaker();

        // Changing state and saving to memento
        originator.setState("State #1");
        caretaker.add(originator.saveStateToMemento());

        originator.setState("State #2");
        caretaker.add(originator.saveStateToMemento());

        originator.setState("State #3");
        caretaker.add(originator.saveStateToMemento());

        originator.setState("State #4");
        System.out.println("Current State: " + originator.getState());

        // Restoring states from memento
        originator.getStateFromMemento(caretaker.get(0));
        originator.getStateFromMemento(caretaker.get(1));
    }
}
```

``` Output
State is set to: State #1
State is set to: State #2
State is set to: State #3
State is set to: State #4
Current State: State #4
State restored to: State #1
State restored to: State #2
```
## Penjelasan Kode:
1. Class Memento:
Memento hanya menyimpan satu properti, yaitu state dari objek Originator. Ia tidak menyediakan setter untuk menjaga agar status tetap immutable.

2. Class Originator:
- Originator adalah objek yang statusnya ingin kita simpan. Ia memiliki metode saveStateToMemento() untuk menyimpan state saat ini ke dalam memento, dan metode getStateFromMemento() untuk mengembalikan state dari memento.
- Metode setState() digunakan untuk mengubah state dan mencetak state saat ini.

3. Class Caretaker:
Caretaker mengelola memento yang disimpan. Dalam implementasi ini, ia menggunakan List<Memento> untuk menyimpan beberapa memento, yang kemudian dapat digunakan untuk mengembalikan state sebelumnya.

4. Client Code (Main):
Di bagian ini, kita mengubah beberapa kali state dari objek Originator dan menyimpannya di Caretaker. Kemudian, kita menggunakan memento untuk mengembalikan state sebelumnya.