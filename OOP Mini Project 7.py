class Flight:
    max_passengers = 3

    def __init__(self, number):
        self.number = number
        self.passengers = []
        self.waiting_list = []

    def add_passenger(self, passenger):
        if len(self.passengers) >= Flight.max_passengers:
            self.waiting_list.append(passenger)
        else:
            self.passengers.append(passenger)

# Write your code below:

#Code execution
my_flight = Flight("ISM480")
my_flight.add_passenger("Bo")
my_flight.add_passenger("Willoughby")

#Passenger List
print(my_flight.passengers)