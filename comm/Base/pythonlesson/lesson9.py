def maximum(a):
    maxx = a[0]
    for i in a:
        if(maxx<i):
            maxx = i
    print(maxx)

a = [1,2,3,4,5,6,7,8]
b = [10,56,32,12,67,55]

maximum(a)
maximum(b)
