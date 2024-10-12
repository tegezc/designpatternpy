# Decorator Pattern

Decorator pattern adalah desain pattern yang memungkinkan kita untuk menambahkan fungsionalitas baru ke suatu objek tanpa mengubah struktur objek asli. Dalam konteks Python, decorator sering digunakan untuk memodifikasi perilaku fungsi.

Contoh Sederhana: Logging

Misalkan kita ingin menambahkan fitur logging ke beberapa fungsi. Dengan decorator, kita bisa melakukannya tanpa mengubah kode dalam fungsi itu sendiri:

``` python
import functools

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @functools.wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            f"Ran with args: {args}, and kwargs: {kwargs}")
        result = orig_func(*args, **kwargs)
        logging.info(f"Returned: {result}")
        return result

    return wrapper

@my_logger
def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

display_info("Alice", 30)
```
## Penjelasan
- my_logger: Ini adalah decorator kita. Ia menerima fungsi asli sebagai argumen dan mengembalikan sebuah wrapper function.
- wrapper: Fungsi ini menjalankan fungsi asli, tetapi sebelum dan sesudah eksekusi, ia melakukan logging.
- @functools.wraps: Decorator ini digunakan untuk mempertahankan metadata dari fungsi asli, seperti nama fungsi dan docstring.

## Contoh lain : Timing Fungsi

``` python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time elapsed: {end_time - start_time} seconds")
        return result
    return wrapper

@timer
def my_long_running_function():
    # Kode yang membutuhkan waktu lama untuk dijalankan
    time.sleep(2)
    print("Done!")
```
## Contoh dengan Argumen

Decorator juga bisa menerima argumen:
``` python
def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")
```

