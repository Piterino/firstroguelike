COLOR_GREEN = "\033[1;32;40m "
NOMRAL_TEXT = "\033[0;37;40m "
print('Janusz'+ COLOR_GREEN+'Janusz'+(NOMRAL_TEXT+'Janusz').strip())

color = {
    'green' : "\033[1;32;40m",
    'normal' : "\033[0;37;40m",
    'red' : "\033[1;31;40m"
}

print(color['green']+ "#"+ color['normal']+ '@'+ color['green']+ "#")
print(color['green']+ "#"+ color['normal']+ '@'+ color['green']+ "#")
print(color['green']+ "#"+ color['normal']+ '@'+ color['green']+ "#")
