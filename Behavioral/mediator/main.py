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
