class Animal:
    zoo_name = "Hayaton"

    def __init__(self, name, hunger=0):
        self._name = name
        self._hunger = hunger
    
    def get_name(self):
        return self._name
    
    def is_hungry(self):
        return self._hunger > 0
    
    def feed(self):
        self._hunger -= 1

    def talk(self):
        print("Hello")

class Dog(Animal):
    def talk(self):
        print("woof woof")
    
    def fetch_stick(self):
        print("There you go, sir!	")

class Cat(Animal):
    def talk(self):
        print("meow")

    def chase_laser(self):
        print("Meeeeow")

class Skunk(Animal):
    def __init__(self, name, stink_count=60):
        super().__init__(name)
        self._stink_count = stink_count

    def talk(self):
        print("tsssss")

    def stink(self):
        print("Dear lord!")

class Unicorn(Animal):
    def talk(self):
        print("Good day, darling")

    def sing(self):
        print("I’m not your toy...")

class Dragon(Animal):
    def __init__(self, name, color="Green"):
        super().__init__(name)
        self._color = color

    def talk(self):
        print("Raaaawr")
    
    def breath_fire(self):
        print("$@#$#@$")

def main():
    dog1 = Dog("Brownie", 10)
    cat1 = Cat("Zelda", 3)
    skunk1 = Skunk("Stinky")
    unicorn1 = Unicorn("Keith", 7)
    dragon1 = Dragon("Lizzy", 1450)

    dog2 = Dog("Doggo", 80)
    cat2 = Cat("Kitty", 80)
    skunk2 = Skunk("Stinky Jr.", 80)
    unicorn2 = Unicorn("Clair", 80)
    dragon2 = Dragon("McFly", 80)

    zoo_lst = [dog1, cat1, skunk1, unicorn1, dragon1,
               dog2, cat2, skunk2, unicorn2, dragon2]

    for animal in zoo_lst:
        print(type(animal).__name__, animal.get_name())
        animal.talk()

        if(isinstance(animal, Dog)):
            animal.fetch_stick()
        elif(isinstance(animal, Cat)):
            animal.chase_laser()
        elif(isinstance(animal, Skunk)):
            animal.stink()
        elif(isinstance(animal, Unicorn)):
            animal.sing()
        elif(isinstance(animal, Dragon)):
            animal.breath_fire()

        print()

        while animal.is_hungry():
            animal.feed()
    
    print(Animal.zoo_name, "Zoo")

main()
