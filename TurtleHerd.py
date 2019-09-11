import turtle

ian = turtle.Turtle()
alan = turtle.Turtle()
ellie = turtle.Turtle()
timmy = turtle.Turtle()

ian.shape("turtle")
alan.shape("turtle")
ellie.shape("turtle")
timmy.shape("turtle")

ian.color("yellow green")
alan.color("ivory")
ellie.color("medium sea green")
timmy.color("black")

ian.speed(50)
alan.speed(50)
ellie.speed(50)
timmy.speed(50)

ian.pensize(5)
alan.pensize(5)
ellie.pensize(5)
timmy.pensize(5)

ian.begin_fill()
ian.circle(100)
ian.end_fill()

alan.penup()
alan.goto(0, 100)
alan.pendown()

alan.begin_fill()
alan.circle(40)
alan.end_fill()

ellie.goto(0, 135)
ellie.pendown()
ellie.begin_fill()
ellie.circle(15)
ellie.end_fill()

timmy.penup()
timmy.goto(0, 140)
timmy.pendown()
timmy.begin_fill()
timmy.circle(10)
timmy.end_fill()

timmy.penup()
timmy.goto(-50, 75)
timmy.pendown
timmy.right(90)

timmy.begin_fill()
timmy.circle(50, 180)
timmy.end_fill()

ian.penup()
alan.penup()
ellie.penup()
timmy.penup()

ian.goto(-200, -200)
ellie.goto(200, -200)
timmy.goto(200, 200)
alan.goto(-50, 75)

alan.pendown()
alan.right(45)
alan.forward(12.5)
alan.left(90)
alan.forward(12.5)



turtle.exitonclick()