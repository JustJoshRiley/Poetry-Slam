import random

def get_file_lines(filename):
    in_file = open(filename, "r")
    poem = in_file.readlines()
    return poem

def lines_printed_backwards(lines_list):
    total_lines = len(lines_list) 
    for line in reversed(lines_list):
        # print(f'{total_lines} {line}')
        total_lines -= 1

def lines_printed_random(lines_list):
    i = 0
    while i < len(lines_list):
        random_index = random.randint(0,42)
        print(lines_list[random_index])
        i += 1


file_lines = get_file_lines('poem.txt')

lines_printed_backwards(file_lines)

lines_printed_random(file_lines)