class Mammal:
    className = 'Млекопитающее'

class Dog(Mammal):
    specied = 'Canis lupus'

dog = Dog()
print(dog.className) # Млекопитающее


class A:
    def __init__(self):
        self.x = 10


class B(A):
    def __init__(self):
        super().__init__()
        self.y = self.x + 5


print(B().y)

b = B()
print(b.y)
