import time

def execution_time(fn):
    def wrapper(*args):
        start_time = time.time()
        fn(*args)
        end_time = time.time()

        return end_time - start_time

    return wrapper

@execution_time
def fib(n):
    if n == 1 or n == 2:
        return 1
    
    return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    print(fib(7))
    print(fib(8))