import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)
t.pensize(2)

color = ['red', 'green', 'yellow',
    'cyan', 'orange', 'skyblue']

for i in range(150):
    t.pencolor(color[i%6])
    t.circle(190-i,90)
    t.lt(90)
    t.circle(190-i,90)
    t.rt(60)

s.exitonclick()