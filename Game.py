import random
#21 game flow
#Player have to decide to hit or stand, input 
#the house will follow certain rules to ask for more cards
#start game
#shuffle deck
# TIME TO PLAY, the house will get a turn before the players
#the players decide to hit or stand
# Ask the player name and age to be sure they can play
if __name__ == '__main__':
    print('Welcome to 21 Blackjack')
    num_players = int(input('Enter the number of players:'))
    players = {}
    for i in range(num_players):
        player_name = input(f'Enter your name player {i+1}:')
        player_age = int(input(f'Enter your age player {i+1}:'))
        if player_age <= 20:
            print('This player does not have the required age to play, sorry!')
        else:
            players[player_name] = player_age
    print(players)


    