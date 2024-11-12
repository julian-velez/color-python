import turtle

# Configuración de la ventana
window = turtle.Screen()
window.bgcolor("black")

# Crear una tortuga
t = turtle.Turtle()
t.speed(10)

# Colores para la figura
colors = ["red", "blue", "green", "yellow", "purple", "orange"]

# Dibujar una figura colorida
for i in range(36):
    t.color(colors[i % len(colors)])
    t.forward(100)
    t.left(60)
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(60)
    t.forward(100)
    t.left(10)

# Finalizar
turtle.done()
