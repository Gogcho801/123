from turtle import *


#we want to paint a house

#step 1: draw a square

speed(60)
width(5)
color ("purple")
forward(200)
left(90)
forward (200)
left(90)
forward (200)
left(90)
forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color ("yellow")
begin_fill()
left(90)
forward(120)   #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()
color ("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


#draw windows
color("blue")

penup()
goto(200,150)
right(60)
penup()
forward(40)
pendown()
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)



penup()
forward(90)
pendown()

color("blue")
begin_fill()
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
end_fill()


color("blue")
begin_fill()
penup()
goto(200,150)
forward(40)
pendown()
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
end_fill()

#The Fence
penup()
goto(-0,80)
color("black")
pendown()
forward(200)
left(90)
forward(80)
left(90)
forward(200)
left(90)
forward(80)


penup()
goto(-40,80)
pendown()
left(180)
forward(80)

penup()
goto(-80,80)
pendown()
forward(80)

penup()
goto(-120,80)
pendown()
forward(80)

penup()
goto(-160,80)
pendown()
forward(80)

right(90)
forward(40)
right(45)
forward(200)

penup()              #step2
goto(-200,80)
pendown()
forward(100)


penup()
goto(-200,0)
pendown()
forward(250)
right(135)
forward(380)
penup()
goto(200,180)
pendown()
forward(200)
right(90)
penup()
forward(180)
pendown()
right(90)
forward(200)
penup()
right(90)
forward(80)
pendown()
right(90)
forward(200)
right(90)
forward(80)
right(90)
forward(40)
right(90)
forward(80)
left(90)
forward(40)
left(90)
forward(80)
right(90)
forward(40)
right(90)
forward(80)
left(90)
forward(40)
left(90)
forward(80)


penup()              #step2
goto(-200,80)
pendown()
right(135)
forward(100)
right(135)
forward(270)
penup()
goto(200,156)
pendown()
forward(200)
left(90)
penup()
forward(150)
pendown()



color("orange")
begin_fill()
circle(50)
end_fill()





exitonclick()
