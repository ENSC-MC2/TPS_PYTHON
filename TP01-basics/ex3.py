t=[]
for i in range(700, 1100):
    if (i%7 == 0 and i%5 != 0 and i%2 != 0):
        t.append(i)

print("les resultats : ",t)