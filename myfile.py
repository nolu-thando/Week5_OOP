class Character:
    def __init__(self,name, origin):
        self.name = name
        self.origin = origin

        def introduce (self):
            return f "I am {self.name} from {self.origin}!"

            #subclass
            class Superhero (Character):
                def __init__(self, name, origin,power, weakness):
                    super().__init__(name, origin)
                    self. __power = power
                    self . __weakness = weakness
                
                def use_power(self):
                    return f "{self.name} uses {self.__power}!"