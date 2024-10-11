class Component:
    def __init__(self, name):
        self.name = name

    def operation(self):
        pass

class File(Component):
    def operation(self):
        print(f"Displaying file: {self.name}")

class Folder(Component):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def operation(self):
        print(f"Displaying folder: {self.name}")
        for child in self.children:
            child.operation()

#Pemanggilan

# Membuat objek
folder1 = Folder("Documents")
file1 = File("report.txt")
file2 = File("presentation.pptx")
folder2 = Folder("Pictures")
image1 = File("photo1.jpg")

# Membangun struktur
folder1.add_child(file1)
folder1.add_child(file2)
folder1.add_child(folder2)
folder2.add_child(image1)

# Menampilkan struktur
folder1.operation()
