def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Seri!"
    elif (player_choice == 'Gajah' and computer_choice == 'Jerapah') or \
         (player_choice == 'Jerapah' and computer_choice == 'Semut') or \
         (player_choice == 'Semut' and computer_choice == 'Gajah'):
        return "Player Menang!"
    else:
        return "Computer Menang!"
