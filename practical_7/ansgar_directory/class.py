#### Book
# class BookClass with attributes title, author, and year
class BookClass:
    # function that will always run without needing to be called
    def __init__(self, title, author, year):
        # assign the attributes to inputs when creating an object for the class (such as book1)
        self.title = title
        self.author = author
        self. year = year
        # print the attributes of the book
        print(f"Book attributes are:\nTitle = {self.title}\nAuthor = {self.author}\nYear = {self.year}\n")
    # end class block
    pass

# create object book1 for BookClass with attributes
# book1 = BookClass("Scary book", "Steve Steveson", 1995)

# print book1 (does not tell much except that the book exists)
# print(book1)

# create another object book2
# book2 = BookClass("Pageturner", "Frank Frankenstein", 2008)

#### Methods intro
# make a Robot class and give the user the ability to make the robot speak
class Robot:
    def speak(self, text):
        print(f"Beep Boop... Loading... Language loaded: {text}")
    pass

#### Calculator
# make a robot object for the class and chose what it says
# my_robot = Robot()
# my_robot.speak("I am a stinky Clanker!")

# make a calculator class
class Calculator:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
        self.add = Calculator.add(number1, number2)
        self.subtract = Calculator.subtract(number1, number2)
        self.multiply = Calculator.multiply(number1, number2)

    def add(number1, number2):
        sum = number1 + number2
        return sum

    def subtract(number1, number2):
        sum = number1 - number2
        return sum

    def multiply(number1, number2):
        sum = number1 * number2
        return sum
        
    pass

# make an object in Calculator with numbers
# my_calc = Calculator(2, 6)

# do the calculations on the numbers in the object above
# print(my_calc.add)
# print(my_calc.subtract)
# print(my_calc.multiply)

#### Circle
# import math module for pi
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.calc_perimeter = Circle.circumference(radius)
        self.calc_area = Circle.area(radius)

    def circumference(radius):
        circ = radius * 2 * math.pi
        circ = round(circ, 2)
        return circ

    def area(radius):
        area = (radius ** 2) * math.pi
        area = round(area, 2)
        return area

    pass

# create object
# and make the user input the value for the radius
# my_circle = Circle(int(input()))

# get the circumference
# print(my_circle.calc_perimeter)

# get the area
# print(my_circle.calc_area)

#### nesting classes and objects
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = False
        self.borrower = None

    def __str__(self):
        # The __str__ dunder method will be called when using print(book_obj)
        return f"Informative message about the book. You can also use attributes {self.title}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, added_book):
        self.books.append(added_book)



class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []


# Example usage
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
my_library = Library()

# add a book to my_library and make it avaliable
my_library.add_book(f"{book1.title} by {book1.author}, published in {book1.year}")

# show what is in the library
print(my_library.books)

member1 = Member("Alice")
# member1.borrow_book(library, book1)  # Now the book should be borrowed by Alice

# print("Available books:", [str(book) for book in my_library.available_books])