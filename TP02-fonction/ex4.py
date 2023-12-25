
def CH(word):
    s=1
    reslt_of_ch = ""
    for i in range(1,len(word)):
        if word[i] == word[i-1]:
            s += 1
        else:
            reslt_of_ch += f'{s}{word[i-1]}'
            s=1

    return reslt_of_ch + f'{s}{word[-1]}'

ch = "aaaFyBssssssssssssazz"
print("last result ==> ",CH(ch))