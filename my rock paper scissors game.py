
import random


value = {'r': 'rock', 'p': 'paper', 's': 'scissors'}

def play():
    user_choice = input('Choose a symbol\n (r) rock\n (p) paper\n (s) scissors: ')
    cpu_choice = random.choice(['r', 'p', 's'])

    if user_choice == cpu_choice:
        print("You threw a", value[user_choice],", and CPU threw a", value[cpu_choice],". Draw")
    elif winning_the_game(user_choice, cpu_choice):
        print("CPU threw a", value[cpu_choice], "and you threw a", value[user_choice], ". You win.")
    elif winning_the_game(cpu_choice, user_choice):
        print("CPU threw a", value[cpu_choice], ", and you threw a", value[user_choice], ". You lose")

def winning_the_game(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


play()

