import turtle
import random
import time

# Setup the screen
screen = turtle.Screen()
screen.title("Diwali Wishes from Your Friend Turtle")
screen.bgcolor("black")
screen.setup(width=800, height=600)

# Create our friend turtle for the wishes
friend_turtle = turtle.Turtle()
friend_turtle.shape("turtle")
friend_turtle.color("green")
friend_turtle.speed(1)
friend_turtle.pensize(3)

# Create a turtle for fireworks
firework_turtle = turtle.Turtle()
firework_turtle.hideturtle()
firework_turtle.speed(0)

# Turtle for writing text
text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.speed(0)
text_turtle.color("yellow")

# Function for friend turtle to draw a Diya (lamp)
def draw_diya(t):
    t.penup()
    t.goto(-30, -200)
    t.pendown()
    t.color("orange", "yellow")
    t.begin_fill()
    t.left(140)
    t.forward(180)
    t.circle(-90, 200)
    t.left(120)
    t.circle(-90, 200)
    t.forward(180)
    t.end_fill()
    
    # Draw the flame
    t.penup()
    t.goto(0, -30)
    t.pendown()
    t.color("red", "orange")
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    t.penup()

# Function to draw fireworks
def draw_firework(x, y):
    firework_turtle.penup()
    firework_turtle.goto(x, y)
    firework_turtle.pendown()
    firework_turtle.color(random.choice(["red", "blue", "green", "yellow", "purple", "orange"]))
    
    # Draw the firework burst
    for _ in range(36):
        firework_turtle.forward(50)
        firework_turtle.backward(50)
        firework_turtle.left(10)

# Function to show fireworks animation
def show_fireworks():
    for _ in range(8):  # Number of fireworks
        x = random.randint(-300, 300)
        y = random.randint(0, 250)
        draw_firework(x, y)
        firework_turtle.clear()
        time.sleep(0.3)

# Function to display a Diwali message
def display_wish():
    text_turtle.penup()
    text_turtle.goto(0, -100)
    text_turtle.color("yellow")
    text_turtle.write("Happy Diwali!", align="center", font=("Arial", 36, "bold"))
    
    text_turtle.goto(0, -150)
    text_turtle.color("lightgreen")
    text_turtle.write("May your life be as colorful as these fireworks!", align="center", font=("Arial", 24, "italic"))

# Main animation function
def diwali_wishing_animation():
    # Friend turtle introduces the greeting
    friend_turtle.penup()
    friend_turtle.goto(-300, 0)
    friend_turtle.pendown()
    friend_turtle.color("white")
    friend_turtle.write("Hello, I'm your friend Turtle!", align="left", font=("Arial", 16, "normal"))
    
    time.sleep(1)
    
    # Draw Diya with friend turtle
    friend_turtle.penup()
    friend_turtle.goto(-50, -200)
    friend_turtle.pendown()
    friend_turtle.color("green")
    friend_turtle.write("Let's light a Diya for Diwali!", align="left", font=("Arial", 16, "normal"))
    time.sleep(1)
    draw_diya(friend_turtle)
    
    time.sleep(1)
    
    # Fireworks animation
    show_fireworks()
    
    # Display Diwali wishes
    display_wish()

# Run the Diwali wishing animation
diwali_wishing_animation()
turtle.done()
