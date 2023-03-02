my_list = [1,2,3,4,5]
my_iter = iter(my_list)

if __name__ == "__main__":
    while True:
        try:
            print(next(my_iter))
        except StopIteration:
            break