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

