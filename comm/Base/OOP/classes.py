class Person:
    def __init__(self):
        self.Name = "Sergey"
        self.Surname = "Ivanov"
        self.Age = 25
    def work(self, message):
        print(message)
    def pol(self, lool :int):
        print(lool)



class Worker(Person):
    def __init__(self):
        self.salary = 500
        self.post = "Director"

Andrey = Worker()
Andrey.pol("hello")