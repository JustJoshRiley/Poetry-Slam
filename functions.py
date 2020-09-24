filename = "poem.txt"

def get_file_lines(filename):
    in_file = open(filename, "r")
    poem = in_file.read()
    print(poem)



get_file_lines(filename)