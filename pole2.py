body = []
for i in range(10):
    skóre = int(input("Zadej skóre (0-60): "))
    body.append(skóre)
print("Všechny skóre jsou", body)
print("Nejlepší skóre je", max(body))
print("Nejnižší skóre je", min(body))
print("Průměrné skóre je", sum(body) / 10)

for i in (body):
    nad_50 = sum(1 for skore in body if skore > 50)
if nad_50 >= len(body) / 2:
    print("Výborný výsledek !!")
else:
    print("Můžete to zkusit lépe")













        
