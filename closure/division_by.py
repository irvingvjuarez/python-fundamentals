def make_division_by(n: int):
    assert isinstance(n, int), \
        f"An integer should be received, but instead received {type(n)}"

    def division(x: str) -> float:
        assert isinstance(x, int), \
            f"An integer should be received, but instead received {type(x)}"

        return x / n
    
    return division

if __name__ == "__main__":
    division_by_3 = make_division_by(3)
    print(division_by_3(18))

    division_by_5 = make_division_by(5)
    print(division_by_5(100))

    division_by_18 = make_division_by(18)
    print(division_by_18(54))