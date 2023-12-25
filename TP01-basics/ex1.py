semaine = ["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimance"]

print("semain : \n",semaine)
print("valeur de jour 4 :\n",semaine[4])

# t=semaine[0]
# semaine[0]=semaine[-1]
# semaine[-1]=t

# or :
semaine[0],semaine[-1]=semaine[-1],semaine[0]

print("new valeur :\n",semaine)
print("12 fois :\n",semaine[-1]*12)