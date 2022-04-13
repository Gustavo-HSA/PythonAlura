import random   # importa o módulo random


print("**********************************")
print("Bem vindo ao jogo de adivinhação!!")
print("**********************************")

numero_secreto = random.randrange(1, 101)   # gera um número aleatório entre 1 e 100
total_de_tentativas = 0
pontos = 1000

print("Qual nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina a dificuldade desejada: "))

if nivel == 1:
    total_de_tentativas = 20
elif nivel == 2:
    total_de_tentativas = 10
elif nivel == 3:
    total_de_tentativas = 5
else:
    int(input("Erro! o número deve ser 1, 2 ou 3! escolha uma dificuldade pré-definida: "))

for rodada in range(1, total_de_tentativas + 1):
    print(f"Tentativa {rodada} de {total_de_tentativas}")
    numero_usuario = int(input("Digite um número entre 1 e 100: "))
    print(f"Você digitou {numero_usuario}")

    if numero_usuario < 1 or numero_usuario > 100:
        print("Você deve digitar um número entre 1 e 100!")
        continue  # continue diferente de break não sai do laço mas pula para a próxima iteração

    acerto = numero_usuario == numero_secreto
    maior = numero_usuario > numero_secreto
    menor = numero_usuario < numero_secreto

    if acerto:
        print(f"Parabéns!!! Você acertou o número correto e fez {pontos} pontos")
        break
    else:
        if menor:
            print("Que pena!! Você digitou um número menor")
        elif maior:
            print("Que pena!! Você digitou um número maior")
        pontos_perdidos = abs(numero_secreto - numero_usuario)
        pontos = pontos - pontos_perdidos

print("Fim do jogo")
