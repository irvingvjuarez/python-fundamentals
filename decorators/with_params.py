def custom_message(msg: str):
    def with_message(fn):
        def wrapper():
            print(msg)
            fn()
        return wrapper
    return with_message

@custom_message("Below you will see the fn execution message 👇")
def greet():
    print("I am the greeting. So, hello 👋")

if __name__ == "__main__":
    greet()