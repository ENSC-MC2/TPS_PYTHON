numList = [1,2,3,4,5]
alphaList = ["a","b","c","d","e"]
print(numList is alphaList)
print(numList == alphaList)
numList = alphaList

print(id(numList), id(alphaList))

print(numList is alphaList)
print(numList == alphaList)