a = [1, 2, 4, 5, 8]
b =[2, 3, 5, 6, 7, 8]

c= [(x%y) if x==y else 1 for x in b for y in a]

for x in b:
    for y in a:
        if x == y:
            c.append(x%y)
        else:
            c.append(1)    



print(c)



