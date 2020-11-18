import os
import random

room = {}

def room_randomizer():
    return str(random.randint(1, 5))


def import_room(room_name, path = 'rooms/'):
    i = 1
    room_dict = {}
    room_x = []
    room_directory = path+room_name
    with open(room_directory) as room_read:
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

def gamemap(room):
    for i in range(1,len(room)+1):
        print (" ".join(room[i]))

if __name__ == "__main__":
    gamemap(chunk_merger())