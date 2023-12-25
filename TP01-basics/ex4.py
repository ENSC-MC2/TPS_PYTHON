stock = ["Ordinateur de bureau", "Ordinateur portable", 100, "Caméra",310.28,"Haut-parleurs" , 27.00,\
         "Télévision" , 1000, "Cartes meres" ,"souris" , "clavier" , 500,"barrettes de mémoire"]

print("list : ",stock)

stock_char,stock_int = [], []
for i in stock:
    if type(i) is str:
        stock_char.append(i)
    elif type(i)==type(1) or type(i)==type(1.1):
        stock_int.append(i)

print("\nliste separer :")
print(stock_char,"\n",stock_int)

print(" le nombre d’élément de stock_char est:",len(stock_char))
print(" le nombre d’élément de stock_int est:",len(stock_int))
print("stock_char trie :",sorted(stock_char))
print("stock_char reversed :",sorted(stock_char)[::-1])
print("stock_int trie :",sorted(stock_int))
print("stock_int reversed :",sorted(stock_int)[::-1])

