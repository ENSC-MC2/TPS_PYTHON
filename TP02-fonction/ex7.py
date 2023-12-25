
def check_sum_nbr(n):
    return sum([int(i) for i in str(n)])+n

def autoNomber(nbr):
    n = 1
    while n != nbr:
        if nbr == check_sum_nbr(n):
            print(nbr," est auto-nombre")
            break
        else:
            n += 1
    if n == nbr:
        print(nbr, "n'est pas auto-nombre")

autoNomber(21)