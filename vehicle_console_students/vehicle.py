from blinker import *
from engine import *
from fuel import *
from enviroment import *

class Vehicle:
    def __init__(self):
        self.blinker_front = Blinker(BLINKER_FRONT)
        self.blinker_rear = Blinker(BLINKER_REAR)
        self.engine = Engine()
        self.fuel = Fuel(self.engine)
        self.enviroment = Enviroment()

    def __str__(self):
        status = ""
        status += str(self.blinker_front) + "  BLINKERS  " + str(self.blinker_rear) + "\n"
        status += str(self.engine) + "\n"
        status += "Combustible: " + str(self.fuel.level) + "\n"
        status += "Luminosidad: " + str(self.enviroment.get_lum())
        return status


    def do_work(self):

        while self.fuel.level > 0:            
            print(self)
            key = input('next action (q quit): ')

            if key == 's':
                self.blinker_front.change()
            if key == 'a':
                self.blinker_rear.change()
            if key == 'w':
                self.engine.modify_rpm(100)
            if key == 'z':
                self.engine.modify_rpm(-100)
            if key == 'e':
                self.engine.modify_gear(1)
            if key == 'd':
                self.engine.modify_gear(-1)
            if key == 'r':
                self.enviroment.modify_lum(10)
            if key == 'f':
                self.enviroment.modify_lum(-10)

            if key == 'q':
                exit()
            
            #self.light.update()
            self.fuel.update()


if __name__ == "__main__":
    vehicle1 = Vehicle()
    vehicle1.do_work()

