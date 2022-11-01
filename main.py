
class Human:
    def __init__(self, name):
        self.name = name

    def say_Hello(self):
        print(f"hello my name is {self.name}")


class Player:
    def __init__(self, name, xp):
        self.name = name
        self.xp = xp

    def say_Hello(self):
        print(f"hello my name is {self.name}")


class Fan:
    def __init__(self, name, fav_team):
        self.name = name
        self.fav_team: fav_team

    def say_Hello(self):
        print(f"hello my name is {self.name}")


nico = Player("nico", 20)
print(nico.name)
nico.say_Hello()
ko = Fan("Ko", 21)
ko.say_Hello()
