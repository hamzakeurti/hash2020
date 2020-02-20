
class Library(object):
    def __init__(self,books_list,signup,books_rate):
        self.books_list = books_list
        self.signup = signup
        self.books_rate = books_rate



def parse_file(filename):
    f = open(filename)
    B,L,D = map(int,f.readline().strip().split())
    books_values = list(map(int,f.readline().strip().split()))
    libraries = []
    for l in range(L):
        n_books, signup, books_rate = map(int,f.readline().strip().split())
        books_list = list(map(int,f.readline().strip().split()))
        libraries.append(Library(books_list,signup,books_rate))
    return B,L,D,books_values,libraries
