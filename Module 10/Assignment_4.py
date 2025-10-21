import random


class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_of_speed):

        if self.current_speed + change_of_speed < 0:
            self.current_speed = 0
        elif self.current_speed + change_of_speed <= self.maximum_speed:
            self.current_speed += change_of_speed

    def drive(self, hours):
        travelled = self.current_speed * hours
        self.travelled_distance += travelled


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = []

        for i in range(3):
            car = Car(f"ABC-{i}", random.randint(100, 200))
            self.cars.append(car)

    def hour_passes(self):

        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):

        for car in self.cars:
            print(f"License plate: {car.license_plate}")
            print(f"Maximum speed: {car.maximum_speed}")
            print(f"Current speed: {car.current_speed}")
            print(f"Travelled distance: {car.travelled_distance}\n\n")

    def race_finished(self):

        for car in self.cars:
            if car.travelled_distance > self.distance:
                return True

        return False
