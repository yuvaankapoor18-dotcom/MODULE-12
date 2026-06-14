class Myclass:
    def __privatevar(self):
       self.__privatevar = 27

    def __privMethod(self):
        print("im inside class Myclass")

    def hello(self):
        print("Hello World")

foo = Myclass()
foo.hello()
foo.__privatevar()
foo.__privMethod()
    