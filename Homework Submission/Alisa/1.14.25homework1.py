class Person:
    def __init__(self, name, age):
        self.name = str(name)
        self.age = int(age)

    def greet(self):
        print(f"Hello, {self.name}. Have a good day!")

    def move(self, location):
        self.location = str(location)
        print(f"{self.name} is moving to {self.location}!")

person1 = Person("John", 25)
person1.greet()

person2 = Person("Alice", 30)
person2.greet()

person3 = Person("Bob", 35)
person3.greet()
person3.move("New York")

# maybe books would be a real-life scenaro where the classes and objects could be applied. They all need a title, author, length, genre, etc. They could also be checked out or not

class Book:
    def __init__(self, title, author, pages, genre):
        self.title = str(title)
        self.author = str(author)
        self.pages = int(pages)
        self.genre = str(genre)
        self.checked_out = False  
        self.checked_out_by = None  

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}, Genre: {self.genre}, Checked Out: {self.checked_out}")

    def check_out(self, person_name):
        if not self.checked_out:
            self.checked_out = True
            self.checked_out_by = person_name
            print(f"{self.title} has been checked out by {self.checked_out_by}")
        else:
            print(f"{self.title} is already checked out by {self.checked_out_by}")

    def return_book(self):
        if self.checked_out:
            print(f"{self.title} has been returned by {self.checked_out_by}")
            self.checked_out = False
            self.checked_out_by = None
        else:
            print(f"{self.title} was not checked out.")

book1 = Book("BOOOK", "IDK", 642, "nonfiction")
book2 = Book("oooh.... look a book in the wild!!!", "Pokemon", 265, "fiction")
book3 = Book("book about the most boring things in the universe", "your boring professor", 65465, "nonfiction")


book1.check_out("Alisa")
book1.display_info()
book1.return_book()
book1.display_info()