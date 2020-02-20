def evaluate_solution(D,selected_libraries,books_val):
    A = len(selected_libraries)
    scanned_books = set()
    signup_day = []
    d = 0
    for l in range(A):
        d = d+selected_libraries[l].signup
        # if we vannot signup all selected libraries solution is 0
        if d>D:
            return 0
        signup_day.append(d)
    # send books (=value)
    for l in range(A):
        number_books = min((D - signup_day[l])*selected_libraries[l].books_rate, selected_libraries[l].n_books)
        for book in range(number_books):
            scanned_books.add(book)

    return sum(list(map(books_val.__getitem__,scanned_books)))    



        
        
        

def write_solution(solution,filename):
    with open(filename,"w") as f:
        f.write(solution)