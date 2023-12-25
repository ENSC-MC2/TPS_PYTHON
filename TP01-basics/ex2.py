entier = list(range(10))

print("les liste :\n",entier)

print("les column :")
for key,value in enumerate(entier):
    print("index : ",key," la valeur",value)

print("sum de tableau :\n",sum(entier))

t1 = [i*3 for i in entier]
print("multipe de list :",t1)

print("plus grand : ",max(entier))
print("plus petit : ",min(entier))
print("count pair : ",len([i for i in entier if i%2==0]))
print("sum inpair : ",sum([i for i in entier if i%2!=0]))