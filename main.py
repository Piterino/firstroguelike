import os
import random
import platform
from sprites import *
#from hotcold import *
from display import *
#from map_gen import *
from char import *

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

def pressedkey():
    return getch()

#DATA

stuff  = {
    'wall'     :  "#",
    'player'   :  "@",
    'empty'    :  " ",
    'money'    :  "$",
    'weapon'   :  "W",
    'armor'    :  "A",
    'entrance' :  "0",
    'first aid':  "+",
    'key'      :  "K",
    'sunglasses': "B",
    'mushroom' :  "?"
}

enemy_stuff = {
    'bambi'    :  "b",
    'sanic'    :  "&",
    'sphinx'   :  "^",
    'centipede':  "S",
    'owl'      :  "%",
    'gorilla'  :  "G",
    'yeet'     :  "Y"
}

enemy_objects = {
    "b" : 'bambi',
    "&" : 'sanic',   
    "^" : 'sphinx',   
    "S" : 'centipede',
    "%" : 'owl',
    "G" : 'gorilla',  
    "Y" : 'yeet'
}

weapons = {'Headbutt' : 1,
           'Spoiled Yoghurt' : 2,
           'Enchanted Serwer Pipe' : 3,
           'Moonlight Sword' : 4
}

armors = {'Used Underwear' : 0,
         'Aluminium Foil Hat' : 1,
         'Ghost Rider Jacket' : 2,
         'Nerf Vest' : 3
}

#MAP

def change_screen_color():
    os.system('clear')
    COLOR_GREEN = "\033[1;32;40m "
    print(COLOR_GREEN+'color swap')
    print(COLOR_GREEN+'color swap')
    print(COLOR_GREEN+'color swap')
    os.system('clear')
    print(COLOR_GREEN+'color swap')
    print(COLOR_GREEN+'color swap')
    print(COLOR_GREEN+'color swap')
    os.system('clear')

def gamemap(room):
    for i in range(1,len(room)+1):
        print (" ".join(room[i]))

def updater(room):
    os.system('clear')
    gamemap(room)
    player_pos()
    print(f"HP: {player['current hp']} / {player['limit hp']}")
    print(f"$: {money}")

def check_room(room, room_number, dungeon_mode = False):
    global room_num
    room_num +=1
    room = import_room(f"room_{room_num}")
    if dungeon_mode == True:
        return chunk_merger()
    return room

#MAP GENERATOR
def room_randomizer():
    return str(random.randint(1, 5))


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

def chunk_merger():
    i = 1
    height = 30
    chunk_1 = import_room('chunk_left_' +room_randomizer())
    chunk_2 = import_room('chunk_mid_left_' +room_randomizer())
    chunk_3 = import_room('chunk_mid_right_' +room_randomizer())
    chunk_4 = import_room('chunk_right_' +room_randomizer())
    for row in range(height):
        room[i] = chunk_1[i]
        room[i].extend(chunk_2[i])
        room[i].extend(chunk_3[i])
        room[i].extend(chunk_4[i])
        i += 1
    return room

#COMBAT SYSTEM

enemies = {
'centipede' : {
    'hp' : 5,
    'dmg': 1,
    'start chance': 20
},
'owl' :{
    'hp' : 7,
    'dmg': 2,
    'start chance': 50
},
'yeet' : {
    'hp' : 22,
    'dmg': 2,
    'start chance': 30
},
'gorilla' : {
    'hp' : 25,
    'dmg': 3,
    'start chance': 20
},
'bambi' : {
    'hp' : 32,
    'dmg': 4,
    'start chance': 80
},
'sanic' : {
    'hp' : 25,
    'dmg': 6,
    'start chance': 100
}
}

attacks = {
    'Quick attack' : {
        'damage multiplier' : 1,
        'crit chance' : 10,
        'stamina cost': 10
    },
    'Normal attack': { 
        'damage multiplier' : 1, 
        'crit chance' : 30,
        'stamina cost': 20
    },
    'Power attack' : {
        'damage multiplier' : 2,
        'crit chance' : 60,
        'stamina cost': 40
    }
}
attack_options = {
    '0' : 'Wait',
    '1' : 'Quick attack',
    '2' : 'Normal attack',
    '3' : 'Power attack'
}

def start_combat(enemy, enemy_sprite, player):
    stamina = 100
    STAMINA_LIMIT = 100
    current_enemy_hp = enemy['hp']
    display_enemy(enemy_sprite)
    damage = player['base damage'] + weapons[player['weapon_name']]
    print(damage)
    if is_critical(enemy['start chance']) == True:
        player['current hp'] = deal_damage_to_player(enemy, player)
    while player['current hp'] > 0:
        display_combat_stats(enemy, current_enemy_hp, enemy_sprite, player, stamina)
        pressedkey = getch()
        if pressedkey == '0':
            print("You feel more rested")
            stamina += 30
        elif pressedkey in attack_options and stamina - attacks[attack_options[pressedkey]]['stamina cost'] >= 0:
            stamina = spend_stamina(stamina, attacks[attack_options[pressedkey]])
            current_enemy_hp = deal_damage_to_enemy(current_enemy_hp, attacks[attack_options[pressedkey]])
        else:
            print("You tried to inflict damage but you failed.")

        if stamina > STAMINA_LIMIT:
            stamina = STAMINA_LIMIT

        if current_enemy_hp <= 0:
            print("\n>>YOU ARE VICTORIOUS!<<\n")
            input("[Press Enter]")
            return player['current hp']

        player['current hp'] = deal_damage_to_player(enemy, player)
    
    return player['current hp']

def deal_damage_to_enemy(enemy_hp, attack_type):
    base_attack_damage = attack_type['damage multiplier']*(player['base damage'] + weapons[player['weapon_name']])
    if is_critical(attack_type['crit chance']) == True:
        print("Critical Damage!")
        print(f"You attacked for {base_attack_damage*player['crit multiplier']} damage!")
        enemy_hp -= base_attack_damage*player['crit multiplier']
    else:
        print(f"You attacked for {base_attack_damage} damage!")
        enemy_hp -= base_attack_damage
    return enemy_hp

def deal_damage_to_player(enemy, player):
    output_hp = player['current hp']
    if  player['base armor'] + armors[player['armor_name']] - enemy['dmg'] < 0:
        print(f"Enemy attacks you for {enemy['dmg'] - (player['base armor'] + armors[player['armor_name']])} damage")
        output_hp -= (enemy['dmg'] - (player['base armor'] + armors[player['armor_name']]))
        input("[Press Enter]")
        return output_hp
    else:
        print("Enemy can't penetrate your armor! You feel strong.")
        input("[Press Enter]")
        return output_hp

def display_combat_stats(enemy, enemy_hp, enemy_sprite, player, player_stamina):
    display_enemy(enemy_sprite)
    print(f" {display_bar(enemy_hp)}")
    print(f"ENEMY HP: {enemy_hp}\n")
    print("Player:")
    print(f" {display_bar(player['current hp'])}")
    print(f"HP: {player['current hp']} / {player['limit hp']}")
    print(f"Armor Points: {player['base armor'] + armors[player['armor_name']]}")
    print(f"Stamina: {player_stamina}\n")
    print(f"0. Wait (+ 30 stamina)")
    print(f"1. Quick attack {attacks['Quick attack']['damage multiplier']*(player['base damage'] + weapons[player['weapon_name']])} damage (-10 stamina, 10% crit chance)")
    print(f"2. Normal attack {attacks['Normal attack']['damage multiplier']*(player['base damage'] + weapons[player['weapon_name']])} damage (-20 stamina, 30% crit chance)")
    print(f"3. Power attack {attacks['Power attack']['damage multiplier']*(player['base damage'] + weapons[player['weapon_name']])} damage (-40 stamina, 60% crit chance)")
    print(f"\nFIGHT!")

def spend_stamina(player_stamina, attack_type):
    return player_stamina - attack_type['stamina cost']
    
def is_critical(chance):
    random_num = random.randint(1, 100)
    if random_num < chance:
        return True
    else:
        return False

#INVENTORY

def display_player_inventory():
    os.system('clear')
    print(f"Armor: {player['armor_name']} [DEF: +{armors[player['armor_name']]}]")
    print(f"Weapon: {player['weapon_name']} [DMG: +{weapons[player['weapon_name']]}]")
    print("\nPlayer stats:\n")
    print(f"HP: {player['current hp']} / {player['limit hp']}")
    print(f"DMG: {weapons[player['weapon_name']] + player['base damage']}")
    print(f"Base Armor: {player['base armor']}")
    print(f"Armor Points: {armors[player['armor_name']] + player['base armor']}")
    print("\n[Move to close inventory]\n")
    show_legend()

def get_armor():
    os.system('clear')
    random_armor = random.choice(list(armors.keys()))
    print(f"You found {random_armor} [DEF: +{armors[random_armor]}]\n")
    print(f"Do you want to switch from {player['armor_name']} [DEF: +{armors[player['armor_name']]}] ?\n")
    print("\n1. Yes please.")
    print("2. What kind of junk is this?")
    while True:
        pressedkey = getch().lower()
        if pressedkey == "1":
            os.system('clear')
            print(f"You are wearing {random_armor}")
            input("[Press Enter]")
            player['armor_name'] = random_armor
            return player
        elif pressedkey == "2":
            return player
        else:
            pass


def get_weapon():
    os.system('clear')
    random_weapon = random.choice(list(weapons.keys()))
    print(f"You found {random_weapon} [DMG: +{weapons[random_weapon]}]\n")
    print(f"Do you want to switch from {player['weapon_name']} [DMG: {weapons[player['weapon_name']]}] ?")
    print("\n1. Yes please.")
    print("2. What kind of junk is this?")
    while True:
        pressedkey = getch().lower()
        if pressedkey == "1":
            os.system('clear')
            print(f"You are wearing {random_weapon}")
            input("[Press Enter]")
            player['weapon_name'] = random_weapon
            return player
        elif pressedkey == "2":
            return player
        else:
            pass

#MOVEMENT AND COLISION

pos = []
room = import_room("room_1")

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

def player_pos():
    for i in range(1,len(room)):
        if stuff['player'] in room[i]:
            x_axis = i
            y_axis = room[i].index(stuff['player'])
            global pos
            del pos[:]
            pos.append(x_axis)
            pos.append(y_axis)

def check_colission(target_cell, player_dict):
    global money
    global key
    global player
    global enemies

    if target_cell is stuff['first aid']:
        player['current hp'] = player['limit hp']
    elif target_cell is stuff['money']:
        money += 1
    elif target_cell is stuff['armor']:
        player = get_armor()
    elif target_cell is stuff['weapon']:
        player = get_weapon()
    elif target_cell is stuff['key']:
        key = True
    elif target_cell is stuff['sunglasses']:
        sunglasses = True
    elif target_cell in enemy_objects and target_cell is enemy_stuff['sphinx']:
        sphinx_screen()
    elif target_cell in enemy_objects:
        player['current hp'] = start_combat(enemies[enemy_objects[target_cell]], import_sprite(f"{enemy_objects[target_cell]}_sprite"), player)
        

def update_board(ditcionary,inst_replace,inst_player, direction):
    (ditcionary[pos[0]]).pop(pos[1])
    (ditcionary[pos[0]]).insert(pos[1],inst_replace)
    (ditcionary[pos[0] + direction[0]]).pop(pos[1] + direction[1] )
    (ditcionary[pos[0] + direction[0]]).insert(pos[1] + direction[1],inst_player)

def move(direction):
    global room
    global player
    target_cell = room[pos[0] + direction[0]][pos[1] + direction[1]]

    if target_cell is stuff['entrance'] and key == False:
        print("Entrance is locked")
    elif target_cell is stuff['entrance'] and key == True:
        room = check_room(room, room_num, dungeon_mode)
        updater(room)
    elif target_cell is not stuff['wall']:
        check_colission(target_cell, player)
        update_board(room,stuff['empty'], stuff['player'], direction)
        updater(room)

#MAIN
dungeon_mode = False
is_running_chose = True
while is_running_chose == True:
    os.system('clear')  
    print(import_sprite("adventure_mode_sprite"))
    print(import_sprite("dungeon_mode_sprite"))
    print("[Choose Mode]")
    pressedkey = getch()
    if pressedkey == '1':
        room = import_room('room_1')
        is_running_chose = False
    elif pressedkey == '2':
        room = chunk_merger()
        dungeon_mode = True
        is_running_chose = False

player = display()
change_screen_color()

room_num = 1
key = False
sunglasses = False

updater(room)

is_running = True
while is_running == True:
    pressedkey = getch().lower()
    if pressedkey in directions:
        move(directions[pressedkey])
    elif pressedkey == 'l':
        leave_game()
    elif pressedkey == 'i':
        display_player_inventory()

    if player['current hp'] <= 0:
        lose_screen()