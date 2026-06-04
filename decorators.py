import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        print(f"Elapsed Time: {elapsed_time:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    print("Done!")

@timer
def add(a: int, b: int) -> int:
    return a + b

slow_function()

print(add(3, 4))