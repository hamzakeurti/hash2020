from input import Library


def library_score(library,previous_libraries,D,current_D,books_values):
    book_potential = 0

    for book in library.books_list:
        book_potential += previous_libraries.get(book,books_values[book])

    return library.books_rate*(D - current_D - library.signup) * book_potential


def greedy_algo(D,libraries,books_values):
    current_D = 0
    previous_libraries = {}
    selected_libraries = []

    while current_D<D:
        best_score = -1

        for library in libraries:
            lib_score = library_score(library,previous_libraries,D,current_D,books_values)
            if lib_score > best_score:
                best_score = lib_score
                best_library = library

        current_D += best_library.signup

        if current_D>=D:
            break

        for book in library.books_list:
            previous_libraries[book] = 0
            
        selected_libraries.append(best_library)
        libraries.remove(best_library)

    current_D = 0
    for library in selected_libraries:
        current_D += library.signup
        possible_books = (D-current_D) * library.books_rate
        library.selected_books = sorted(library.books_list,key=lambda x: books_values[x])[:min(possible_books,len(library.books_list)-1)]

    return selected_libraries


