class Vehicle:
    def move(self):
        raise NotImplementedError("This method should be overridden in subclasses")


class Car(Vehicle):
    def move(self):
        print("Driving 🚗")


class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")


class Boat(Vehicle):
    def move(self):
        print("Sailing 🚢")


# Polymorphic behavior
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()