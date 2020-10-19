"""
haslo do zgadniecia pogrupowane jako wpisy w bazie danych (?)
rysowanie wisielca po skusze


 |----
 |   |
 |   0
 |  /|\
 |  / \
 |  
/ \  *

    
"""
import numpy as np

password = 'kocham cię'

letters_list = []
known_letters_list = []

def print_password():        
    for i in password:
        if i in known_letters_list:
            print(i, end=" ")
        elif i == ' ':
            print('  ', end=" ")
        else:
            print('_ ', end=" ")

def print_hangman():
    global licznik_skuch
    global play
    if licznik_skuch == 1:
        print(' ')
        print('    ')
        print('   ')
        print('   ')
        print('   ')
        print('   ')
        print('/ \\  ')
    if licznik_skuch == 2:
        print(' ')
        print('    ')
        print('   ')
        print('   ')
        print(' |  ')
        print(' |  ')
        print('/ \\  ')
    if licznik_skuch == 3:
        print(' |')
        print(' |   ')
        print(' |  ')
        print(' |  ')
        print(' |  ')
        print(' |  ')
        print('/ \\  ')
    if licznik_skuch == 4:
        print(' |----')
        print(' |   |')
        print(' |  ')
        print(' |  ')
        print(' |  ')
        print(' |  ')
        print('/ \\  ')
    if licznik_skuch == 5:
        print(' |----')
        print(' |   |')
        print(' |   0')
        print(' |  \|/')
        print(' |  / \\')
        print(' |  ')
        print('/ \\  ')
    if licznik_skuch == 6:
        print(' |----')
        print(' |   |')
        print(' |   0')
        print(' |  /|\\')
        print(' |  / \\')
        print(' |  ')
        print('/ \\  *')
        print('')
        print('PRZEGRANKO :(')
        play = False
        print('poprawne haslo to: {0}'.format(password))


def user_input():
    user_input = input('\n')
    if user_input in known_letters_list:
        print('error: letter already known')
    else:
        return user_input  


def check(letter):
    global licznik_skuch
    if letter in letters_list:
        known_letters_list.append(letter)    
    else:   # instrukcje co ma zrobic jak skucha
        
        licznik_skuch += 1
        print_hangman()


for i in password:
    if i not in letters_list and i != ' ':
        letters_list.append(i)        


print_password()

licznik_skuch = 0
play = True
while play == True:  
    check(user_input())
    print_password()

    
    if sorted(letters_list) == sorted(known_letters_list):
        print('')
        print('\n' + 'ZWYCIESTWO!')
        play = False