import turtle

# Set up the turtle window
window = turtle.Screen()
window.bgcolor("black")
window.title("Love You Sandeep - Turtle Design")

# Create a turtle named 'pen'
pen = turtle.Turtle()
pen.speed(3)
pen.color("red")
pen.pensize(3)

# Function to draw a heart shape
def draw_heart():
    pen.begin_fill()
    pen.left(140)
    pen.forward(180)
    pen.circle(-90, 200)
    pen.left(120)
    pen.circle(-90, 200)
    pen.forward(180)
    pen.end_fill()

# Write the love message
def write_message():
    pen.penup()
    pen.goto(-100, 150)
    pen.color("white")
    pen.write("Love You, Sandeep!", font=("Arial", 18, "bold"), align="center")

# Draw SAP colors (Yellow and Blue) around the heart
def sap_colors_effect():
    sap_colors = ["#FFDD00", "#003366"]  # SAP Yellow and SAP Blue
    for color in sap_colors:
        pen.color(color)
        pen.penup()
        pen.goto(-200, 200)
        pen.pendown()
        pen.dot(30)  # Draw a dot in SAP color

# Main code
pen.penup()
pen.goto(0, -200)
pen.pendown()

# Draw the heart and the message
draw_heart()
write_message()
sap_colors_effect()

# Hide the turtle after drawing
pen.hideturtle()

# Keep the window open until clicked
window.exitonclick()
