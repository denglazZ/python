a = ["Зебра", "Конь","Лошадь"]
while(True):
    b = input()
    c = False
    for i in a:
        if(b == i):
            c = True
    if(c):
        print("Такое значение есть")
    else:
        print("Добавили")
        a.append(b)
    for i in a:
        print(i)
    
