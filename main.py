number = int(input('Digite quantos primos quer imprimir: '))
contador = 0
i = 2
while contador < number:
    teste = 2
    primo = True
    while teste < i: 
        if i % teste ==0 and i !=teste:
            primo = False
            break
        teste = teste +1
    if primo:
        contador += 1
        print(i)
    i = i + 1