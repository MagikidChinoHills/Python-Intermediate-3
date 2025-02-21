
#Inheritance and Polymorphism

'''
Inheritance: A mechanism where a new class(subclass
inherits properties and behavior from an existing
class(superclass)

Polymorphism: The ability of different classes to be treated as
instances of the same class through a common interface
'''

#Problem 1
'''
Create a subclass Ebook that inherits from the Book class. Add
a new attribute' file_size' and a method 'read_book' to
the Ebook class

'''

'''
Class Name: Book
Description: This defines a class which contains title, author and pages of a book.
This has one method which displays the books inforamtion.
'''
'''
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        print(f"Title: {self.title} , Author: {self.author} , Pages: {self.pages}")

    def update_title(self, new_title):
        self.title = new_title

    def update_author(self, new_author):
        self.author = new_author

    def update_pages(self, new_pages):
        self.pages = new_pages

    def read_book(self):
        print(f"Reading the eBook '{self.title}'")


Class Name: EBook
Description: THis is going to inherit the Book class, and add new attributes.


class EBook(Book):
    def __init__(self, title, author, pages,fs):
        super().__init__(title, author, pages)
        self.fie_size = fs

    def read_book(self):
        print(f"Reading the eBook '{self.title}' with file size {self.fie_size} MB.")

book1 = EBook("Victor's Super Secret Diary", "Victor Liu", 384,15)
print(book1)

book1.display_info()
book1.read_book()
book1.update_pages(500)
book1.display_info()

book2 = Book("Captain Underpants", "Justin", 35)
book2.display_info()

book2.update_pages(10000)
book2.display_info()

#Polymorphism
def print_info(tbook):
    tbook.display_info()
print("-------------------------------")
print_info(book1)
print_info(book2)
'''

'''
# INHERITENCE AND POLYMORPHISM

# Base class: Animal
class Animal:
    def make_sound(self):
        print("Some generic animal sound")

# Subclass: Dog
class Dog(Animal):
    def make_sound(self):
        print("Bark! Bark!")

# Subclass: Cat
class Cat(Animal):
    def make_sound(self):
        print("Meow! Meow!")

def play_sound(animal):
    animal.make_sound()

dog = Dog()
cat = Cat()
generic_animal = Animal()

# Polymorphism
play_sound(dog)
play_sound(cat)
play_sound(generic_animal)
'''
import random

class Superhero:
    def __init__(self, name, health = 100):
        self.name = name
        self.health = health

    def use_power(self):
        print("Using a generic superhero power!")

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage! Health: {self.health}")

    def is_defeated(self):
        return self.health <= 0


class SuperStrengthMan(Superhero):
    def use_power(self):
        print(f"{self.name} has superstrength and he can lift a big bag of candy")

class Telekinesis(Superhero):
    def use_power(self):
        print(f"{self.name} has telekenisis powers and is all knowing")

class Shapeshifter(Superhero):
    def use_power(self):
        print(f"{self.name} has shapeshifting powers and can shapeshift into an apple")

class Technopathy(Superhero):
    def use_power(self):
        print(f"{self.name} has technopathy powers and can turn the TV on with his mind")

# Function for polymorphism
def activate_power(hero):
    hero.use_power()


# Battle Function: Superheroes Fight Until One Remains
def superhero_battle(heroes):
    print("\n SUPERHERO BATTLE ROYALE BEGINS! \n")

    while len(heroes) > 1:
        attacker, defender = random.sample(heroes, 2)  # Pick 2 random fighters

        damage = random.randint(10, 25)  # Random damage
        print(f"\n {attacker.name} attacks {defender.name}!")
        attacker.use_power()
        defender.take_damage(damage)

        if defender.is_defeated():
            print(f" {defender.name} is eliminated!\n")
            heroes.remove(defender)  # Remove defeated hero

        input("Press Enter for the next round...\n")  # Pause between fights

    print(f" {heroes[0].name} is the LAST HERO STANDING! ")


heroes = [
    SuperStrengthMan("Victor"),
    Telekinesis("Alisa"),
    Shapeshifter("Leo"),
    Technopathy("Victor Underpants"),
]

superhero_battle(heroes)
