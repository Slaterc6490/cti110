import turtle

# Create a turtle 
t = turtle.Turtle()

# Move the turtle to the starting point
t.penup()
t.goto(0, 100)
t.pendown()

# Draw the letter 'C'
t.setheading(140)
t.circle(100, 270)


# Create a turtle object
t = turtle.Turtle()

# Move the turtle to the starting point
t.penup()
t.goto(-100, 0)
t.pendown()

# Draw the 'S'
t.forward(40)
t.circle(50, 180)
t.circle(-50, 180)
t.forward(40)

# Hide the turtle
t.hideturtle()

# Keep the window open until it is manually closed
turtle.done()
