# class Dog():
#     # Class Object Attribute
#
#     species = "mammal"
#
#     def __init__(self, breed, name):
#         self.breed = breed
#         self.name = name
#
#
# my_dog = Dog("Lab", "Jack")
#
# print(my_dog.breed)
# print(my_dog.name)
# print(my_dog.species)


class Circle():

    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.x = 4


    def area(self):
        return self.radius*self.radius * Circle.pi

    def set_radius(self, new_r):
        self.radius = new_r


# myc = Circle(3)
# myc.set_radius(100)
# print(myc.area())

print(Circle.x)