def make_multiplier(n):

    def multiplier(x):
        return n * x

    return multiplier

if __name__ == "__main__":
    multiplier = make_multiplier(10)
    multiplication = multiplier(10)

    print(multiplication)