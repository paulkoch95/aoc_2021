input = open("input_02.txt","r").read().splitlines() # load in data
horizontal = 0
depth = 0
for move in input:
    _inst, _inc = move.split(" ")
    if _inst == 'forward':
        horizontal+= int(_inc)
    elif _inst == 'down':
        depth+=int(_inc)
    elif _inst == 'up':
        depth-= int(_inc)

print(f'Challenge 1: Horizontal {horizontal} with depth {depth} produces {horizontal*depth}')

horizontal = 0
depth = 0
aim = 0
for move in input:
    _inst, _inc = move.split(" ")
    if _inst == 'forward':
        horizontal+= int(_inc)
        depth+= (aim*int(_inc))
    elif _inst == 'down':
        aim+=int(_inc)
    elif _inst == 'up':
        aim-= int(_inc)

print(f'Challenge 2: Horizontal {horizontal} with depth {depth} and aim {aim} produces {horizontal*depth}')
