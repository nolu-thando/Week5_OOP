class Vehicle:
    def move(self):
        return "Moving..."

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing ⛵"

class Superhero(Vehicle):
    def move(self):
        return "Running "

# Polymorphism in action
vehicles = [Car(), Plane(), Boat(), Superhero()]
for v in vehicles:
    print(v.move())
