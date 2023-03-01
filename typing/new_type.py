from typing import NewType

UserId = NewType("UserId", int)

if __name__ == "__main__":
    some_id = UserId(19237)

    print(type(some_id))