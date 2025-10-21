class Elevator:

    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = self.bottom_floor

    def floor_down(self):
        self.current_floor += -1

    def floor_up(self):
        self.current_floor += 1

    def go_to_floor(self, floor_number):

        while floor_number != self.current_floor:

            if self.current_floor > floor_number:
                self.floor_down()
            else:
                self.floor_up()


class Building:
    def __init__(self, bottom_floor, top_floor, numbers_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.numbers_of_elevators = numbers_of_elevators
        self.elevators = []

        for i in range(self.numbers_of_elevators):
            elevator = Elevator(self.bottom_floor, self.top_floor)
            self.elevators.append(elevator)

    def run_elevator(self, elevator_number, floor_number):
        elevator = self.elevators[elevator_number]
        elevator.go_to_floor(floor_number)

    def fire_alarm(self):

        for i in self.elevators:
            i.go_to_floor(self.bottom_floor)