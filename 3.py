def verificar_parenteses(expressao):

    pilha = []

    for caractere in expressao:
        if caractere == "(":
            pilha.append("(")
        elif caractere == ")":
            if not pilha:
                return False
            pilha.pop()

    return not pilha

if __name__ == "__main__":
    expressao = input("Digite a expressão com parênteses: ")

    if verificar_parenteses(expressao):
        print("Não há erro na expressão, tudo certo!")
    else:
        print("Errooooooooou!")
