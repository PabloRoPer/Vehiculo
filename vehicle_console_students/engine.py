# Engine

class Engine:
    def __init__(self):
        self.rpm = 0
        self.gear = 0
    
    def modify_rpm(self, data):
        if (data + self.rpm) >= 0:
            self.rpm += data
    
    def modify_gear(self, data):
        if (data + self.gear <= 5) and (data + self.gear >= -1):
            self.gear += data

    def get_speed(self):
        if self.gear >= 0:
            speed = (self.rpm * self.gear / 5)/10
        elif self.rpm > 0:
            speed = -10
        else:
            speed = 0
        return speed

    def __str__(self):
        return str(self.rpm) + "rpm  y  " + str(self.gear) + " marcha  " + str(self.get_speed()) + "km/h"