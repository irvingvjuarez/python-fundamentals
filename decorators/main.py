from typing import Callable

def decorator(fn: Callable[[], str]):
    def wrapper():
        print("Here is the beginning of the wrapper function")
        fn()
        print("Here is the end of the wrapper function")

    return wrapper

def greet():
    print("I am the greeting function")

if __name__ == "__main__":
    greeting = decorator(greet)
    greeting()