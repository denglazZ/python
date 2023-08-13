class Car:
    def __init__(self,brand :str,model:str,price:int):
        self.Brand = brand
        self.Model = model
        self.Price = price
    def Info(self):
        print(f"Brand = {self.Brand} Model = {self.Model} Price = {self.Price}")
    def Move(self,km):
        print(f"")


def Summa(a,b):
    print(a+b)
    return a+b
Summa("2","2")
Summa(2,2)