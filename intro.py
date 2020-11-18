#def char_screen_script():
#    is_first_screen = False
#    is_char_screen = True
#    os.system('clear')
#    empty_format = '[ ]'
#    exd_format = '[x]'
#
#    fill_format_1 = [exd_format, empty_format, empty_format, empty_format]
#    fill_format_2 = [exd_format, empty_format, empty_format, empty_format]
#    fill_format_3 = [exd_format, empty_format, empty_format, empty_format]
#
#    name_dict = {fill_format_1[0]:"Aleksey Alekseyevich Aleksyevinov", fill_format_1[1]:"Ampfschiffahrtsgesellschaftskapitän",fill_format_1[2]:"Plammogroundy",fill_format_1[3]:"Banskera"}
#    race_dict = {fill_format_2[0]:"Ogre", fill_format_1[1]:"Reptilian",fill_format_1[2]:"Star Child",fill_format_1[3]:"Snow Flake"}
#    console_dict = {fill_format_3[0]:"Philips Tele-Game", fill_format_1[1]:"Telejogo",fill_format_1[2]:"Intellivision",fill_format_1[3]:"CD-i"}
#
#    print('\033[0;30;42m Choose your name.\n{} Q - Aleksey Alekseyevich Aleksyevinov\n{} W - Donaudampfschiffahrtsgesellschaftskapitän\n{} E - Plammogroundy\n{} R - Banskera\n'.format(fill_format_1[0],fill_format_1[1],fill_format_1[2],fill_format_1[3]))
#    print('\033[0;30;42m Choose your race.\n{} A - Ogre\n{} S - Reptilian\n{} D - Star child\n{} F - Snow flake\n'.format(fill_format_2[0],fill_format_2[1],fill_format_2[2],fill_format_2[3]))
#    print('\033[0;30;42m Choose your favourite gaming console.\n{} Z - Philips Tele-Game\n{} X - Telejogo\n{} C - Intellivision\n{} V - CD-i\n'.format(fill_format_3[0],fill_format_3[1],fill_format_3[2],fill_format_3[3]))
#    
#    os.system('clear')
#    print('Choose your name.\n{} Q - Aleksey Alekseyevich Aleksyevinov\n{} W - Donaudampfschiffahrtsgesellschaftskapitän\n{} E - Plammogroundy\n{} R - Banskera\n'.format(fill_format_1[0],fill_format_1[1],fill_format_1[2],fill_format_1[3]))
#    print('Choose your race.\n{} A - Ogre\n{} S - Reptilian\n{} D - Star child\n{} F - Snow flake\n'.format(fill_format_2[0],fill_format_2[1],fill_format_2[2],fill_format_2[3]))
#    print('Choose your favourite gaming console.\n{} Z - Philips Tele-Game\n{} X - Telejogo\n{} C - Intellivision\n{} V - CD-i\n'.format(fill_format_3[0],fill_format_3[1],fill_format_3[2],fill_format_3[3]))
#    
#    while is_char_screen == True:
#        pressedkey = getch()
#
#        if pressedkey is 'q' or pressedkey is 'Q':
#            os.system('clear')
#            fill_format_1 = exd_format, empty_format, empty_format, empty_format
#            print('Choose your name.\n{} Q - Aleksey Alekseyevich Aleksyevinov\n{} W - Donaudampfschiffahrtsgesellschaftskapitän\n{} E - Plammogroundy\n{} R - Banskera\n'.format(fill_format_1[0],fill_format_1[1],fill_format_1[2],fill_format_1[3]))
#            print('Choose your race.\n{} A - Ogre\n{} S - Reptilian\n{} D - Star child\n{} F - Snow flake\n'.format(fill_format_2[0],fill_format_2[1],fill_format_2[2],fill_format_2[3]))
#            print('Choose your favourite gaming console.\n{} Z - Philips Tele-Game\n{} X - Telejogo\n{} C - Intellivision\n{} V - CD-i\n'.format(fill_format_3[0],fill_format_3[1],fill_format_3[2],fill_format_3[3]))
#        elif pressedkey is 'w' or pressedkey is 'W':
#            os.system('clear')
#            fill_format_1 = empty_format, exd_format, empty_format, empty_format
#            print('Choose your name.\n{} Q - Aleksey Alekseyevich Aleksyevinov\n{} W - Donaudampfschiffahrtsgesellschaftskapitän\n{} E - Plammogroundy\n{} R - Banskera\n'.format(fill_format_1[0],fill_format_1[1],fill_format_1[2],fill_format_1[3]))
#            print('Choose your race.\n{} A - Ogre\n{} S - Reptilian\n{} D - Star child\n{} F - Snow flake\n'.format(fill_format_2[0],fill_format_2[1],fill_format_2[2],fill_format_2[3]))
#            print('Choose your favourite gaming console.\n{} Z - Philips Tele-Game\n{} X - Telejogo\n{} C - Intellivision\n{} V - CD-i\n'.format(fill_format_3[0],fill_format_3[1],fill_format_3[2],fill_format_3[3]))
#        elif pressedkey is 'e' or pressedkey is 'E':
#            fill_format_1 = empty_format, empty_format, exd_format, empty_format
#            os.system('clear')
#            print('Choose your name.\n{} Q - Aleksey Alekseyevich Aleksyevinov\n{} W - Donaudampfschiffahrtsgesellschaftskapitän\n{} E - Plammogroundy\n{} R - Banskera\n'.format(fill_format_1[0],fill_format_1[1],fill_format_1[2],fill_format_1[3]))
#            print('Choose your race.\n{} A - Ogre\n{} S - Reptilian\n{} D - Star child\n{} F - Snow flake\n'.format(fill_format_2[0],fill_format_2[1],fill_format_2[2],fill_format_2[3]))
#            print('Choose your favourite gaming console.\n{} Z - Philips Tele-Game\n{} X - Telejogo\n{} C - Intellivision\n{} V - CD-i\n'.format(fill_format_3[0],fill_format_3[1],fill_format_3[2],fill_format_3[3]))
#        elif pressedkey is 'r' or pressedkey is 'R':
#            fill_format_1 = empty_format, empty_format, empty_format, exd_format
#            os.system('clear')
#            print('Choose your name.\n{} Q - Aleksey Alekseyevich Aleksyevinov\n{} W - Donaudampfschiffahrtsgesellschaftskapitän\n{} E - Plammogroundy\n{} R - Banskera\n'.format(fill_format_1[0],fill_format_1[1],fill_format_1[2],fill_format_1[3]))
#            print('Choose your race.\n{} A - Ogre\n{} S - Reptilian\n{} D - Star child\n{} F - Snow flake\n'.format(fill_format_2[0],fill_format_2[1],fill_format_2[2],fill_format_2[3]))
#            print('Choose your favourite gaming console.\n{} Z - Philips Tele-Game\n{} X - Telejogo\n{} C - Intellivision\n{} V - CD-i\n'.format(fill_format_3[0],fill_format_3[1],fill_format_3[2],fill_format_3[3]))
#        elif pressedkey is 'a' or pressedkey is 'A':
#            fill_format_2 = exd_format, empty_format, empty_format, empty_format
#            os.system('clear')
#            print('Choose your name.\n{} Q - Aleksey Alekseyevich Aleksyevinov\n{} W - Donaudampfschiffahrtsgesellschaftskapitän\n{} E - Plammogroundy\n{} R - Banskera\n'.format(fill_format_1[0],fill_format_1[1],fill_format_1[2],fill_format_1[3]))
#            print('Choose your race.\n{} A - Ogre\n{} S - Reptilian\n{} D - Star child\n{} F - Snow flake\n'.format(fill_format_2[0],fill_format_2[1],fill_format_2[2],fill_format_2[3]))
#            print('Choose your favourite gaming console.\n{} Z - Philips Tele-Game\n{} X - Telejogo\n{} C - Intellivision\n{} V - CD-i\n'.format(fill_format_3[0],fill_format_3[1],fill_format_3[2],fill_format_3[3]))
#        elif pressedkey is 's' or pressedkey is 'S':
#            fill_format_2 = empty_format, exd_format, empty_format, empty_format
#            os.system('clear')
#            print('Choose your name.\n{} Q - Aleksey Alekseyevich Aleksyevinov\n{} W - Donaudampfschiffahrtsgesellschaftskapitän\n{} E - Plammogroundy\n{} R - Banskera\n'.format(fill_format_1[0],fill_format_1[1],fill_format_1[2],fill_format_1[3]))
#            print('Choose your race.\n{} A - Ogre\n{} S - Reptilian\n{} D - Star child\n{} F - Snow flake\n'.format(fill_format_2[0],fill_format_2[1],fill_format_2[2],fill_format_2[3]))
#            print('Choose your favourite gaming console.\n{} Z - Philips Tele-Game\n{} X - Telejogo\n{} C - Intellivision\n{} V - CD-i\n'.format(fill_format_3[0],fill_format_3[1],fill_format_3[2],fill_format_3[3]))
#        elif pressedkey is 'd' or pressedkey is 'D':
#            fill_format_2 = empty_format, empty_format, exd_format, empty_format
#            os.system('clear')
#            print('Choose your name.\n{} Q - Aleksey Alekseyevich Aleksyevinov\n{} W - Donaudampfschiffahrtsgesellschaftskapitän\n{} E - Plammogroundy\n{} R - Banskera\n'.format(fill_format_1[0],fill_format_1[1],fill_format_1[2],fill_format_1[3]))
#            print('Choose your race.\n{} A - Ogre\n{} S - Reptilian\n{} D - Star child\n{} F - Snow flake\n'.format(fill_format_2[0],fill_format_2[1],fill_format_2[2],fill_format_2[3]))
#            print('Choose your favourite gaming console.\n{} Z - Philips Tele-Game\n{} X - Telejogo\n{} C - Intellivision\n{} V - CD-i\n'.format(fill_format_3[0],fill_format_3[1],fill_format_3[2],fill_format_3[3]))
#        elif pressedkey is 'f' or pressedkey is 'F':
#            fill_format_2 = empty_format, empty_format, empty_format, exd_format
#            os.system('clear')
#            print('Choose your name.\n{} Q - Aleksey Alekseyevich Aleksyevinov\n{} W - Donaudampfschiffahrtsgesellschaftskapitän\n{} E - Plammogroundy\n{} R - Banskera\n'.format(fill_format_1[0],fill_format_1[1],fill_format_1[2],fill_format_1[3]))
#            print('Choose your race.\n{} A - Ogre\n{} S - Reptilian\n{} D - Star child\n{} F - Snow flake\n'.format(fill_format_2[0],fill_format_2[1],fill_format_2[2],fill_format_2[3]))
#            print('Choose your favourite gaming console.\n{} Z - Philips Tele-Game\n{} X - Telejogo\n{} C - Intellivision\n{} V - CD-i\n'.format(fill_format_3[0],fill_format_3[1],fill_format_3[2],fill_format_3[3]))
#        elif pressedkey is 'z' or pressedkey is 'Z':
#            fill_format_3 = exd_format, empty_format, empty_format, empty_format
#            os.system('clear')
#            print('Choose your name.\n{} Q - Aleksey Alekseyevich Aleksyevinov\n{} W - Donaudampfschiffahrtsgesellschaftskapitän\n{} E - Plammogroundy\n{} R - Banskera\n'.format(fill_format_1[0],fill_format_1[1],fill_format_1[2],fill_format_1[3]))
#            print('Choose your race.\n{} A - Ogre\n{} S - Reptilian\n{} D - Star child\n{} F - Snow flake\n'.format(fill_format_2[0],fill_format_2[1],fill_format_2[2],fill_format_2[3]))
#            print('Choose your favourite gaming console.\n{} Z - Philips Tele-Game\n{} X - Telejogo\n{} C - Intellivision\n{} V - CD-i\n'.format(fill_format_3[0],fill_format_3[1],fill_format_3[2],fill_format_3[3]))
#        elif pressedkey is 'x' or pressedkey is 'X':
#            fill_format_3 = empty_format, exd_format, empty_format, empty_format
#            os.system('clear')
#            print('Choose your name.\n{} Q - Aleksey Alekseyevich Aleksyevinov\n{} W - Donaudampfschiffahrtsgesellschaftskapitän\n{} E - Plammogroundy\n{} R - Banskera\n'.format(fill_format_1[0],fill_format_1[1],fill_format_1[2],fill_format_1[3]))
#            print('Choose your race.\n{} A - Ogre\n{} S - Reptilian\n{} D - Star child\n{} F - Snow flake\n'.format(fill_format_2[0],fill_format_2[1],fill_format_2[2],fill_format_2[3]))
#            print('Choose your favourite gaming console.\n{} Z - Philips Tele-Game\n{} X - Telejogo\n{} C - Intellivision\n{} V - CD-i\n'.format(fill_format_3[0],fill_format_3[1],fill_format_3[2],fill_format_3[3]))
#        elif pressedkey is 'c' or pressedkey is 'C':
#            fill_format_3 = empty_format, empty_format, exd_format, empty_format
#            os.system('clear')
#            print('Choose your name.\n{} Q - Aleksey Alekseyevich Aleksyevinov\n{} W - Donaudampfschiffahrtsgesellschaftskapitän\n{} E - Plammogroundy\n{} R - Banskera\n'.format(fill_format_1[0],fill_format_1[1],fill_format_1[2],fill_format_1[3]))
#            print('Choose your race.\n{} A - Ogre\n{} S - Reptilian\n{} D - Star child\n{} F - Snow flake\n'.format(fill_format_2[0],fill_format_2[1],fill_format_2[2],fill_format_2[3]))
#            print('Choose your favourite gaming console.\n{} Z - Philips Tele-Game\n{} X - Telejogo\n{} C - Intellivision\n{} V - CD-i\n'.format(fill_format_3[0],fill_format_3[1],fill_format_3[2],fill_format_3[3]))
#        elif pressedkey is 'v' or pressedkey is 'V':
#            fill_format_3 = empty_format, empty_format, empty_format, exd_format
#            os.system('clear')
#            print('Choose your name.\n{} Q - Aleksey Alekseyevich Aleksyevinov\n{} W - Donaudampfschiffahrtsgesellschaftskapitän\n{} E - Plammogroundy\n{} R - Banskera\n'.format(fill_format_1[0],fill_format_1[1],fill_format_1[2],fill_format_1[3]))
#            print('Choose your race.\n{} A - Ogre\n{} S - Reptilian\n{} D - Star child\n{} F - Snow flake\n'.format(fill_format_2[0],fill_format_2[1],fill_format_2[2],fill_format_2[3]))
#            print('Choose your favourite gaming console.\n{} Z - Philips Tele-Game\n{} X - Telejogo\n{} C - Intellivision\n{} V - CD-i\n'.format(fill_format_3[0],fill_format_3[1],fill_format_3[2],fill_format_3[3]))
#        elif pressedkey is 'y' or pressedkey is 'Y':
#            is_char_screen = False
#            os.system('clear')
#            name = name_dict.get('[x]', "none")
#            race = race_dict.get('[x]', "none")
#            console = console_dict.get('[x]', "none")
#            return [name, race, console]
#        elif pressedkey is 'l' or pressedkey is 'L':
#            os.system('clear')
#            print('Goodbye')
#            exit()


def skip_intro_2():
    pass


def intro_screen_script2():
    is_intro_screen2 = True
#    name = char_screen_script()[0]
#    race = char_screen_script()[1]
#    console = char_screen_script()[2]
    name = 'Shrek'
    race = 'Ogre'
    console = 'Onion'
    os.system('reset')
    print("\33[1;33;48m                                                                Press a to continue \n\n\n\n\n")
    print("\33[1;33;48m Your name is", name)
    print("\33[1;33;48m You are a", race)
    print("\33[1;33;48m You would spend all day playing", console)
    os.system('clear')
    print("\033[1;33;48m                                                                Press a to continue \n\n\n\n\n")
    print(slide_list1[5], name, slide_list1[7])
    os.system('clear')
    print("\033[1;33;48m                                                                Press a to continue \n\n\n\n\n")
    first_line = str(slide_list2[0])+ name+ str(slide_list2[2])
    second_line = str(slide_list2[3])+ name+ str(slide_list2[5])
    third_life = str(slide_list2[6])+'\n'+ str(slide_list2[7])+ name+ str(slide_list2[9])
    fourth_line = str(slide_list2[10])+ name+ str(slide_list2[12])
    lines_to_print = [fourth_line, second_line, third_life, first_line]
    which_line_to_print = -1
    sprites_to_print = [crown_sprite, lvlup_sprite, reptilian_sprite, house_sprite]
    
    while is_intro_screen2 == True:
        pressedkey = getch()
        os.system('clear')
        print("\033[1;33;48m                                                                Press a to continue \n\n\n\n\n")
        os.system('clear')
        print("\033[1;33;48m                                                                Press a to continue \n\n\n\n\n")
        if pressedkey is 'l' or pressedkey is 'L':
            os.system('clear')
            print('Goodbye')
            exit()
        elif pressedkey is 'a' or pressedkey is 'A':
            os.system('clear')
            if which_line_to_print == 3:
                os.system('clear')
                print('\033[1;30;42m a')
                os.system('clear')
                print('\033[1;30;42m a')
                is_intro_screen2 = False
            print("\033[1;33;48m                                                                Press a to continue \n\n\n\n\n")
            print(lines_to_print[which_line_to_print])
            print('\n')
            print(sprites_to_print[which_line_to_print])
            which_line_to_print += 1


def import_sprite(sprite_name, how_far = 0, path = 'sprites/'):
    spaced_sprite = ''
    file_name = path + sprite_name
    spaces = how_far * ' '
    with open(file_name) as sprite_read:
        sprite_name = sprite_read.readlines()
        for each_line in sprite_name:
            new_line = (spaces)+each_line
            spaced_sprite += new_line
        return spaced_sprite


print(import_sprite('bambi_sprite', 50))
