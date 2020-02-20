
class Library(object):
    def __init__(self,books_list,signup,books_rate):
        self.books_list = books_list
        self.signup = signup
        self.books_rate = books_rate
    def __repr__(self):
        return f'Library : \nsignup {signup} \nbooks_rate {books_rate} \nbooks_list {books_list}'
    def __str__(self):
        return f'Library : \nsignup {signup} \nbooks_rate {books_rate} \nbooks_list {books_list}'


def parse_file(filename):
    with open(filename) as f:
        B,L,D = map(int,f.readline().strip().split())
        books_values = list(map(int,f.readline().strip().split()))
        libraries = []
        for l in range(L):
            n_books, signup, books_rate = map(int,f.readline().strip().split())
            books_list = list(map(int,f.readline().strip().split()))
            libraries.append(Library(books_list,signup,books_rate))
    return B,L,D,books_values,libraries
