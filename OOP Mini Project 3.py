class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

car_1 = Car("Nissan", "Rouge", "2021")
car_2 = Car("Honda", "Accord", "2023")
car_3 = Car("Honda", "Civic", "2024")

cars = [car_1, car_2, car_3]

for car in cars:
    print(f"We have 1 {car.make} {car.model} from {car.year}")