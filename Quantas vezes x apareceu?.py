lista = []

for i in range (10):
    n = int(input())
    lista.append(n)

x = int(input())
contador = 0
for i in range(len(lista)):
    num = lista[i]
    if num == x:
        contador +=1

print(contador)
