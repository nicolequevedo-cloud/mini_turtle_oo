# mini_turtle_oo

codigo:
```
import turtle

# Crear las dos tortugas
t1 = turtle.Turtle()
t2 = turtle.Turtle()
turtle.bgcolor("black")


# Configuración para que se vea el movimiento
t1.speed(2)
t2.speed(1)

t1.color("pink")
t2.color("light blue")

# Mover t2 a otro lugar para que no se crucen
t2.penup()
t2.goto (160,0)
t2.pendown()

#  Triángulo con t1
for i in range(3):
    t1.forward(120)
    t1.left(120)

# Exágono t2 (diferente distancia)
for i in range(6):
    t2.forward(60)
    ```
    t2.left(60)

turtle.done()
