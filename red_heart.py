import turtle

# Create a turtle object
pen = turtle.Turtle()
# Set the drawing speed
pen.speed(2)

# Define a function to draw a curve
def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)

# Define a function to draw a full heart
def heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()

# Call the heart drawing function and hide the turtle
heart()
pen.ht()

# Keep the window open (essential for some IDEs like PyCharm)
turtle.done()