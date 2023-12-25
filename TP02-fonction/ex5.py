def aisement_dechiffrable(word):
    if word.isupper():
        result = ""
        for i in word:
            word_in_ascii = ord(i)
            if word_in_ascii == 90:
                word_in_ascii = 64
            result += chr(word_in_ascii+1)
        return result
    else:
        return f"{word} is lower case"


ch = "ABCCZABEY"
print(aisement_dechiffrable(ch))