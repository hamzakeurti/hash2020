import os.path as path
import input,output,algos
from collections import defaultdict
INPUT_DIR = "inputs"
INPUT_FILE = "___"

OUTPUT_DIR = "outputs"
OUTPUT_FILE = "solution"


# input
filename = path.join(INPUT_DIR,INPUT_FILE)
B,L,D,books_values,libraries = input.parse_file(filename)


# algo
# Finding greedily a sequence of libraries based on number of books that are not already in the previous libraries
current_D = 0
previous_libraries = defaultdict(int)
best_score = -1

for library in libraries:
    library_score = algos.Library_score(Library,previous_libraries,D,current_D)
    if library_score > best_score:
        best_score = library_score
        best_library = library

current_D += best_library.signup

for book in library.books_list:
    previous_libraries[book] = 0
libraries.remove(best_library)

# output
