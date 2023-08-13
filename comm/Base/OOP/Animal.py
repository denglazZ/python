class Animal:
    def __init__(self, age:int, name:str ,predator:bool,redbook:bool):
        self.name = name
        self.age = age
        self.predator = predator
        self.redbook = redbook

    def Prant(self):
        print(F"AGE: {self.age}")
        print(f"NAME:{self.name}")
        print(f"REDBOOK: {self.redbook}")
        print(f"PREDATOR: {self.predator}")

anml1 = Animal(23,"Shark",True,True)
anml1.Prant()

class Math:
    def dell(self, q1:int, q2:int):
        return q1/q2
a = Math.dell(4.5, 4.5)
print(a)


