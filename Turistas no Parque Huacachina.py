jipsDentro = 0
pessoasDentro = 0

while True:
    prompt = [x for x in input().split()]
    if len(prompt) == 2:
        prompt[1] = int(prompt[1])
    if prompt[0] == "SALIDA":
        jipsDentro += 1
        pessoasDentro += prompt[1]
    if prompt[0] == "VUELTA":
        jipsDentro -= 1
        pessoasDentro -= prompt[1]
    if prompt[0] == "ABEND":
        break
print(pessoasDentro)
print(jipsDentro)
