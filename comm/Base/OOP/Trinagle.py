import math
class Triangle:
    def __init__(self, Ax, Ay, Bx, By, Cx, Cy):
        self.AC = Cy - Ay
        self.BC = Bx - Cx
        self.AB = round(math.sqrt((self.BC ** 2) + (self.AC ** 2)),1)
        self.Perimetr = self.AB+self.BC+self.AC
        self.Ploshad = (self.AC*self.BC)//2
    def Print(self):
        print(f"AC = {self.AC}, BC = {self.BC}, AB = {self.AB}, Perimetr = {self.Perimetr}, Ploshad = {self.Ploshad}")

treug = Triangle(100,100,560,560,100,550)
treug.Print()

treug2 = Triangle(50,50,350,350,50,350)
treug2.Print()




