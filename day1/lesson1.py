from turtle import *

speed(30)

width(5)

color("cyan")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
forward(70)


color("red")
begin_fill()

left(90)
forward(100)

right(90)
forward(60)

right(90)
forward(100)

end_fill()

penup()
goto(200, 200)
pendown()

color("blue")
begin_fill()

right(150)
forward(200)

left(120)
forward(200)

end_fill()

penup()
goto(0, 200)
pendown()

left(30)
forward(30)

left(90)

color("yellow")
begin_fill()

forward(60)
right(90)

forward(60)
right(90)

forward(60)
end_fill()

penup()
goto(200, 200)
pendown()

left(90)
forward(30)
right(90)

color("yellow")
begin_fill()

forward(60)
left(90)

forward(60)
left(90)

forward(60)
end_fill()

exitonclick() 