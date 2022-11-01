class Dog:
    def woof(self):
        print("woof woof")


class Beagle(Dog):
    def woof(self):
        super().woof()
        print("super jump")


beagle = Beagle()
# beagle.jump()
beagle.woof()
