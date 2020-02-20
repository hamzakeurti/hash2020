

def Library_Score(Library,previous_libraries,D,current_D):
    book_potential = 0
    for book in Library.books_list:
        book_potential += previous_libraries.get(book,1)
    return Library.books_rate*(D-current_D - Library.signup) * book_potential


