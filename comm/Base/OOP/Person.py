class Person:
    Name = 90
    def __init__(self, name: str, age: int):
        self.Name = name
        self.Age = age
    def walk(self, count):
        print(self.Name, "идет", count,"шагов")
    def sleep(self):
        print("Человек спит")
    def eating(self):
        print("yummy")

Egor = Person("Егор", 9)
print(Egor.Name)
print(Egor.Age)
Egor.walk(90)
Egor.sleep()

Dinislam = Person("Динислам", 23)
print(Dinislam.Name)
print(Dinislam.Age)
Dinislam.walk(100)
Dinislam.sleep()