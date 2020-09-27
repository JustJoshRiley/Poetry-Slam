import random

#Question 1
def get_file_lines(filename):
    in_file = open(filename, "r")
    poem = in_file.readlines()
    return poem

#Question 2
def lines_printed_backwards(lines_list):
    total_lines = len(lines_list) 
    for line in reversed(lines_list):
        print(f'{total_lines} {line}')
        total_lines -= 1

# Question 3
def lines_printed_random(lines_list):
    i = 0
    while i <= len(lines_list):
        random_index = random.randint(0,42)
        print(lines_list[random_index])
        i += 1

#Question 4
def lines_printed_custom(lines_list):
    # skip lines prints every 2nd line from the 0th index:
    i = 0
    for line in lines_list:
        if i % 2 == 0:
            print(line)
        i += 1

#Stretch Challenge::: Make menu for options on how to see poems
user_request = int(input("Choose 1, 2, 3, or 4. \n 1: Print Poem Backwards\n 2: Print Poem Random \n 3: Print Poem With Skipped Lines \n 4: Exit Program::  \n Answer Here ---> "))

#Question 1
file_lines = get_file_lines('poem.txt')

if user_request == 1 or user_request == '1':
    #Question 2
    lines_printed_backwards(file_lines)
elif user_request == 2 or user_request == '2':
    #Question 3
    lines_printed_random(file_lines)
elif user_request == 3 or user_request == '3':
    #Question 4
    lines_printed_custom(file_lines)
elif user_request == 4 or user_request == '4':
    exit()