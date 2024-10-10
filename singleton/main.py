"""
Implementasi singleton :
1. Menggunakan metode metaclass
2. Menggunakan fungsi dekorator
3. Menggunakan modul
"""


class SingletonWighMetaclass(type):
    """
    Menggunakan metaclass
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                SingletonWighMetaclass, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=SingletonWighMetaclass):
    """
    subclass
    """

    def log(self, message):
        """
        log 
        """
        print(message)


logger1 = Logger()
logger2 = Logger()

# logger1 dan logger2 adalah objek yang sama
print(logger1 is logger2)  # Output: True

#====================================

def singleton_decorator(cls):
    """
    decorator singleton
    """
    instances = {}

    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance


@singleton_decorator
class Database:
    """
    menggunakan decorator singleton
    """

    def __init__(self):
        print("Connecting to database...")


db1 = Database()
db2 = Database()

# db1 dan db2 adalah objek yang sama
print(db1 is db2)  # Output: True

#=============================
class _SingletonModule:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(_SingletonModule, cls).__new__(cls, *args, **kwargs)
        return cls._instance

class Database1(_SingletonModule):
    """
    singleton with modul
    """
    def __init__(self):
        print("Connecting to database...")

db1 = Database1()
db2 = Database1()

# db1 dan db2 adalah objek yang sama
print(db1 is db2)  # Output: True
