import random
import os
import platform
from hotcold import *
is_char_screen = False
is_first_screen = True
press_f_to_start = ((100*" ")+"\033[1;33;48m Press f to start"+(5*"\n"))
press_f_to_continue = ((100*" ")+"\033[1;33;48m Press f to continue or s to skip"+(3*"\n"))
press_l_to_quit = (3*'\n'+10*' '+"Press l to quit")
press_f_to_finish = ((65*' ')+"Press f to finish creating your character.")


sunglasses = False
intro_ended = False

char_class = 0
char_race = 0
char_perk = 0

intro_sprites_1 = [
        'syringe_sprite',
        'syringe_sprite',
        'dna_sprite',
        'dna_sprite',
        'sun_sprite',
        'fire_sprite',
        'einstein_sprite',
]
intro_sprites_2 = [
        'house_sprite',
        'title_sprite',
        'reptilian_sprite',
        'crown_sprite'
]


create_player = {
    'class' : {'Hobo' : [12,1,0], 'Sewer-maintenance' : [8,1,1], 'White-belt' : [6,2,0]},
    'race' : {'Ogre' : [2,0,1], 'Reptilian' : [1,1,0], 'Moth-man' : [0,2,0]},
    'perk' : {'Critter' : 'critx3', 'Aspirine' : '+5hp', 'Secret' : 'mushrooms+1-3'}
}



def player_character():
    print("Your race HP/DMG/DEF gain: ",create_player['race'][character_race()])
    print("Your class HP/DMG/DEF: ",create_player['class'][character_class()])
    print("Your perk special: ",create_player['perk'][character_perk()])
    return [create_player['race'][character_race()],
            create_player['class'][character_class()],
            create_player['perk'][character_perk()]]


def enter_char_screen():
    global intro_ended
    while intro_ended != True:
        pressedkey = getch()
        screen_text_update(press_f_to_continue, import_intro_line('intro_2', 3), import_sprite(intro_sprites_2[3], 10) ,press_l_to_quit)
        if pressedkey == 'f' or pressedkey == 's':
            intro_ended = True
        elif pressedkey == 'l':
            leave_game()


def intro_screen_script():
    screen_text_update(press_f_to_continue, import_sprite('title_sprite', 70), '', press_l_to_quit)
    slide_show('intro_1', 7, intro_sprites_1)
    slide_show('intro_2', 4, intro_sprites_2)
    enter_char_screen()


def slide_show(text_file = 'intro_1', slides = 0, which_sprites = intro_sprites_1):
    global intro_ended
    which_slide = 0
    while which_slide < slides and intro_ended != True:
        pressedkey = getch()
        if pressedkey is 'l':
            leave_game()
        elif pressedkey is 'f':
            screen_text_update(press_f_to_continue,
            import_intro_line(text_file, which_slide),
            import_sprite(which_sprites[which_slide], 70),
            press_l_to_quit)
            which_slide += 1
        elif pressedkey is 's':
            intro_ended = True
            which_slide += slides


def char_screen_update():
    return screen_text_update (
                        import_intro_line('race', char_class),
                        import_intro_line('class', char_race),
                        import_intro_line('perk', char_perk),
                        press_l_to_quit+press_f_to_finish,
                        (5*'\n'+80*' ')
            )


char_race_options = {
    'a' : 1,
    's' : 2,
    'd' : 3
}
char_class_options = {
    'q' : 1,
    'w' : 2,
    'e' : 3
}
char_perk_options = {
    'z' : 1,
    'x' : 2,
    'c' : 3
}


def char_screen():
    global intro_ended
    intro_ended = True
    is_character_finished = False
    global char_class
    global char_race
    global char_perk
    char_screen_update()

    while is_character_finished != True:
        pressedkey = getch()
        if pressedkey is 'l':
            leave_game()
        elif pressedkey in char_race_options:
            char_race = char_race_options[pressedkey]
            char_screen_update()
        elif pressedkey in char_class_options:
            char_class = char_class_options[pressedkey]
            char_screen_update()
        elif pressedkey in char_perk_options:
            char_perk = char_perk_options[pressedkey]
            char_screen_update()
        elif pressedkey is 'f':
            if char_class == 0 or char_race == 0 or char_perk == 0:
                char_screen_update()
                print('You must choose!')
            else:
                is_character_finished = True
        

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


def character_perk():
    global char_perk
    player_perk = ['empty', 'Critter', 'Aspirine', 'Secret']
    chosen_perk = player_perk[char_perk]
    return chosen_perk


def char_name_fun():
    global char_name
    char_name = input("Who dares enetring >>THE GUTTER<< ?: ")
    return char_name


def import_sprite(sprite_name, how_far = 0, path = 'sprites/'):
    spaced_sprite = ''
    file_name = path + sprite_name
    spaces = how_far * ' '
    with open(file_name, encoding='utf-8') as sprite_read:
        sprite_name = sprite_read.readlines()
        for each_line in sprite_name:
            new_line = (spaces)+each_line
            spaced_sprite += new_line
        return spaced_sprite


def import_intro_line(line_name, which_line = 0, path = 'text_lines/'):
    file_name = path + line_name
    global char_name
    with open(file_name, encoding='utf-8') as line_read:
        line_name = line_read.readlines()
    line_name = [name.replace('NAME', char_name) for name in line_name]
    return line_name[which_line].strip('\n')


def import_char_screen_line(line_name, path = 'text_lines/'):
        file_name = path + line_name
        with open(file_name, encoding='utf-8') as line_read:
                line_name = line_read.readlines()


def import_room(room_name, path = 'rooms/'):
    i = 1
    room_dict = {}
    room_x = []
    room_directory = path+room_name
    with open(room_directory, encoding='utf-8') as room_read:
        room = room_read.readlines()
    for y_axis in room:
        y_axis = y_axis.strip('\n')
        y_axis = list(y_axis)
        room_dict[i] = y_axis
        i += 1
    return room_dict


def screen_text_update(text_line_1 = '', text_line_2 = '', text_line_3 = '', text_line_4 = '', text_modifier = ''):
    os.system('clear')
    print(text_modifier+text_line_1)
    print(text_modifier+text_line_2)
    print(text_modifier+text_line_3)
    print(text_modifier+text_line_4)
    os.system('clear')
    print(text_modifier+text_line_1)
    print(text_modifier+text_line_2)
    print(text_modifier+text_line_3)
    print(text_modifier+text_line_4)


def display_enemy():
    is_running = False
    os.system('clear')
    print(centipede_sprite)
    print ("You lost 2 $$$")
    xdddd = input("Press enter")

    is_running = True


def lose_screen():
    os.system('clear')
    print (import_sprite('lose_screen_sprite'))
    exit()

def win_screen():
    os.system('clear')
    print (import_sprite('win_screen_sprite'))
    exit()

def sphinx_screen():
    os.system('clear')
    guess_game()

def leave_game():
    os.system('clear')
    print('Goodbye')
    exit()

def display_enemy(enemy_sprite):
    os.system('clear')
    print(enemy_sprite)


def display_bar(resource):
    bar = ''
    for i in range(resource):
        bar += "|"
    return bar

def leave_game():
    os.system('clear')
    print('Goodbye')
    exit()


def pressedkey():
    return getch().lower()


try:
    from msvcrt import getch
except ImportError:
    def getch():
    
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


title_formatted = '%2000s' % '\n'+import_sprite('title_sprite')
room = import_room('room_1')    #to be changed to rmg

RACE_INDEX = 0
CLASS_INDEX = 1
PERK_INDEX = 2

HP_INDEX = 0
DMG_INDEX = 1
DEF_INDEX = 2

def show_legend():
    i = 0
    while i < 14:
        print(import_intro_line('legend', i))
        i += 1


def display():
    os.system('clear')
    name = char_name_fun()
    intro_screen_script()
    char_screen()
    creation_list = player_character()
    player_creation = {
        'name' : name,
        'level' : 1,
        'exprience' : 0,
        'current hp' : creation_list[CLASS_INDEX][HP_INDEX],
        'limit hp' : creation_list[CLASS_INDEX][HP_INDEX],
        'base armor' : creation_list[CLASS_INDEX][DEF_INDEX],
        'base damage' : creation_list[CLASS_INDEX][DMG_INDEX],
        'weapon_name' : 'Headbutt',
        'armor_name' : 'Used Underwear',
        'perk' : creation_list[PERK_INDEX],
        'crit multiplier' : 2,
        'money' : 0
    }
    return player_creation
    
if __name__ == "__main__":
    display()

def guess_game():
    is_guess_game = True
    is_guess_game2 = True
    number = random.randint (1, 666)
    guesses_taken = 0
    guess = 0
    print("I am the master of the labirynth. Solve my mystery od die!")
    print("I am thinking of a number between 1 and 666")
    while is_guess_game:
        while is_guess_game2:
            try:
                if guess is not 0:
                    print("Your last guess: " + str(guess))
                print(import_sprite('sphinx_sprite'))
                print("You guessed " + str(guesses_taken) + " times")
                guess = int(input("Enter your number: "))
                os.system('clear')
                guesses_taken += 1
                is_guess_game2 = False
            except ValueError:
                os.system('clear')
                print("It's not even a number")
                is_guess_game2 = True
        if guess < number:
            if abs(number - guess) < 10:
                print("Oof, that's hot")
            elif abs(number - guess) > 10:
                print("That's cold my dude")
            print("Your guess is too low")
        elif guess > number:
            if abs(number - guess) < 10:
                print("Oof, that's hot")
            elif abs(number - guess) > 10:
                print("That's cold my dude")
            print("Your guess is too high")
        else:
            win_screen()
        if guesses_taken > 10:
            lose_screen()

        is_guess_game2 = True