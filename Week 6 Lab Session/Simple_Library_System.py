import os
#Step 1: Defining the classes:

members = []
def clear_screen():
    os.system('cls' if os.name == "nt" else 'clear')
class Book:
    #__init__ bascially takes the title and author as parameters
    def __init__ (self, title, author):
        self.title = title
        self.author = author
        #Sets the availability_status to "Available" by default
        self.availability_status = "available"
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {self.availability_status}")

class Member:
    def __init__ (self, name):
        self.name = name 
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)
    
    def return_book(self, book):
        self.borrowed_books.remove(book)



class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Book {title} by {author} added to the library !")

    def display_books(self):
        if not self.books:
            print("No books in the library yet. ")
            return 
        print("\nLibrary Books: ")
        for book in self.books:
            book.display_info()
            print("------")

    def borrow_book(self, member, book_title):
        for book in self.books:
            if book.title.lower() == book_title.lower():
                if book.availability_status == "Available":
                    book.availability_status = "borrowed"
                    member.borrow_book(book)
                    print(f"{member.name} borrowed {book.title}")
                    return
                else:
                    print(f"Sorry, {book.title} is already borrowed.")
                    return
        print(f"Book {book.title} not found in the library ")
    

    def return_book(self, member, book_title):
        #Step 1: Find the book in Library
        for book in self.books:
            if book.title.lower() ==book_title.lower():
                #Step 2: Check if member has borrowed it
                if book in member.borrowed_books:
                    book.availability_status = "Available"
                    member.return_book(book)
                    print(f"{member.name} returned {book.title}")
                    return 
                else:
                    print(f"{member.name} did not borrow {book.title}")
                    return 
        print(f"Book {book.title} not found in the library.")


my_library = Library()

while True:
    clear_screen()
    
    print("\n Library Menu: ")
    print("1. Add a Book")
    print("2. Borrow a Book")
    print("3. Return a Book")
    print("4. Display all Books")
    print("5. Quit")

    choice = input("\nEnter your choice (1-5): ")


    if choice == "1":
        title = input("Enter the Book Title: ")
        author = input("Enter Book Author: ")
        my_library.add_book(title, author)

    elif choice == "2":
        member_name = input("Enter member name: ")
        member = next((m for m in members if m.name == member_name), None)
        if not member: 
            member = Member(member_name)
            members.append(member)
        book_title = input("Enter book title to borrow: ")
        my_library.borrow_book(member, book_title)
        pass
    elif choice == "3":
        member_name = input("Enter members name: ")
        member = next((m for m in members if m.name == member_name), None)
        if member: 
            book_title = input("Enter the book title to return: ")
            my_library.return_book(member, book_title)

        else:
            print(f"No Member found with name {member_name}")
        pass

    elif choice == "4":
        my_library.display_books()

    elif choice == "5":
        print("Exiting the library System.")
        break
    else:
        print("Invaalid choice. Please enter a number 1-5. ")
    input("\nPress Enter to return to the menu")

