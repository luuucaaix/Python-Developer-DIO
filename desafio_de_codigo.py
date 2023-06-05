#Desafio 1 - Tuitando

T = input().lstrip()[:500]
if len(T)>=1 and len(T)<= 140:
    print('TWEET')
else:
    print('MUTE')

#Desafio 2 - Mês

months_dict = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

month = int(input("Digite um número entre 1 e 12: "))

if month < 1 or month > 12:
    print("Número inválido!")
else:
    i_month = months_dict[month]
    print(i_month)

#Desafio 3 - Encaixa ou Não? (Opção 1 - Pedindo entradas separadas)

N = int(input()) #Quantidade de casos teste

i = 0 #Quantidade de iterações

while(i < N):
    A = str(input("Insira A: "))    #Pergunta a string A
    B = str(input("Insira B: "))    #Pergunta a string B
    a = A[-len(B):]                 #Pega apenas o final da string A (deixando do mesmo tamanho que B)
    i += 1

    else:
        if B == a:
            print("encaixa")
        else:
            print("nao encaixa")

#Desafio 4 - Encaixa ou Não? (Opção 1 - Pedindo entradas juntas)
N = int(input()) #Quantidade de casos teste
n = N

while(n > 0):

    A, B = input().split(" ")
    c = (len(B))
    A = A[-c:]

    if B == A:
        print("encaixa")
    else:
        print("nao encaixa")

    n -= 1
