class IOString:

    def __init__(self):
        self.str1 = ""

    def get_string(self):
        self.str1 = input("Enter a string: ")
        return self.str1

    def print_string(self):
        print(self.str1.upper())

str1 = IOString()

print("Original String: " ,str1.get_string())
print("Uppercase String: ", end="")
str1.print_string()