# Stwórz grę w papier, kamień, nożyce


# Powodzenia!

from random import choice

def check_winner(player1hand, player2hand):
    if(player2hand == player1hand):
        return f'Remis poprzez Gracz1 {player1hand}: Gracz2 {player2hand}'
    if(player1hand == 'scissors' and player2hand == 'paper'):
        return f'Wygrywa Gracz1 poprzez Gracz1 {player1hand}: Gracz2 {player2hand}'
    if(player1hand == 'scissors' and player2hand == 'rock'):
        return f'Wygrywa Gracz2 poprzez Gracz1 {player1hand}: Gracz2 {player2hand}'
    if(player1hand == 'paper' and player2hand == 'rock'):
        return f'Wygrywa Gracz1 poprzez Gracz1 {player1hand}: Gracz2 {player2hand}'
    if(player1hand == 'paper' and player2hand == 'scissors'):
        return f'Wygrywa Gracz2 poprzez Gracz1 {player1hand}: Gracz2 {player2hand}'
    if(player1hand == 'rock' and player2hand == 'scissors'):
        return f'Wygrywa Gracz1 poprzez Gracz1 {player1hand}: Gracz2 {player2hand}'
    if(player1hand == 'rock' and player2hand == 'paper'):
        return f'Wygrywa Gracz2 poprzez Gracz1 {player1hand}: Gracz2 {player2hand}'

possibleMoves = ['paper', 'rock', 'scissors']



player1hand = choice(possibleMoves)
player2hand = choice(possibleMoves)

print(check_winner(player1hand, player2hand))