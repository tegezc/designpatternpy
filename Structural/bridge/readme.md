# Bridge Pattern

Pattern Bridge adalah pola desain yang digunakan untuk memisahkan abstraksi dari implementasinya. Ini berguna ketika kita ingin mengubah implementasi suatu kelas tanpa harus mengubah klien yang menggunakan kelas tersebut.

# Kapan Menggunakan Pattern Bridge?

* Abstraksi dan Implementasi yang Berubah-ubah: Ketika kita memiliki kelas dengan banyak implementasi yang berbeda, dan klien tidak perlu tahu tentang perbedaan-perbedaan tersebut.
* Ketergantungan yang Kompleks: Ketika ada ketergantungan yang rumit antara kelas-kelas, dan kita ingin melonggarkan ketergantungan tersebut.

Contoh Kasus:

Misalkan kita ingin membuat aplikasi yang dapat menggambar berbagai bentuk (lingkaran, persegi, dll.) pada berbagai perangkat (layar, printer). Tanpa menggunakan pattern Bridge, kode kita mungkin akan terlihat seperti ini:

``` python
class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Menggambar lingkaran")

class Square(Shape):
    def draw(self):
        print("Menggambar persegi")

class ScreenDevice:
    def draw_shape(self, shape):
        shape.draw()

# Penggunaan
screen = ScreenDevice()
circle = Circle()
screen.draw_shape(circle)
```
Masalah dengan Kode di Atas:

Jika kita ingin menambahkan perangkat baru (misalnya, proyektor), kita harus mengubah kelas ScreenDevice dan semua kelas bentuk.
Ketergantungan antara kelas Shape dan ScreenDevice sangat erat.
Solusi dengan Pattern Bridge:

``` python
class Renderer:
    def render_circle(self):
        pass

    def render_square(self):
        pass

class VectorRenderer(Renderer):
    def render_circle(self):
        print("Menggambar lingkaran dengan vektor")

    def render_square(self):
        print("Menggambar persegi dengan vektor")

class RasterRenderer(Renderer):
    def render_circle(self):
        print("Menggambar lingkaran dengan raster")

    def render_square(self):
        print("Menggambar persegi dengan raster")

class Shape:
    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        self.renderer.render_circle()

class Square(Shape):
    def draw(self):
        self.renderer.render_square()

# Penggunaan
vector_renderer = VectorRenderer()
raster_renderer = RasterRenderer()

circle = Circle(vector_renderer)
circle.draw()  # Output: Menggambar lingkaran dengan vektor

square = Square(raster_renderer)
square.draw()  # Output: Menggambar persegi dengan raster
```
## Penjelasan:

- Renderer: Kelas abstrak yang mendefinisikan operasi rendering untuk setiap bentuk.
- VectorRenderer, RasterRenderer: Kelas konkret yang mengimplementasikan operasi rendering dengan cara yang berbeda.
- Shape: Kelas abstrak yang memiliki referensi ke objek Renderer.
- Circle, Square: Kelas konkret yang mengimplementasikan metode draw() dengan memanggil metode render_circle() atau render_square() pada objek Renderer.

## Keuntungan:

- Koupeling yang Rendah: Kelas Shape tidak lagi bergantung pada kelas ScreenDevice.
- Ekstensibilitas: Kita dapat menambahkan renderer baru tanpa mengubah kelas Shape atau kelas bentuk lainnya.
- Fleksibelitas: Kita dapat memilih renderer yang berbeda untuk setiap bentuk pada saat runtime.

## Contoh lain

Bayangkan kita sedang membangun sebuah aplikasi pengedit gambar sederhana. Aplikasi ini memungkinkan pengguna untuk menggambar berbagai bentuk (lingkaran, persegi, dll.) dengan berbagai gaya (garis tebal, garis tipis, warna berbeda) pada berbagai perangkat (layar komputer, tablet, ponsel).

Implementasi dengan Pattern Bridge:

``` python
from abc import ABC, abstractmethod

class Renderer(ABC):
    @abstractmethod
    def render_circle(self, radius):
        pass

    @abstractmethod
    def render_square(self, side):
        pass

class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Menggambar lingkaran dengan vektor: radius={radius}")

    def render_square(self, side):
        print(f"Menggambar persegi dengan vektor: sisi={side}")

class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Menggambar lingkaran dengan raster: radius={radius}")

    def render_square(self, side):
        print(f"Menggambar persegi dengan raster: sisi={side}")

class Shape:
    def __init__(self, renderer):
        self.renderer = renderer

    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

class Square(Shape):
    def __init__(self, renderer, side):
        super().__init__(renderer)
        self.side = side

    def draw(self):
        self.renderer.render_square(self.side)

# Penggunaan
vector_renderer = VectorRenderer()
raster_renderer = RasterRenderer()

circle1 = Circle(vector_renderer, 5)
circle1.draw()  # Output: Menggambar lingkaran dengan vektor: radius=5

square1 = Square(raster_renderer, 10)
square1.draw()  # Output: Menggambar persegi dengan raster: sisi=10
```
## Penjelasan Lebih Detail:

- Renderer: Kelas abstrak yang mendefinisikan cara menggambar bentuk dasar (lingkaran, persegi). Setiap metode render_* memiliki parameter tambahan untuk menentukan ukuran atau atribut bentuk.
- VectorRenderer, RasterRenderer: Kelas konkret yang mengimplementasikan cara menggambar bentuk menggunakan vektor atau raster.
- Shape: Kelas abstrak yang bertindak sebagai dasar untuk semua bentuk. Setiap bentuk memiliki referensi ke objek Renderer.
- Circle, Square: Kelas konkret yang mewakili bentuk lingkaran dan persegi. Selain referensi ke Renderer, kelas-kelas ini juga menyimpan informasi spesifik tentang bentuk (radius, sisi).

## Jika contoh di atas tidak menerapkan bridge pattern 

```
class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Menggambar lingkaran")

class Square(Shape):
    def draw(self}
        print("Menggambar persegi")

class ScreenDevice:
    def draw_shape(self, shape):
        shape.draw()

# Penggunaan
screen = ScreenDevice()
circle = Circle()
screen.draw_shape(circle)
```
## Apa yang Terjadi Jika Kita Ingin Menambahkan Proyektor?

1. Membuat Kelas Baru:
Kita perlu membuat kelas baru, misalnya ProjectorDevice, yang memiliki metode draw_shape serupa dengan ScreenDevice.

``` python
class ProjectorDevice:
    def draw_shape(self, shape):
        # Logika untuk menggambar di proyektor
        print("Menggambar di proyektor:")
        shape.draw()
```
2. Mengubah Kelas Shape:
Karena setiap perangkat mungkin memiliki cara yang berbeda untuk menggambar, kita perlu menambahkan logika untuk menangani perbedaan ini di dalam kelas Shape. Misalnya, kita bisa menambahkan parameter device ke metode draw:

``` python
class Shape:
    def draw(self, device):
        if isinstance(device, ScreenDevice):
            # Logika menggambar di layar
        elif isinstance(device, ProjectorDevice):
            # Logika menggambar di proyektor
```

3. Memperbarui Penggunaan:
Kita perlu mengubah cara kita membuat objek dan memanggil metode draw_shape:

``` python
projector = ProjectorDevice()
circle = Circle()
projector.draw_shape(circle)
```
## Masalah yang Muncul:

- Kode Menjadi Kompleks: Kelas Shape menjadi semakin besar dan kompleks karena harus menangani berbagai jenis perangkat.
- Ketergantungan yang Tinggi: Setiap perubahan pada perangkat (misalnya, menambahkan fitur baru) akan berdampak pada kelas Shape dan semua kelas bentuk turunannya.
- Sulit Diperluas: Menambahkan perangkat baru akan selalu membutuhkan modifikasi pada kelas Shape.
- Kurang Fleksibel: Jika kita ingin menggunakan perangkat yang sama dengan cara yang berbeda (misalnya, menggambar dengan warna yang berbeda), kita harus menambahkan parameter tambahan ke metode draw.
