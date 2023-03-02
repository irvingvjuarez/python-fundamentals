def to_upper(fn):
    wrapper = lambda text: fn(text).upper()
    
    return wrapper

@to_upper
def message(name):
    return f"{name}, you have 1 new message"

if __name__ == "__main__":
    print(message("myself"))