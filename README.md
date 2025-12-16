<<<<<<< HEAD
Implementa la tortuga usando Programación Orientada a Objetos (POO)

Cada tortuga es un objeto independiente

El estado de cada tortuga se maneja mediante atributos de instancia

Visualización gráfica mediante la librería estándar turtleññ
=======
# mini_turtle_oo

codigo:
```
import turtle

screen = turtle.Screen()
screen.bgcolor("black")

# CLASE
class MiTortuga:
    def __init__(self, color, velocidad, inicio_x):
        self.t = turtle.Turtle()
        self.t.color(color)
        self.t.speed(velocidad)

        self.t.penup()
        self.t.goto(inicio_x, 0)
        self.t.pendown()

        self.posicion_x = inicio_x

    def adelante(self, distancia):
        self.t.forward(distancia)
        self.posicion_x += distancia

    def girar(self, grados):
        self.t.left(grados)

    def triangulo(self):
        for _ in range(3):
            self.adelante(120)
            self.girar(120)

    def hexagono(self):
        for _ in range(6):
            self.adelante(60)
            self.girar(60)

# OBJETOS
t1 = MiTortuga("pink", 2, 0)
t2 = MiTortuga("light blue", 1, 160)

t1.triangulo()
t2.hexagono()

# FIN 
turtle.done()

>>>>>>> 291f8e00a303b1a4ce794872d9d15dca125779e2
