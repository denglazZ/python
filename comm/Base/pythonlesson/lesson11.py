def Max(a):
    max = a[0]
    for i in a:
        if(max<i):
            max = i
    print(max)

a = [-9,-10,-3,-4,-7,0]

b = [10,8,79,34,25,101,56]

Max(a)
print()
Max(b)

