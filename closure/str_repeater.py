def make_repeater(word: str):
    assert isinstance(word, str), f"A string should be received, but instead received {type(word)}"

    def repeater(times):
        assert isinstance(times, int), f"An integer should be received, but instead received {type(times)}"

        return word * times
    
    return repeater

if __name__ == "__main__":
    repeater = make_repeater("Irving")
    repeated_str = repeater(5)

    print(repeated_str)