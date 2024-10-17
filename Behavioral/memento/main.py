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
