from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

class OperationAdd(Strategy):
    def execute(self, a, b):
        return a + b

class OperationSubtract(Strategy):
    def execute(self, a, b):
        return a - b

class OperationMultiply(Strategy):
    def execute(self, a, b):
        return a * b

class OperationDivide(Strategy):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def execute_strategy(self, a, b):
        return self._strategy.execute(a, b)

# Contoh penggunaan
context = Context(OperationAdd())
print(context.execute_strategy(2, 3))  # Output: 5

context = Context(OperationMultiply())
print(context.execute_strategy(2, 3))  # Output: 6
