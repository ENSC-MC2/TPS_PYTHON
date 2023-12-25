def calc_multi_list(nbr_cdu_str):
    l = int(nbr_cdu_str[0])
    for i in range(1,len(nbr_cdu_str)):
        l *= int(nbr_cdu_str[i])
    return l

def cdu(nbr_cdu):
    if nbr_cdu>0 and isinstance(nbr_cdu,int):
        sum_cdu = sum([int(i) for i in str(nbr_cdu)])
        multi_cdu = calc_multi_list(str(nbr_cdu))
        if multi_cdu % sum_cdu == 0:
            return f"L’entier {nbr_cdu} vérifie cette propriété"
        else:
            return f"L’entier {nbr_cdu} ne vérifie pas cette propriété"
    else:
        return f"{nbr_cdu} pas un entier ou pas positif"

print(cdu(514))
print(cdu(5143))