def make_repeater(word: str):
    return lambda times: word * times

if __name__ == "__main__":
    repeater = make_repeater("Irving")
    repeated_str = repeater(5)

    print(repeated_str)