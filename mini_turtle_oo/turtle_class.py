import turtle

class Tortuga:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.speed(1)
        self.posicion_x = 0

    def adelante(self, pasos):
        self.t.forward(pasos)
        self.posicion_x += pasos

    def abajo(self, pasos):
        self.t.right(90)
        self.t.forward(pasos)
        self.t.left(90)

    def reiniciar(self):
        self.t.penup()
        self.t.home()
        self.t.pendown()
        self.posicion_x = 0
