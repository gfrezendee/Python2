lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

print(f"Dada a lista: {lista}, observe as informações abaixo.\n")

maior = lista[0]
for numero in lista:
    if numero > maior:
        maior = numero
print(f"O maior é: {maior}")

menor = lista[0]
for numero in lista:
    if numero < menor:
        menor = numero
print(f"O menor é: {menor}")

for numero in lista:
    if numero % 2 == 0:
        print(f"Par: {numero}")

primeiro_elemento = lista[0]
frequencia = lista.count(primeiro_elemento)
print(f"O {primeiro_elemento} aparece {frequencia} vezes")

soma = 0
for numero in lista:
    soma += numero
media = soma / len(lista)
print(f"A média é: {media:.2f}")

soma_negativos = 0
for numero in lista:
    if numero < 0:
        soma_negativos += numero
print(f"A soma dos negativos resulta em: {soma_negativos}")
