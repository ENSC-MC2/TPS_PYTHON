def heureux(nb):
    res = nb
    same_val = []

    while nb != 1 and nb not in same_val:
        same_val.append(nb)
        nb = sum(int(i)**2 for i in str(nb))

    if nb ==1:
        return f"{res} est heureux"
    else:
        return f"{res} n'est pas heureux"


print(heureux(7))