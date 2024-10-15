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
