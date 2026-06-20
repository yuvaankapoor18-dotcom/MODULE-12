from abc import ABC, abstractmethod
from modulefinder import test
class abstract(ABC):

    def print(self, x):
        print("passed value", x)
    @abstractmethod
    def task(self):
        print("this is an abstract parent-class")

class child(abstract):
    def task(self):
        print("this is an abstract child-class")

test.obj = child()
test.obj.task()
test.obj.print(100)