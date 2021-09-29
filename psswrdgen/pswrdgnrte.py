import random

special_char = ["!","@","$","%","&","*"]
wordlist=[]

with open("history.text","r") as file:
    data=file.readlines()


    for line in data:
        wod=line.split()
        print(wod)

        for item in wod:
             if len(item) >5 :
                 wordlist.append(item.capitalize())

print(wordlist)
passs=random.choice(wordlist)
sd=random.choice(special_char)
ws=str(random.randint(10,99))

#qrt=passs+sd+ws
print(passs+sd+ws)









