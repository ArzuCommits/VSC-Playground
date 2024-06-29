class Employee:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
        
    def details(self):
        print(f"The name of the employee is {self.name} and his occupation is {self.occupation}")
        
        
arzu = Employee('arzu','programmer')
print(arzu.details())

# this is a testing comments