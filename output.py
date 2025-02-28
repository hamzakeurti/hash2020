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



        
        
def make_submission(selected_libraries):
    submission_txt = ""
    A = len(selected_libraries)
    submission_txt += str(A) + "\n"
    for library in selected_libraries:
        submission_txt += " ".join(map(str,[library.id,len(library.selected_books)])) + "\n"
        submission_txt += " ".join(map(str,library.selected_books)) + "\n"
    return submission_txt

def write_file(selected_libraries,filename):
        
    with open(filename,"w") as f:
        f.write(make_submission(selected_libraries))

        
    
