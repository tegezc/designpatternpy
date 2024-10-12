class Coffee:
    def make_coffee(self):
        self.boil_water()
        self.brew_coffee_with_water()
        self.pour_in_cup()
        self.add_suger()
        self.add_milk()

    def boil_water(self):
        print("Rebus air")

    def brew_coffee_with_water(self):
        print("Seduh kopi dengan air")

    def pour_in_cup(self):
        print("Tuang ke dalam cangkir")

    def add_suger(self):
        pass

    def add_milk(self):
        pass

class BlackCoffee(Coffee):
    pass  # Tidak ada penambahan gula atau susu

class Latte(Coffee):
    def add_milk(self):
        print("Tambahkan susu")

class Cappuccino(Latte):
    def add_milk(self):
        print("Tambahkan busa susu")

# Penggunaan
black_coffee = BlackCoffee()
black_coffee.make_coffee()

latte = Latte()
latte.make_coffee()

cappuccino = Cappuccino()
cappuccino.make_coffee()
