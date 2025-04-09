import time
import sys
# sys.set_int_max_str_digits(100000)

def timer(func):
    def wrapper_timer(*args, **kwargs):
        start_time = time.time()
        value = func(*args, **kwargs)
        end_time = time.time()
        print(f"Завершено за {end_time - start_time:.4f} секунд")
        return value
    return wrapper_timer

@timer
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

factorial(100000)