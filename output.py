def evaluate_solution(D,A,libraries_list,books_val):
    scanned_books = set()
    signup_day = []
    d = 0
    for l in range(A):
        d = d+libraries_list[l].signup
        # if we vannot signup all selected libraries solution is 0
        if d>D:
            return 0
        signup_day.append(d)
    # send books (=value)
    for l in range(A):
        number_books = min((D - signup_day[l])*libraries_list[l].book_rate, libraries_list[l].books)
        for book in range(number_books):
            scanned_books.add(book)

    return sum(list(map(books_val.__getitem__,scanned_books)))    



        
        
        

def write_solution(solution,filename):
    with open(filename,"w") as f:
        f.write(solution)