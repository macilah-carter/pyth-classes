class Superhero:
    def __init__(self,name,powers,rating,age,id):
        self.name=name
        self.powers= powers
        self.rating = rating
        self.age = age
        self._id = id

    def __str__(self):
        return f"Superhero(name={self.name}, powers={self.powers}, rating={self.rating},age={self.age}, id = {self._id})"

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, newValue):
        if isinstance(newValue, int) and newValue > 0:
            self._id = newValue
        else:
            raise ValueError("Must be an int")


class Subgroup(Superhero):
    def __init__(self, name, powers, rating,age,group,id):
        super().__init__(name, powers, rating,age,id)
        self.group = group

    def Group(self):
        return f"They belong to this group {self.group}"




# Activity 2: Polymorphism Challenge! 🎭


class Vehicle:
    def move(self):
        return f"Movement for all"

class Car:
    def move(self):
        return f"Driving"

class Plane:
    def move(self):
        return f"Flying"
        
class Boat:
    def move(self):
        return f"Sailing"
    
class Bicycle:
    def move(self):
        return f"Cycling"



car = Car()
print(car.move)

# hero = Superhero("Flash", ["Speed", "Agility"], 9.5, 30, 101)
# print(hero)

# group_hero = Subgroup("Ironman", ["Intelligence", "Flight"], 9.8, 45, "Avengers", 102)
# print(group_hero)
# print(group_hero.Group())

# print(hero.id)
# hero.id = 102
# print(hero.id)