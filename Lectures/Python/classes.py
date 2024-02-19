class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2,8)
print(p.x)
print(p.y)


class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passangers = []

    def addPassangers(self, name):
        if not self.openSeats():
            return False 
        self.passangers.append(name)
        return True

    def openSeats(self):
        return self.capacity - len(self.passangers)

flight = Flight(3)

people = ["Harry", "Ron", "Hermione", "Ginny"]
for i in people:
    success = flight.addPassangers(i)
    if success:
        print(f"Added {i} to flight successfully")
    else:
        print(f"No available seats for {i}")