import os.path as path
import input,output,algos
from collections import defaultdict
INPUT_DIR = "inputs"
INPUT_FILE = "e_so_many_books.txt"

OUTPUT_DIR = "outputs"
OUTPUT_FILE = "e_so_many_books.txt"


# input
filename = path.join(INPUT_DIR,INPUT_FILE)
B,L,D,books_values,libraries = input.parse_file(filename)


# algo
selected_libraries = algos.greedy_algo(D,libraries,books_values)
print(output.evaluate_solution(D,selected_libraries,books_values))

# output
output.make_submission(selected_libraries,path.join(OUTPUT_DIR,OUTPUT_FILE))
