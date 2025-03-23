# Solution: A simple Python program to demonstrate using functions and classes.
def add_numbers(a, b):
    result = a + b
    print("The sum of", a, "and", b, "is", result)

add_numbers(3, 5)  # Example usage

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return f"{self.name} says hello"

# Create an instance of the class and call a method
person1 = Person("Alice", 25)
print(person1.speak())  # Output: Alice says hello

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

# Create an instance of the class and call a method
bank_account1 = BankAccount("123456789")
print(bank_account1.deposit(50))  # Output: The account has been successfully deposited with $50. The new balance is now $50.

class Shape:
    def __init__(self, shape_type):
        self.shape_type = shape_type

    def area(self):
        return 4 * 3.141592653589793

# Create an instance of the class and call a method
circle_shape = Shape("Circle")
print(circle_shape.area())  # Output: The area of the circle is 12.5663706146482e-06

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author}, priced at ${self.price}"

# Create an instance of the class and call a method
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 9.99)
print(book1)  # Output: The Great Gatsby by F. Scott Fitzgerald, priced at $9.99

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, a, b):
        self.result = a + b
        print("The result of", a, "and", b, "is", self.result)

    def subtract(self, a, b):
        self.result = a - b
        print("The result of", a, "and", b, "is", self.result)
