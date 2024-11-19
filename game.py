# Jogo da velha
# x | x | x
# x | x | x
# x | x | x

#  (Possíveis jogadas)
#  (1, 1) | (1, 2) | (1, 3)
#  (2, 1) | (2, 2) | (2, 3)
#  (3, 1) | (3, 2) | (3, 3)

#  Combinações vencedoras
#  (1, 1) + (1, 2) + (1, 3)
#  (2, 1) + (2, 2) + (2, 3)
#  (3, 1) + (3, 2) + (3, 3)
#  (1, 1) + (2, 1) + (3, 1)
#  (1, 2) + (2, 2) + (3, 2)
#  (1, 3) + (2, 3) + (3, 3)
#  (1, 1) + (2, 2) + (3, 3)
#  (3, 1) + (2, 2) + (1, 3)

# Regras
# Um jogador começa, ele sempre começa como (x)
# Depois do primeiro jogador o segundo jogador joga, ele sempre joga como (o)
# O primero jogador joga novamente alternando entre ele e o segundo
# O primeiro que fazer uma combinação igual ganha
# Se nenhuma combinação for válida o jogo da "velha"

valid_options = [1, 2, 3]
winning_options = [
  [[1, 1], [1, 2], [1, 3]],
  [[2, 1], [2, 2], [2, 3]],
  [[3, 1], [3, 2], [3, 3]],
  [[1, 1], [2, 1], [3, 1]],
  [[1, 2], [2, 2], [3, 2]],
  [[1, 3], [2, 3], [3, 3]],
  [[1, 1], [2, 2], [3, 3]],
  [[3, 1], [2, 2], [1, 3]],
]

def select_line ():
  line = int(input('\n\nSelecione a linha: (Entre 1 e 3)\n'))
  
  while check_input(line) == False:
    line = select_line()
  
  return line

def select_column ():
  column = int(input('Selecione a coluna: (Entre 1 e 3)\n'))

  while check_input(column) == False:
    column = select_column()

  return column

def check_input (param):
  if param not in valid_options:
    print ('input inválido')
    print (param)
    return False
  return True

def ask_move ():
  line = select_line()
  column = select_column()

  return [line, column]

def check_move_is_valid(jogada, x_turn, jogadas_x, jogadas_o):
  if jogada in jogadas_x:
    return False
  
  if jogada in jogadas_o:
    return False

  return True

def change_turn (x_turn):
  if x_turn == True:
    x_turn = False
  else:
    x_turn = True
  return x_turn

def check_if_win (jogadas):
  for winning_option in winning_options:
    check_combination = []  
    for combination in winning_option:
      if(combination in jogadas): check_combination.append(combination)
    if len(check_combination) == 3:
      return True
  return False

def draw_board (jogadas_x, jogadas_o):
  board = [[" " for _ in range(3)] for _ in range(3)]

  for pos in jogadas_x:
    board[pos[0] - 1][pos[1] - 1] = "X"
  for pos in jogadas_o:
    board[pos[0] - 1][pos[1] - 1] = "O"

  print("\n\n\n")
  for i in range(3):
    print(" | ".join(board[i]))
    if i < 2:
      print("---------")

def game():
  game_finished = False
  jogadas = []

  x_turn = True
  jogadas_x = []
  jogadas_o = []

  while game_finished == False:
    jogada = ask_move()

    while check_move_is_valid(jogada, x_turn, jogadas_x, jogadas_o) == False:
      print("Combinação já feita, tente novamente: ")
      jogada = ask_move()

    if x_turn == True:
      jogadas_x.append(jogada)
      if check_if_win(jogadas_x) == True:
        print("\n\nJogador 'X' venceu!\n\n")
        game_finished = True
    else:
      jogadas_o.append(jogada)
      if check_if_win(jogadas_o) == True:
        print("\n\nJogador 'O' venceu!\n\n")
        game_finished = True

    x_turn = change_turn(x_turn)
    draw_board(jogadas_x, jogadas_o)
  
  print('\n\nJOGO FINALIZADO\n\n')


game()