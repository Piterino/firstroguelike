from main_test import *
from display import *


player = {
    'class' : {'Hobo' : [12,1,0], 'Sewer-maintenance' : [8,1,1], 'White-belt' : [6,2,0]},
    'race' : {'Ogre' : [2,0,1], 'Reptilian' : [1,1,0], 'Moth-man' : [0,2,0]},
    'perk' : {'Critter' : 'critx3', 'Aspirine' : '+5hp', 'Secret' : 'mushrooms+1-3'}
}
HP_INDEX = 0
DMG_INDEX = 1
DEF_INDEX = 2

RACE_INDEX = 0
CLASS_INDEX = 1
PERK_INDEX = 2

def character_race():
    global char_race
    player_race = ['empty', 'Ogre', 'Reptilian', 'Moth-man']
    chosen_race = player_race[char_race]
    return chosen_race


def character_class():
    global char_class
    player_class = ['empty', 'Hobo', 'Sewer-maintenance', 'White-belt']
    chosen_class = player_class[char_class]
    return chosen_class


def character_perk():   # global into parameter
    global char_perk
    player_perk = ['empty', 'Critter', 'Aspirine', 'Secret']
    chosen_perk = player_perk[char_perk]
    return chosen_perk


def char_name_fun():
    global char_name
    char_name = input("What is the name of the immortal god-king of the underworld?: ")   

def import_intro_line(line_name, which_line = 0, path = 'text_lines/'):
    file_name = path + line_name
    global char_name
    with open(file_name) as line_read:
        line_name = line_read.readlines()
    line_name = [name.replace('NAME', char_name) for name in line_name]
    return line_name[which_line].strip('\n')         

def player_character():
    print("Your race HP/DMG/DEF gain: ",player['race'][character_race()])
    print("Your class HP/DMG/DEF: ",player['class'][character_class()])
    print("Your perk special: ",player['perk'][character_perk()])
    return [player['race'][character_race()],
    player['class'][character_class()],
    player['perk'][character_perk()]]

def char_start():
    char_name_fun()
    char_screen()
    player_character()

if __name__ == "__main__":
    char_start()