'''qtd= int(input("Quantos números você quer descobrir se são pares?: "))
i = 0
while i<=qtd:
    num = int(input("Digite um número e eu digo se ele é par ou não: "))
    if num%2 == 0:
        print(f"O número {num} é par")
    else:
        print(f"O número {num} é ímpar.")
    i += 1

resposta = input("VocÊ quer encontrar os numeros pares? (s/n): ")
j=0
while resposta != "s" and resposta != "n":
    print("Prestenção bobo!!!!!")
    resposta = input("Você quer encontrar numeros pares? (s/n): ")
    j += 1

if j != 0:
    print("Parabéns!!!!! você não é mais bobo")
elif resposta == "n":
    print ("Chatão d+ ein.")
else:
    print("Você é brabo!")

if resposta == "s":

    qtd = input("Quantos números você quer?: ")
    while not qtd.isnumeric():
        print("Decepcionado, você é muito bobo.")
        qtd = input("Quantos números você quer?.")
    qtd = int(qtd)

    i = 0

    while i < qtd:

        num = input("Diga um número: ")
        while not num.isnumeric():
            print("Decepcionado, você é muito bobo.")
            num = input("Diga um número.")

        num = int(num)
        if num%2 == 0:
            print(f"O número {num} é par.")
        else:
            print(f"O número {num} é ímpar")
        i += 1
        if i == qtd:
            print("Flw brabo.")

for nome in ["danilo","rafael","edson"]:
    print(f"o seu nome é: {nome}.")'''

resposta = input("Você quer descobrir a soma dos números de 1 a 100? (s/n): ")
i=0
conta = 0

if resposta == "s":
     while i < 100:
        print(f"a soma de {i} com a conta anterior é de {conta}")
        i += 1
        conta += i
else:
    print("bobão.")