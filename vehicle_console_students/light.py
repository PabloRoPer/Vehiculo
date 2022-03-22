# Light

class Light:
    def __init__(self, enviroment):
        self.umbral = 40
        self.enviroment =  enviroment
        self.activated = self.enviroment.get_lum() <= self.umbral

    def activate(self):
        self.activated =  True

    def deactivate(self):
        self.activated = False

    def update(self):
        if self.enviroment.get_lum() <= self.umbral:
            self.activate()
        else:
            self.deactivate()

    def __str__(self):
        if self.activated == True:
            resultado = "Activadas"
        else:
            resultado = "Desactivadas"

        return "Luces: " + str(resultado)