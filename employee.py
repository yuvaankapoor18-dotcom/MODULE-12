class employee:
    
    employee = 0

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        employee.employee += 1

    def __del__(self):
        print("Employee Fired")
        employee.employee -= 1


jack = employee("Jack", 30, 50000)

print("Name: {}, Age: {}, Salary: {}".format(jack.name, jack.age, jack.salary))
print("Total employees: {}".format(employee.employee))
