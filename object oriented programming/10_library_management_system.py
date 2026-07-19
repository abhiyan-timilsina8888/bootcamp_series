class library:

    def __init__(self):
        self.books={}

    def add_books(self,title,author):
        if title in self.books:
            print("Book already exists.")
        else:
            self.books[title]=author
            print(f"{title } has been added.")

    def remove_books(self,title):
        if title in self.books:
            del self.books[title]
        else:
            print("Book not found")

    def search_book(self):
        print("1.search with title ")
        print("2. search with author name")

        choice= int(input("enter the choice:"))

        if choice==1:
            title= input("enter the book title:")
            if title in self.books:
                print(f"book found\n")
                print(f"Title:{title}")
                print(f"Author:{self.books[title]}")

            else:
                print("Book not found")

        elif choice == 2:
            author = input("enter author name:")
            found = False

            for title, book_author in self.books.items():
                if book_author.lower()==author.lower():
                    print(f"title:{title}")
                    found= True

            if not found:
                print("not available")

    
    def display_books(self):
        if not self.books:
            print("empty ")
            return
        
        print("books available are;")

        for title, author in self.books.items():
            print(f"title: {title}")
            print(f"author: {author}")


    
lib= library()


while True:


    print("1. add_books.")
    print("2. remove books.")
    print("3. search books.")
    print("4. display books.")
    print("5.exit")


    option= int(input("enter the options:"))

    if option== 1:
        title= input("enter the title")
        author= input("enter the author")
        lib.add_books(title,author)

    elif option == 2:
        title= input("enter the title")
        lib.remove_books(title)

    elif option == 3:
        lib.search_book()

    elif option == 4:
        lib.display_books()

    elif option == 5:
        print("Thanks for using library managemnet system")

    else:
        print("invalid number.")

print("\n")









