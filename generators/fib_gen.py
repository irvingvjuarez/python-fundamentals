def fib_gen(max: int):
    assert isinstance(max, int), \
        f"Expecting an integer, but received {type(max)}"
    
    index = current = 1
    prev = 0

    while index <= max:
        next_val = prev + current

        if index > 1:
            prev, current = current, next_val
        
        index += 1
        yield next_val


if __name__ == "__main__":
    gen = fib_gen(8)

    for num in gen:
        print(num)