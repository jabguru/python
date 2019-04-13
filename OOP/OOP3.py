# # Inheritance
# class Animal():
#     def __init__(self):
#         print("Animal Created")
#
#     def who_am_i(self):
#         print("Animal")
#
#     def eat(self):
#         print("Eating")
#
#
# class Dog(Animal):
#
#     def __init__(self):
#         print("Dog created")
#
#
# my_dog = Dog()
# my_dog.who_am_i()
# my_dog.eat()

# Special methods

class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: {}, Author: {}, Pages: {}".format(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is destroyed")


b = Book("Python", "Jabguru", 200)
del b