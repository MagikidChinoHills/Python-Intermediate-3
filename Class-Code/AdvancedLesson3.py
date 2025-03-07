# Lesson 3
# Encapsulation and Abstraction
'''
Encapsulation: The bundling of data and methods that
operate on that data within a single unit(class)

Abstraction: The process of simplyfing complex systems by modeling
classes based on their essential properties and behaviors
'''

from abc import ABC, abstractmethod

class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self._pages = pages        #Encapsulate / Private

    def display_info(self):
        print(f"Title: {self.title} , Author: {self.author},Pages: {self._pages}")

    def get_pages(self):
        return self._pages

    def set_pages(self,new_pages):
        if new_pages > 0:
            self._pages = new_pages # Encapsulated / Private



#------------------------


#------------------------

book1 = Book("Victor's Diary", "Victor L.", 130)
book1.display_info()
myPages = book1.get_pages()
print("PAGES->:", myPages)

#Set new pages to 1500
book1.set_pages(1500)
myPages = book1.get_pages()
print("PAGES->:", myPages)


#ABC (Abstract Base Class)
'''
Abstact Classes: An abstract class is a class that cannont
be instantiated. It serves as a blueprint for other classes
and may contain abstract methods(methods without implementation
ABSTRACT CLASSES ARE DEFINED USING ABC MODULE

Abstract Methods: Abstract methods are declared in abstract classes
but lack implementation details. They act as placeholders
for methods that must be implemented concrete subclasses.
THESE ARE DEFINE USING '@abstractmethod' decorator from
ABC module.

'''

# Abstract Class

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Our class circle
class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius
    def area(self):
        return 3.14 * self._radius ** 2

# Class of Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height

circle1 = Circle(5)
print(f"Circle area is {circle1.area()}")
rect1 = Rectangle(10,15)
print(f"Rectangle area is {rect1.area()}")
