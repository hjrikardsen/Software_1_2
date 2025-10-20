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


def race():
    cars = []

    for i in range(1, 11):
        car = Car(f"ABC-{i}", random.randint(100, 200))
        cars.append(car)

    furthest_distance = 0

    while furthest_distance <= 10000:

        for car in cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)
            travelled = car.travelled_distance

            if travelled > furthest_distance:
                furthest_distance = travelled

    #lambda expression from stackOverflow. Sorts based on the specified attribute of the car objects
    cars.sort(key = lambda car:car.travelled_distance, reverse = True)

    return cars


race()

