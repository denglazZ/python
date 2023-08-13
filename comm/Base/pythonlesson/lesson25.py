'''a = []
b = input().split()
for i in range(len(b)):
    a.append(int(b[i]))
for i in a:
    print(i)'''
        
a = input().split()
b = []
height = int(a[0])
width = int(a[1])
for i in range(height):
    elements = input().split()
    for j in range(width):
        b.append(elements[j])
for i in b:
    print(i)
