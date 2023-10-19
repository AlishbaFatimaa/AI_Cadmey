class Dog():
    def __init__(self, name):
        self.name = name
    def sit(self):
        print(self.name + " is sitting")

class sardog(Dog):
    def __init__(self, name):
        super().__init__(name)
    def search(self):
        print(self.name + " is searching.")


my_dog = sardog('tommy')
print(my_dog.name + " is a search dog.")
my_dog.sit()
my_dog.search()