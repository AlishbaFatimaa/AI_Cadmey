class Dog():
    def __init__(self, name):
        self.name = name
    def sit(self):
        print(self.name + " is sitting.")


my_dog = Dog('tommy')
print(my_dog.name + " is a great dog!")
my_dog.sit()