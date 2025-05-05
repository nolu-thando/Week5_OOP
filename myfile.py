# Base class
class Character:
    def __init__(self, name, origin):
        self.name = name
        self.origin = origin

    def introduce(self):
        return f"I am {self.name} from {self.origin}!"

# Subclass 
class Superhero(Character):
    def __init__(self, name, origin, power, weakness):
        super().__init__(name, origin)
        self.__power = power      # Encapsulated attribute
        self.__weakness = weakness

    def use_power(self):
        return f"{self.name} uses {self.__power}!"

    def reveal_weakness(self):
        return f"{self.name}'s weakness is {self.__weakness}."

# Example usage
hero1 = Superhero("Catwoman", "New York City", "Super Strength", "Bright Light")
print(hero1.introduce())
print(hero1.use_power())
print(hero1.reveal_weakness())
