liste = [17, 38, 10, 25, 72]
print(sorted(liste))
liste.append(15)
print(liste)
print(sorted(liste)[::-1])

for key,val in enumerate(liste):
    if val ==17:
        print(key)
    else:
        break

print("enleve 38 : ",liste.remove(38))
print("sous list 1 : ",liste[1:3])
print("sous list 2 : ",liste[:2])
print("sous list 3 : ",liste[2:])
print("sous list 4 : ",liste[:])
print("lat element : ",liste[-1])