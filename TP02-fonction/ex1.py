def Robinson(N):
    if N == 0:
        return "0"

    previous_term = "0"
    for n in range(1, N + 1):
        digit_count = [0] * 10
        result = ""

        # Compte les occurrences de chaque chiffre dans le terme précédent
        for digit in previous_term:
            digit_count[int(digit)] += 1

        # Construit le terme actuel en concaténant les occurrences et les chiffres
        for digit in range(9, -1, -1):
            if digit_count[digit] > 0:
                result += str(digit_count[digit]) + str(digit)

        previous_term = result

    return result


# Exemple d'utilisation :
N = 5
result = Robinson(N)
print(f"U{N} = {result}")
