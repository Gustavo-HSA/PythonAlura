def jogar():
    print("**********************************")
    print("***Bem vindo ao jogo da Forca***!!")
    print("**********************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    # enquanto enforcou and acertou forem True o jogo vai ser executado
    while not enforcou and not acertou:
        chute = input("Qual a letra? ")
        chute = chute.strip()  # strip remove espaços em branco na esquerda e direita

        index = 0
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                print(f"Encontrei a letra {letra} na posição {index}")
            index += 1
        print("Jogando....")



    print("Fim do jogo")


if __name__ == "__main__":
    jogar()
