<<<<<<< HEAD
import turtle

# Function to draw a box
def draw_box():
    box = turtle.Turtle()
    box.color("black")
    box.penup()
    box.goto(-150, 100)  # Starting position for the box
    box.pendown()
    
    # Draw the box
    for _ in range(4):
        box.forward(300)  # Length of the box
        box.right(90)     # Turn 90 degrees
    
    box.hideturtle()  # Hide the box turtle

# Function to display the surprise message
def display_surprise_message():
    message_turtle = turtle.Turtle()
    message_turtle.penup()
    message_turtle.goto(0, 0)  # Center the message
    message_turtle.pendown()
    
    # Display the surprise message
    message_turtle.color("blue")
    message_turtle.write("🎉 Surprise! 🎉\nYou've opened the gift!\nEnjoy your special day!", 
                          align="center", font=("Arial", 18, "bold"))
    
    message_turtle.hideturtle()  # Hide the message turtle

# Function to handle the key press
def open_box():
    display_surprise_message()

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightyellow")

# Draw the box
draw_box()

# Set up key press event to open the box
screen.listen()
screen.onkey(open_box, "space")  # Press space to open the box

# Instructions for the user
instruction_turtle = turtle.Turtle()
instruction_turtle.penup()
instruction_turtle.goto(0, -100)
instruction_turtle.pendown()
instruction_turtle.write("Press SPACE to open the box!", align="center", font=("Arial", 16, "normal"))
instruction_turtle.hideturtle()

# Finish
turtle.done()
=======
import turtle

# Function to draw a box
def draw_box():
    box = turtle.Turtle()
    box.color("black")
    box.penup()
    box.goto(-150, 100)  # Starting position for the box
    box.pendown()
    
    # Draw the box
    for _ in range(4):
        box.forward(300)  # Length of the box
        box.right(90)     # Turn 90 degrees
    
    box.hideturtle()  # Hide the box turtle

# Function to display the surprise message
def display_surprise_message():
    message_turtle = turtle.Turtle()
    message_turtle.penup()
    message_turtle.goto(0, 0)  # Center the message
    message_turtle.pendown()
    
    # Display the surprise message
    message_turtle.color("blue")
    message_turtle.write("🎉 Surprise! 🎉\nYou've opened the gift!\nEnjoy your special day!", 
                          align="center", font=("Arial", 18, "bold"))
    
    message_turtle.hideturtle()  # Hide the message turtle

# Function to handle the key press
def open_box():
    display_surprise_message()

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightyellow")

# Draw the box
draw_box()

# Set up key press event to open the box
screen.listen()
screen.onkey(open_box, "space")  # Press space to open the box

# Instructions for the user
instruction_turtle = turtle.Turtle()
instruction_turtle.penup()
instruction_turtle.goto(0, -100)
instruction_turtle.pendown()
instruction_turtle.write("Press SPACE to open the box!", align="center", font=("Arial", 16, "normal"))
instruction_turtle.hideturtle()

# Finish
turtle.done()
>>>>>>> afb4775 (Initial commit)
