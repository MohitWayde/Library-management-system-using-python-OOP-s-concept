# 25-11-2020
# mini project on LIBRARY MANAGEMENT SYSTEM USING OOP concepts
# statements:
# Displaybook() : To display the available books
# Lendbook(): To lend a book to a user
# Addbook(): To add a book in the library
# Returnbook(): To return the book in the library.
# object1 = Library(listofbooks, library_name)
# dictionary for who have particular book

alloted_books = {}
notalloted_books = ["Deep work","Rich dad poor dad","Tools of titans","Ikigai",
                         "The code of extra-ordinary minds","So good they cant ignore you"]
class Library_mgmt:
    def __init__(self, alist_of_books, aname_of_library):
        self.list_of_books = alist_of_books
        self.name_of_library = aname_of_library
        
    def lendbook(self):
        global alloted_books
        global notalloted_books
        print("You chose to lend a book")
        person_username = input("Enter your name :")
        book_name = input("Enter the book name which you want :")
        if book_name in notalloted_books:
            print(f"Great {person_username}, You've taken \"{book_name}\" ")
            alloted_books.__setitem__ (book_name,person_username)
            notalloted_books.remove(book_name)
            print(alloted_books)
            print(notalloted_books)
        else:
            print(f"!Book is already taken by {alloted_books[book_name]}")
            
            
    def displaybook(self):
#         print(f"Here are the name of books that available :\n{notalloted_books}")
        print(f"Here are the name of books that available :")
        for i in notalloted_books:
            print(i)
#         print(f"Here are the name of books that are alloted :\n{alloted_books}")
        print(f"Here are the name of books that are alloted :")
        for j in alloted_books:
            print(j)
            
    def addbook(self):
        new_book = input("Enter the new book name :")
        notalloted_books.append(new_book)
        print("New book is added")
        print("Here is an updated book inventory :",notalloted_books)
    def returnbook(self):
        user_name = input("Enter your name :")
        return_book_var = input("Name of book for returning :")
        if user_name and return_book_var in alloted_books:
            notalloted_books.append(return_book_var)
            del alloted_books[return_book_var]
        print("Book returned successfully")
        print("alloted books are :\n",alloted_books)
        print("Available books are :\n",notalloted_books)
    
    

library1 = Library_mgmt(["Deep work","Rich dad poor dad","Tools of titans","Ikigai",
                         "The code of extra-ordinary minds","So good they cant ignore you"],
                        "audible") 

while True:
    user_input = input("!Welcome to Library Management System!\n"+
    "Press 1 for lend books\n"+
    "Press 2 for display books\n"+
    "Press 3 for add new books\n"+
    "Press 4 for return books\n"+
    "Press 0 for exit\n"+
    "Enter your choice here :")
    if user_input == '1':
        library1.lendbook()
    if user_input == '2':
        library1.displaybook()
    if user_input == '3':
        library1.addbook()
    if user_input == '4':
        library1.returnbook()
    if user_input == '0':
        break
