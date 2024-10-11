class Tree:
    def __init__(self, x, y, jenis):
        self.x = x
        self.y = y
        self.jenis = jenis

    def draw(self):
        # Logika untuk menggambar pohon berdasarkan jenisnya
        print(f"Menggambar pohon {self.jenis} di ({self.x}, {self.y})")

# Flyweight factory
class TreeFactory:
    _tree_types = {}

    def get_tree(self, jenis):
        tree_type = self._tree_types.get(jenis)
        if not tree_type:
            tree_type = TreeType(jenis)
            self._tree_types[jenis] = tree_type
        return Tree(0, 0, tree_type)

class TreeType:
    def __init__(self, jenis):
        self.jenis = jenis

# Penggunaan
tree_factory = TreeFactory()

# Membuat banyak pohon pinus
for i in range(100):
    tree = tree_factory.get_tree("pinus")
    tree.x = i * 10
    tree.y = i
    tree.draw()
