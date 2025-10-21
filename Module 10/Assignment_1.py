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