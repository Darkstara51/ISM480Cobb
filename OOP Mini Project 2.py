class Dog:
    def __init__(self, age, name, is_male, weight):
        self.age = age
        self.name = name
        self.is_male = is_male # Boolean. True if Male, False if Female.
        self.weight = weight

my_dog = Dog(1, "moe", False, 5)

print(f"{my_dog.name} is a {my_dog.weight} pound female dog who is {my_dog.age} year old.")