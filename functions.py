import random

def get_file_lines(filename):
    in_file = open(filename, "r")
    poem = in_file.readlines()
    # print(poem)
    return poem

def lines_printed_backwards(lines_list):
    # get_file_lines('poem.txt')
    total_lines = len(lines_list) 
    for line in reversed(lines_list):
        print(f'{total_lines} {line}')
        total_lines -= 1

def lines_printed_random(lines_list):
    for line in lines_list:
        print(line)




file_lines = get_file_lines('poem.txt')
lines_printed_backwards(file_lines)
lines_printed_backwards