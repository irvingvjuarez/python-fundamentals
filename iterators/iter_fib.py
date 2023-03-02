class Fib:
    def __init__(self, target):
        assert target > 0, f"Expected target greater than zero, but received {target}"
        self.target = target
    
    def __iter__(self):
        self.index = 1
        self.prev = 0
        self.current = 1
        return self
    
    def __next__(self):
        if self.index <= self.target:
            next = self.prev + self.current

            if self.index > 1:
                self.prev, self.current = self.current, next
            
            self.index += 1
            return next
        else:
            raise StopIteration

if __name__ == "__main__":
    for fib_num in Fib(8):
        print(fib_num)
