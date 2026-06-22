class Human:
    def __init__(self , name , age):
        self.name = name
        self.age = age
        
Emirhan = Human('Emirhan' , 13)
print(Emirhan)

class Counter:
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count += 1
    def get_count(self) -> int:
        return self.count

counter = Counter()
counter.increment()
counter.increment()

print(counter)


