data=[]
for x in range (0,10):
    z=int(input('put your number'))
    y = z % 42
    data.append(y)
print(len(set(data)))
