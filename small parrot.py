class parrot:

    species = "parrot"

    def __init__(self, name, age):
        self.name = name
        self.age = age
blu = parrot("Blu", 10)
white = parrot("White", 15)

print("there is a bird named {} and it is {} years old".format(blu.name, blu.age))
print("Blu is a {}".format(blu.species))
print("there is another bird named {} and it is {} years old".format(white.name, white.age))
print("White is also a {}".format(white.species))
