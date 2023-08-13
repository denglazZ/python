class bankshet:
    def __init__(self,id,name,balanse):
        self.id = id
        self.name = name
        self.balanse = balanse
    def vnesti(self,number):
        self.balanse += number
        print("Деньги добавлены")
    def snyat(self,number):
        if(self.balanse >= 0):
            if(self.balanse - number >= 0 ):
                self.balanse -= number
                print("Деньги сняты")
            else:
                print("Недостаточно средств")
        else:
            print("Нет средств")

shet1 = bankshet(1,"Vasiliy",10000)
shet1.snyat(100001)
shet1.vnesti(10000)
print(shet1.balanse)
shet1.snyat(20000)
print(shet1.balanse)