# Enviroment

class Enviroment:
    def __init__ (self):
        self.lum = 50
    
    def modify_lum(self, modificacion):
        self.lum += modificacion

    def set_lum(self, valor):
        self.lum = valor
        
    def get_lum(self):
        return self.lum

    def __str__(self):
        return "Luminosidad: " + str(self.lum) + "%"