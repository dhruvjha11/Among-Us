import turtle #inporting turtle

#define colors
colors = ["red","yellow","green","purple","blue","orange"]

#setting up workspace
t = turtle.Turtle()
s = turtle.Screen()

s.title("Spiral Design")
s.bgcolor("black")

for x in range(201):
    t.speed(10)
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)

t.screen.exitonclick()