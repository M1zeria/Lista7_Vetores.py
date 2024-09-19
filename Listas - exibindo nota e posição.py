qtdNotas = int(input())
notas = []
soma = 0

if qtdNotas <= 0:
    print("Numero de notas invalido.")
    
else:
    for i in range (qtdNotas):
        nota = float(input())
        notas.append(nota)
        soma = soma + nota

    for i in range (len(notas)):
        print(f"Nota {i+1}: {notas[i]}")

    print(f"Media: {soma/len(notas):.2f}")

