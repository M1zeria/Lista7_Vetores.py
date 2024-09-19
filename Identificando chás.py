tipoCha = int(input())

contador = 0

respostas = [int (x) for x in input().split()]

for i in range(len(respostas)):
    if respostas[i] == tipoCha:
        contador += 1
        
print(contador)

