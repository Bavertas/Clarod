sente = str(input("Please Enter a Sentence :"))
arak = list(sente)
dara = []
for i in arak:
      dara.append(i)
dara_1 =([ [l, dara.count(l)] for l in set(dara)])    
    
print(dict(dara_1))  