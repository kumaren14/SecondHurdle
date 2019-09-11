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

ian.speed(10)
alan.speed(10)
ellie.speed(10)
timmy.speed(10)

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
alan.begin_fill()
alan.pensize(3)
alan.right(45)
alan.forward(35)
alan.left(90)
alan.forward(35)
alan.end_fill()
alan.right(45)
alan.begin_fill()
alan.pensize(3)
alan.right(45)
alan.forward(35)
alan.left(90)
alan.forward(35)
alan.end_fill()

alan.color("black")
alan.penup()
alan.goto(-200, 200)

alan.left(45)
ellie.left(90)
ian.left(90)

ian.color("black")
timmy.color("black")
ellie.color("black")

alan.goto(-5, -50)
alan.write("W")
alan.goto(-200, 200)
ian.goto(10, -50)
ian.write("a")
ian.goto(200, 200)
ellie.goto(20, -50)
ellie.write("z")
ellie.goto(200, -200)
timmy.goto(30, -50)
timmy.write("o")
timmy.goto(200, 200)
alan.goto(40, -50)
alan.write("w")
alan.goto(-200, 200)
ian.goto(50, -50)
ian.write("s")
ian.goto(-200, -200)
ellie.goto(60, -50)
ellie.write("k")
ellie.goto(200, -200)
timmy.goto(70, -50)
timmy.write("i")
timmy.goto(200, 200)






turtle.exitonclick()