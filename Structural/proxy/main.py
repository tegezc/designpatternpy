class Image:
    def __init__(self, filename):
        self.filename = filename
        self._load_image()

    def _load_image(self):
        # Simulasi proses loading image yang memakan waktu
        print("Loading image...")
        # ... kode untuk load image

    def display(self):
        print(f"Displaying {self.filename}")

class ProxyImage:
    def __init__(self, filename):
        self.filename = filename
        self.image = None

    def display(self):
        if self.image is None:
            self.image = Image(self.filename)
        self.image.display()

#pemangilan
image = ProxyImage("myimage.jpg")
image.display()  # Image akan di-load dan ditampilkan
image.display()  # Image yang sudah ada akan langsung ditampilkan
