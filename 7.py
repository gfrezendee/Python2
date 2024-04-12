def exibir_tabuleiro(tabuleiro):

  for linha in tabuleiro:
    print(" | ".join(linha))

def verificar_posicao_livre(tabuleiro, posicao):

  linha = (posicao - 1) // 3
  coluna = (posicao - 1) % 3
  return tabuleiro[linha][coluna] == "-"

def marcar_posicao(tabuleiro, posicao, simbolo):

  linha = (posicao - 1) // 3
  coluna = (posicao - 1) % 3
  tabuleiro[linha][coluna] = simbolo

def verificar_vitoria(tabuleiro, simbolo):

  # Verificar linhas
  for linha in tabuleiro:
    if all(celula == simbolo for celula in linha):
      return True

  # Verificar colunas
  for coluna in range(3):
    if all(tabuleiro[linha][coluna] == simbolo for linha in range(3)):
      return True

  # Verificar diagonais
  if all(tabuleiro[i][i] == simbolo for i in range(3)):
    return True
  if all(tabuleiro[i][2-i] == simbolo for i in range(3)):
    return True

  return False

def jogo_da_velha():

  tabuleiro = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
  jogador_atual = "X"

  while True:
    exibir_tabuleiro(tabuleiro)

    posicao = int(input(f"Jogador {jogador_atual}, digite sua jogada (1-9): "))

    while not verificar_posicao_livre(tabuleiro, posicao):
      posicao = int(input("Posição inválida. Tente novamente (1-9): "))

    marcar_posicao(tabuleiro, posicao, jogador_atual)

    if verificar_vitoria(tabuleiro, jogador_atual):
      exibir_tabuleiro(tabuleiro)
      print(f"Parabéns, jogador {jogador_atual}! Você venceu!")
      break

    if all(not verificar_posicao_livre(tabuleiro, posicao) for posicao in range(1, 10)):
      exibir_tabuleiro(tabuleiro)
      print("Empate!")
      break

    jogador_atual = "O" if jogador_atual == "X" else "X"

if __name__ == "__main__":
  jogo_da_velha()
