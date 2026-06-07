class Dog:

    species = "german shephard"
    species2 = "husky"
    def __init__(self, name, age):
        self.name = name
        self.age = age
blu = Dog("Blu", 10)
white = Dog("White", 5)

print("there is a dog named {} and it is {} years old".format(blu.name, blu.age))
print("Blu is a {}".format(blu.species))
print("Blu is also a {}".format(blu.species2))
print("there is another dog named {} and it is {} years old".format(white.name, white.age))
print("White is also a {}".format(white.species))
print("White is also a {}".format(white.species))
