# Docstring this

        
"""Sample code, nothing  important
Per = Book("Per", "People")
Go = Book("Go", "Soup")
Fof = Book("Fof", "f")
gee = Book("gee", "h")
BookList = [Per, Go, Fof, gee]"""
# put patron and book inside here
class Book(object):
    def __init__(self, title, author):
        """Nobody is originally a Patron or on the Wait List"""
        self.title = title
        self.author = author
        self.patron = []
        self.waitlist = {}
    def __str__(self):
        return str(self.__dict__)
    #Ensures that other objects with the same information are counted as the same
    def __eq__(self, other):
        return (self.__dict__ == other.__dict__)
    def addPatron(self, patron):
        """assigns a book to a patron, but if
                    there is a patron that already exists,
                    assigns someone to the waitlist"""
        if len(self.patron) >= 1:
            BookID = 0
            BookID += 1
            self.waitlist[BookID] = patron
            return patron
        else:
            return self.patron.append(patron)
    #def __repr__(self):
     #   """failsafe to return all information"""
      #  return str(self)
    def getPatron(self):
        """gets the current holder of the book"""
        if len(self.patron) >= 1:
            return self.patron
        else:
            return "No one"

        
class Patron(object):
    def __init__(self, name, Library):
        self._name = name
        self._Library = Library
        self.booklist = []
        """booklist shows how many books a patron has"""
    def __str__(self):
        return str(self.__dict__)
    def __eq__(self, other):
        return (self._name == other._name)
        
    def addBook(self, title, author, Library):
        """adds a book to the booklist. patrons cannot have more than 3 books"""
        if len(self.booklist) >= 3:
            return "Invalid"
        else:
            pa = Book(title, author)
            if pa in Library.BookList:
                return self.booklist.append(pa)
            else:
                print("Book not available.")
                
    def getBooks(self):
        """shows how many books a Patron has"""
        return self.booklist
    def TurnedIn(self, bookTitle=None, bookAuthor=None):
        #Turns in books. Removes from booklist.
        if bookTitle != None and bookAuthor != None:
            a = Book(bookTitle, bookAuthor)
            if a in self.booklist:
                self.booklist.remove(a)
            else:
                print("Book not in possession.")
        else:
            while len(self.booklist) > 0:
                self.booklist.pop(0)
        return self.booklist
            
            
    
class Library:
    def __init__(self):
        self.BookList = []
        self.PatronList = []
    def __str__(self):
        return str(self.__dict__)
    def __eq__(self, other):
        return (self.__dict__ == other.__dict__)
    """Add, Remove, and find books / patrons"""
    def newBook(self, itemTitle, itemAuthor):
        """Turns it into the Book class"""
        n = Book(itemTitle, itemAuthor)
        self.BookList.append(n)
        return n
    def newPatron(self, patName):
        """Turns nvalues into Patron class"""
        p = Patron(patName, Library == self)
        self.PatronList.append(p)
        return Patron(patName, self)
    def removeBook(self, itemTitle, itemAuthor):
        n = Book(itemTitle, itemAuthor)
        if n in self.BookList:
            self.BookList.remove(n)
        else:
            print("Book not found")
    def removePatron(self, patName):
        p = Patron(patName, Library = self)
        if p in self.PatronList:
            self.PatronList.remove(p)
        else:
            print("Patron not found.")

def Manager():
    input("What would you like to do? Press the approrpriate key to select an option /n 1. Create a new Patron. /n 2. Add a new Book. /n 3. Remove a Patron. /n 4. Remove a Book.")
        
def main():
   #A bunch of functionality tests
    a = Library()
    print(a)
    pope = a.newBook('a', 'me')
    peep = a.newBook('a', 'me')
    piip = a.newBook('n', 'me')
    print(pope == peep)
    print(pope)
    print(piip)
    print(peep)
    s = a.newPatron('Me')
    d = a.newPatron('You')
    print(a.BookList)
    print(a.PatronList)
    s.addBook('a', 'me', a)
    d.addBook('n', 'me', a)
    print(s.booklist)
    print(d.booklist)
    s.TurnedIn()
    a.removeBook('a', 'me')
    a.removePatron('Me')
    print(a.BookList)
    print(a.PatronList)
    print(s.booklist)

main()
