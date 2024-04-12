lugares_vagos = [10, 2, 1, 3, 0]

print("Bem-vindo! Utilize nosso app para reservar lugares em sua sessão.\n")

while True:
    numero_sala = int(input("Digite o número da sala (0 para sair): "))
    if numero_sala == 0:
        break

    lugares_solicitados = int(input(f"Quantos lugares você deseja na sala {numero_sala}: "))

    if lugares_vagos[numero_sala - 1] >= lugares_solicitados:
        print(f"Parabéns! Há {lugares_solicitados} lugares disponíveis na sala {numero_sala}.")
        lugares_vagos[numero_sala - 1] -= lugares_solicitados
        print(f"Compra realizada! Lugares vagos na sala {numero_sala}: {lugares_vagos[numero_sala - 1]}")
    else:
        print(f"Desculpe, não há {lugares_solicitados} lugares disponíveis na sala {numero_sala}.")

print("Obrigado pela preferência!")
