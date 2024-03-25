class Vehicle:

    def __init__(self, color, speed, fuel_type):
        self.color = color
        self.speed = speed  # In Km/h
        self.fuel_type = fuel_type

# Write your code below:

class Car(Vehicle):
    def __init__(self, color, speed, fuel_type, num_doors, is_electric):

        Vehicle.__init__(self,color,speed,fuel_type)

        self.num_doors = num_doors
        self.is_electric = is_electric

my_car = Car("Purple", "110MPH", "Unleaded", 4, "False")
print(f"Color: {my_car.color}\nSpeed: {my_car.speed}\nFuel Type: {my_car.fuel_type}"
      f"\nNum of Doors: {my_car.num_doors}\nElectric: {my_car.is_electric}")