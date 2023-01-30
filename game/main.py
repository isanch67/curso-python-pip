import random



# ************************************************************

def run_game():
  computer_wins = 0
  user_wins = 0
  round = 1
  while True:
    print('*' * 10)
    print('Round => ', round)
    print()
    print(f'Puntaje => Usuario: {user_wins} y Computadora {computer_wins}')
    print('*' * 10)

    user_option, computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
  
  
    
    if user_wins == 2:
      print()
      print('---- EL USUARIO GANÓ EL MATCH -----')
      break
    elif computer_wins == 2:
      print()
      print('---- LA COMPUTADORA GANÓ EL MATCH -----')
      break
    if user_option != None:
      round += 1
  print()

# *************************************************************

def choose_options():
  
  options = ('piedra','papel','tijera')
  user_option = input('piedra, papel o tijera => ').lower()
  
  # computer_option = 'tijera'
  computer_option = random.choice(options)
  if not user_option in options:
    print()
    print(f'la opción ({user_option}) no está contemplada en el juego')
    # continue
    return None, None
  else:
    print()
    print('Option del Usuario => ', user_option)
    print()
    print('Opción de la Computadora => ', computer_option)
    print()
    return user_option, computer_option
    
# *************************************************************
    
def check_rules(user_option, computer_option, user_wins, computer_wins):
  
  if user_option == computer_option:
    print('Empate!')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('Piedra Gana a Tijera ----> EL USUARIO GANA')
      user_wins += 1
    else:
      print('Papel Gana a Piedra ----> LA COMPUTADORA GANA')
      computer_wins += 1
  elif user_option == 'tijera':
    if computer_option == 'piedra':
      print('Piedra Gana a Tijera ----> LA COMPUTADORA GANA')
      computer_wins += 1
    else:
      print('Tijera Gana a Papel ----> EL USUARIO GANA')
      user_wins += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('Papel gana a Piedra ----> EL USUARIO GANA')
      user_wins += 1
    else:
      print('Tijera Gana a Papel ----> LA COMPUTADORA GANA')
      computer_wins += 1
  return user_wins, computer_wins
# ****************************************************************
      


run_game()