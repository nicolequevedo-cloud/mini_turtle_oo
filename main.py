from mini_turtle_oo import Tortuga
import turtle

# Crear dos tortugas
t1 = Tortuga()
t2 = Tortuga()

# Mover t1
t1.adelante(100)
t1.abajo(50)
t1.adelante(70)

# Mover t2
t2.abajo(30)
t2.adelante(60)
t2.abajo(40)

# Reiniciar t1 y moverlo de nuevo
t1.reiniciar()
t1.adelante(50)

turtle.done()
