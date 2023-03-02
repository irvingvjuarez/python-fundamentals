def my_gen():
    n = 0

    print("First hello")
    yield n

    print("Second hello")
    yield n

    print("Third hello")
    yield n


if __name__ == "__main__":
    foo = my_gen()
    try:
        print(next(foo)) # First
        print(next(foo)) # Second
        print(next(foo)) # Third
        print(next(foo)) # Error
    except StopIteration:
        print("Program finished")