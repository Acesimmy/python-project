import turtle

# Setup the screen
screen = turtle.Screen()
screen.title("Dress Design with Turtle")
screen.bgcolor("lightblue")
screen.setup(width=800, height=600)

# Create a turtle for drawing the dress
designer = turtle.Turtle()
designer.speed(0)
designer.pensize(2)
designer.color("purple")

# Function to draw the bodice (upper part of the dress)
def draw_bodice():
    designer.penup()
    designer.goto(-50, 100)
    designer.pendown()
    designer.begin_fill()
    designer.color("pink")
    
    # Draw the top part of the bodice
    designer.forward(100)
    designer.left(90)
    designer.forward(100)
    designer.left(90)
    designer.forward(100)
    designer.left(90)
    designer.forward(100)
    designer.left(90)
    
    # Draw shoulder straps
    designer.penup()
    designer.goto(-50, 100)
    designer.pendown()
    designer.left(45)
    designer.forward(30)
    designer.backward(30)
    designer.right(90)
    designer.forward(30)
    designer.backward(30)
    designer.left(45)
    
    designer.end_fill()

# Function to draw the skirt (bottom part of the dress)
def draw_skirt():
    designer.penup()
    designer.goto(-50, 0)
    designer.pendown()
    designer.begin_fill()
    designer.color("purple")
    
    # Draw a flared skirt
    designer.right(90)
    designer.forward(200)
    designer.left(120)
    designer.forward(230)
    designer.left(120)
    designer.forward(230)
    designer.left(120)
    designer.forward(200)
    
    designer.end_fill()

# Function to add polka dot decoration
def add_polka_dots():
    designer.penup()
    designer.color("white")
    designer.goto(-40, -30)
    
    for i in range(5):  # 5 rows of dots
        for j in range(5):  # 5 dots in each row
            designer.dot(10)  # Create a dot
            designer.forward(40)  # Move to the next dot position
        designer.backward(200)  # Move back to start of the row
        designer.right(90)
        designer.forward(40)
        designer.left(90)

# Main function to design the dress
def dress_design():
    draw_bodice()
    draw_skirt()
    add_polka_dots()

# Run the dress design function
dress_design()

# End the Turtle Graphics session
turtle.done()
