

# with open("monfichie.txt","r") as f :
#     print("using readline ==>",f.readline())
#     # print("using readlines ==>",f.readlines())


# # ex2:

with open("monfichie.txt","a") as f :
    f.write(", Par moi, apprenti développeur\n")

filee = open("monfichie.txt","r")
print("using readline ==>",filee.readline())
filee.close()

# ex3:

def saisir():
    nb = int(input("Donner un nombre des etudiant : "))
    for i in range(nb):
        cin = input("Donner le cin : ")
        nom = input("Donner le nom : ")
        prenom = input("Donner le prenom : ")
        age = input("Donner l'age : ")

        while not age.isdigit():
            age = input("Donner l'age : ")

        decision = input("donnez decision ? (admis, refusé, ajourné) :") 

        while decision.lower() not in ["admis","refuse","ajourne"]:
            decision = input("donnez decision ? (admis, refusé, ajourné) :") 

        with open("concours.txt","a") as f :
            f.write(f"{cin},{nom},{prenom},{age},{decision.lower()}\n")
        
def admis():
    l = []
    with open("concours.txt","r") as f :
        for line in f.readlines():
            if line.split(",")[-1].strip() == "admis":
                l.append(line)
    
    with open("admis.txt","w+") as f_admis :
        for line in l:
            f_admis.write(line)
            
def attente():
    l = []
    with open("admis.txt","r") as f :
        for line in f.readlines():
            if int(line.split(",")[3]) >= 30:
                l.append(f'{line.split(",")[0]};{line.split(",")[1]};{line.split(",")[2]}\n')
    
    with open("attente.txt","w+") as f_attent :
        for line in l:
            print(line)
            f_attent.write(line+"\n")

# saisir()
# admis()
# attente()