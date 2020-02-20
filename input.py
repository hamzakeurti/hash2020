
class Library(object):
    def __init__(self,id,books,books_list,signup,books_rate):
        self.n_books = books
        self.books_list = books_list
        self.signup = signup
        self.books_rate = books_rate
        self.id = id
        self.selected_books = []
    def __repr__(self):
        return f'Library : id:{self.id} signup:{self.signup} books_rate:{self.books_rate} books_list:{self.books_list}'
    def __str__(self):
        return f'Library : id:{self.id} signup:{self.signup} books_rate:{self.books_rate} books_list:{self.books_list}'


def parse_file(filename):
    with open(filename) as f:
        B,L,D = map(int,f.readline().strip().split())
        books_values = list(map(int,f.readline().strip().split()))
        libraries = []
        for l in range(L):
            n_books, signup, books_rate = map(int,f.readline().strip().split())
            books_list = list(map(int,f.readline().strip().split()))
            libraries.append(Library(l,n_books,books_list,signup,books_rate))
    return B,L,D,books_values,libraries
