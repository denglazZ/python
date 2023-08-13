class Uravnenie:
    def __init__(self,a,b):
        self.A = a
        self.B = b
    def Summa(self,a,b):
        print(a+b)

a = int(input())
b = int(input())
test = Uravnenie(a,b)
test.Summa(test.A,test.B)
