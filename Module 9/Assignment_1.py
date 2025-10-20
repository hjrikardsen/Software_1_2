class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0


car1 = Car("ABC-123", 142)

print(f"License plate: {car1.license_plate}")
print(f"Maximum speed: {car1.maximum_speed} km/h")
print(f"Current speed: {car1.current_speed} km/h")
print(f"Travelled distance: {car1.travelled_distance} km")