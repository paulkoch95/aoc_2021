# Advent of Code Day 1 - 2021
# Author: Paul Koch
#   input = open("day_01/test_input.txt","r").read().splitlines() # load in data
input = open("day_01/input_01.txt","r").read().splitlines() # load in data
input = [int(x) for x in input]                             # parsing to avoid calling int() multiple times
inc, dec = 0,0

for idx, s in enumerate(input):
    if idx>0:
        if s > input[idx-1]:
            inc+=1
print(f'Task1: Incremented {inc} times!')

last_sum = 0
inc = 0
for idx, s in enumerate(input[1:]):
    _sum = sum(input[idx-1:idx+2])
    if _sum > last_sum & last_sum > 0:
        inc+=1
    last_sum = _sum
print(f'Task2: Incremented {inc} times!')

