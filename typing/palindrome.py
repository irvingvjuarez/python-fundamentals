def palindrome(word: str) -> bool:
    word = word.replace(" ", "").lower()

    reversed_word = "".join( list(reversed(word)) )
    return word == reversed_word

if __name__ == "__main__":
    print(palindrome("Ligar es ser agil"))