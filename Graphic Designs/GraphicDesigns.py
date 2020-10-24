import turtle

s = turtle.getscreen()
t = turtle.Turtle()
l1 = ["purple","orange","red","blue","green"]

s.bgcolor("black")
for i in range(200):
    t.speed(20)
    t.color(l1[i%5])
    t.pensize(i/10+1)
    t.forward(i)
    t.left(59)

t.screen.exitonclick()