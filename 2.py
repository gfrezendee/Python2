import random

def jogo_da_forca():
    """
    Função principal do jogo da forca, simplificada ao máximo.

    Argumentos:
        Nenhum.

    Retorno:
        Nenhum.
    """

    palavras = ["banana", "carro", "python"]  # Lista de palavras
    palavra = random.choice(palavras)  # Escolha aleatória
    palavra_visivel = ["_" for _ in palavra]  # Palavra inicial com "_"
    acertos = 0
    erros = 0
    chances = 6

    print(f"Bem-vindo ao Jogo da Forca! Você tem {chances} chances.")

    while True:
        print("\nPalavra:", "".join(palavra_visivel))
        chute = input("Digite uma letra: ").lower()

        if chute in palavra:
            for i, letra in enumerate(palavra):
                if letra == chute:
                    palavra_visivel[i] = letra
                    acertos += 1

            if acertos == len(palavra):
                print(f"Parabéns! Você acertou: {palavra}")
                break

        else:
            erros += 1
            print(f"Letra errada! Você ainda tem {chances - erros} chances.")

            if erros == chances:
                print(f"Você perdeu! A palavra era: {palavra}")
                break

if __name__ == "__main__":
    jogo_da_forca()
