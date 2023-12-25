def estdistinct(nb):
    str_nb = str(nb)
    s=0
    for i in str_nb:
        s+=str_nb.count(i)
    if s>len(str_nb):
        return f"{nb} est non distinct"
    else:
        return f"{nb} est distinct"

print("test : ",estdistinct(1273))
print("test : ",estdistinct(1565))