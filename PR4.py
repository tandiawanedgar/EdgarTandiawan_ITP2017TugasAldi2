change=input().upper()
x=[1,2,3]
for z in change:
    if z == "A":
        x[0],x[1] = x[1], x[0]
    elif z == "B":
        x[1],x[2] = x[2], x[1]
    elif z == 'C':
        x[0],x[2] = x[2], x[0]
    print(x)

