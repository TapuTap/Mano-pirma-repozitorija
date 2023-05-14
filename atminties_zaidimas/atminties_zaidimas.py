import random

# # Sukuriam kortų reikšmes, sudedame į sąrašą "poros" ir jas išmaišome
# poros = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
# random.shuffle(poros)
# print(poros)


# Korteles, kurias naudosime zaidime
CARDS = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F']

# Sumaisome korteles
random.shuffle(CARDS)
import PySimpleGUI as sg
import time

# Sudarome pradini langa su kortelemis
layout = [[sg.Button('', size=(8, 4), key=(i, j), pad=(2, 2)) for j in range(4)] for i in range(3)]
window = sg.Window('Atminties zaidimas', layout, finalize=True)

# Laikinai atverto kortelese issaugosime korteliu reiksmes
open_cards = []

# Laikinai paspausto mygtuko pozicija
pressed_button = None

# Kol dar yra korteles, kurios nera paaiskintos, tesiam zaidima
while CARDS:
    event, values = window.read()

    # Jei vartotojas uzdarineja lango, nutraukiam zaidima
    if event == sg.WINDOW_CLOSED:
        break

    # Atverti paspausta kortele
    i, j = event
    button = window[event]
    button.update(CARDS[i * 4 + j])
    open_cards.append((i, j))

    # Jei atvertos dvi korteles, patikrinam ar jos yra vienodos
    if len(open_cards) == 2:
        if CARDS[open_cards[0][0] * 4 + open_cards[0][1]] == CARDS[open_cards[1][0] * 4 + open_cards[1][1]]:
            # Jei korteles vienodos, isimame jas is lango ir