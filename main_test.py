import random
import os
import platform
from hotcold import *
is_char_screen = False
is_first_screen = True
press_a_to_start = ((50*" ")+"\033[1;33;48m Press a to start"+(5*"\n"))
press_a_to_continue = ((50*" ")+"\033[1;33;48m Press a to continue or s to skip"+(3*"\n"))
press_l_to_quit = (3*'\n'+"Press l to quit")
pos = []
key = False
sunglasses = False
intro_ended = False
money = 0
char_class = 0
char_race = 0
char_perk = 0
up_direction = (-1,0)
down_direction = (1,0)
right_direction = (0,1)
left_direction = (0,-1)
directions = {
    'w': (-1,0),
    's': (1,0),
    'd': (0,1),
    'a': (0,-1)
}
stuff =  {
        'wall' :  "#",
        'player'   :  "@",
        'empty'    :  ".",
        'money'    :  "$",
        'chest'    :  "C",
        'entrance' :  "0",
        'key'      :  "K",
        'sunglasses': "B",
        'mushroom' :  "?",
        'bambi'    :  "b",
        'centipede':  "|",
        'owl'      :  "%",
        'gorilla'  :  "G",
        'sanic'    :  "&",
        'yeet'     :  "Y",
        'dexter'   :  "8",
        'santa'    :  "*",
        'sphinx'   :  "^"
}
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
player = {
    'class' : {'Hobo' : [12,1,0], 'Sewer-maintenance' : [8,1,1], 'White-belt' : [6,2,0]},
    'race' : {'Ogre' : [2,0,1], 'Reptilian' : [1,1,0], 'Moth-man' : [0,2,0]},
    'perk' : {'Critter' : 'critx3', 'Aspirine' : '+5hp', 'Secret' : 'mushrooms+1-3'}
}
HP_INDEX = 0
DMG_INDEX = 1
DEF_INDEX = 2





def player_character():
    print("Your class HP/DMG/DEF: ",player['class'][character_class()])
    print("Your race HP/DMG/DEF gain: ",player['race'][character_race()])
    print("Your perk",player['perk'][character_perk()])
    return print([player['class'][character_class()],
    player['race'][character_race()],
    player['perk'][character_perk()]])


def enter_char_screen():
    global intro_ended
    while intro_ended != True:
        pressedkey = getch()
        screen_text_update(press_a_to_continue, import_intro_line('intro_2', 3), import_sprite(intro_sprites_2[3], 10) ,press_l_to_quit)
        if pressedkey == 'a' or pressedkey == 's':
            intro_ended = True
        elif pressedkey == 'l':
            leave_game()


def intro_screen_script():
    screen_text_update(press_a_to_continue, import_sprite('title_sprite'), '', press_l_to_quit)
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
        elif pressedkey is 'a':
            screen_text_update(press_a_to_continue,
            import_intro_line(text_file, which_slide),
            import_sprite(which_sprites[which_slide], 10),
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
                        press_l_to_quit
            )


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
        elif pressedkey is 'a':
            char_race = 1
            char_screen_update()
        elif pressedkey is 's':
            char_race = 2
            char_screen_update()
        elif pressedkey is 'd':
            char_race = 3
            char_screen_update()
        elif pressedkey is 'q':
            char_class = 1
            char_screen_update()
        elif pressedkey is 'w':
            char_class = 2
            char_screen_update()
        elif pressedkey is 'e':
            char_class = 3
            char_screen_update()
        elif pressedkey is 'z':
            char_perk = 1
            char_screen_update()
        elif pressedkey is 'x':
            char_perk = 2
            char_screen_update()
        elif pressedkey is 'c':
            char_perk = 3
            char_screen_update()
        elif pressedkey is 'g':
            if char_class == 0 or char_race == 0 or char_perk == 0: 
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
    char_name = input("What is the name of the immortal god-king of the underworld?: ")


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


def screen_text_update(text_line_1 = '', text_line_2 = '', text_line_3 = '', text_line_4 = ''):
    os.system('clear')
    print(text_line_1)
    print(text_line_2)
    print(text_line_3)
    print(text_line_4)
    os.system('clear')
    print(text_line_1)
    print(text_line_2)
    print(text_line_3)
    print(text_line_4)


def display_enemy():
    is_running = False
    os.system('clear')
    print(centipede_sprite)
    print ("You lost 2 $$$")
    xdddd = input("Press enter")

    is_running = True


def lose_screen():
    is_running = False
    os.system('clear')
    print (lose_screen_sprite)
    exit()


def win_screen():
    is_running = False
    os.system('clear')
    print (win_screen_sprite)
    exit()


def sphinx_screen():
    is_running = False
    os.system('clear')
    guess_game()
    os.system('clear')


def show_inventory():
    pass


def show_legend():
    pass


def first_screen():
    screen_text_update()
    while is_first_screen == True:
        pressedkey = getch()


def gamemap():
    for i in range(1,len(room)+1):
        print (" ".join(room[i]))


def player_pos():
    for i in range(1,len(room)+1):
        if stuff['player'] in room[i]:
            x_axis = i
            y_axis = room[i].index(stuff['player'])
            global pos
            del pos[:]
            pos.append(x_axis)
            pos.append(y_axis)


def updater():
    os.system('clear')
    gamemap()
    player_pos()
    print (pos)


def check_colission(target_cell):
    global money
    global key

    if target_cell is stuff['money']:
        money += 1
    elif target_cell is stuff['chest']:
        random_num = random.randint(1,5)
        money += random_num
    elif target_cell is stuff['key']:
        key = True
    elif target_cell is stuff['sunglasses']:
        sunglasses = True
    elif target_cell is stuff['centipede']:
        money -= 2
        display_enemy()
    elif target_cell is stuff['sphinx']:
        sphinx_screen()


def update_board(ditcionary,inst_replace,inst_player, direction):
    (ditcionary[pos[0]]).pop(pos[1])
    (ditcionary[pos[0]]).insert(pos[1],inst_replace)
    (ditcionary[pos[0] + direction[0]]).pop(pos[1] + direction[1] )
    (ditcionary[pos[0] + direction[0]]).insert(pos[1] + direction[1],inst_player)


def check_room(map):
    global key
    global room
    if room == room1:
        del room
        room = room2
        key = False
        return room
    if room == room2:
        del room
        room = room3
        key = False
        return room
    if room == room3:
        del room
        room = room4
        key = False
        return room


def move(direction):
    global room
    target_cell = room[pos[0] + direction[0]][pos[1] + direction[1]]

    if target_cell is stuff['entrance'] and key == False:
        print("Entrance is locked")
    elif target_cell is stuff['entrance'] and key == True:
        room = check_room(room)
        updater()
    elif target_cell is not stuff['wall']:
        check_colission(target_cell)
        update_board(room,stuff['empty'], stuff['player'], direction)
        updater()


def display_enemy():
    is_running = False
    os.system('clear')
    print(centipede_sprite)
    print ("You lost 2 $$$")
    xdddd = input("Press enter")

    is_running = True


def lose_screen():
    is_running = False
    os.system('clear')
    print (lose_screen_sprite)
    exit()


def win_screen():
    is_running = False
    os.system('clear')
    print (win_screen_sprite)
    exit()


def sphinx_screen():
    is_running = False
    os.system('clear')
    guess_game()


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


room = {}



def room_randomizer():
    return str(random.randint(1, 5))

def chunk_merger():
    i = 1
    height = 30
    global room
    chunk_1 = import_room('chunk_left_' +room_randomizer())
    chunk_2 = import_room('chunk_mid_left_' +room_randomizer())
    chunk_3 = import_room('chunk_mid_right_' +room_randomizer())
    chunk_4 = import_room('chunk_right_' +room_randomizer())
    for row in range(height):
        room[i] = chunk_1[i]
        room[i] = room[i].extend(chunk_2[i])#.extend(chunk_3[i]).extend(chunk_4[i])
        i += 1
    return room


title_formatted = '%2000s' % '\n'+import_sprite('title_sprite')
room = chunk_merger()


def main():
#    char_name()
#    intro_screen_script()
#    char_screen()
#    player_character()
    updater()

if __name__ == "__main__":
    main()