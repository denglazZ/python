tree = 20
day = 5
night = 4
snail = 0
i = 0
while(snail != tree):
    snail = snail + day
    print("metr day", snail)
    if(snail != tree):
        snail -= night
        print("metr night", snail)
    i += 1
    print("day =",i)
print(i)

    
