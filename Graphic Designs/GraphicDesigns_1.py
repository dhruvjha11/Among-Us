import turtle

s = turtle.Screen()
t = turtle.Turtle()
l1 = ["purple","orange","red","blue","green"]

s.bgcolor("black")

for i in range(200):
    t.speed(10)
    t.color(l1[i%5])
    t.pensize(i/10+1)
    t.forward(i)
    t.left(59)

t.screen.exitonclick()