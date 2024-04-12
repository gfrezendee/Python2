valores = [9, 8, 7, 12, 0, 13, 21]

pares = []
impares = []

for valor in valores:
    # Verificando se o valor é par (resto da divisão por 2 é zero)
    if valor % 2 == 0:
        pares.append(valor)  # Adiciona o valor par à lista de pares
    else:
        impares.append(valor)  # Adiciona o valor ímpar à lista de ímpares

print(f"Dada a lista: {valores}, esses são os valores pares e ímpares:\n")
print(f"Valores pares: {pares}")
print(f"Valores ímpares: {impares}")
