class Cook(object):
    def prepareDish(self):
        self.cutter = Cutter()
        self.cutter.cutVegetables()
        self.boiler = Boiler()
        self.boiler.boilVegetables()

class Cutter(object):
    def cutVegetables(self):
        print("All vegetables are cut")

class Boiler(object):
    def boilVegetables(self):
        print("All vegetables are boiled")

cook = Cook()
cook.prepareDish()
