import turtle
import webbrowser

# --- Setup the Screen ---
screen = turtle.Screen()
screen.setup(width=900, height=900) # Adjust screen size as needed
screen.bgcolor("black")
screen.title("Interactive Pookalam")
screen.tracer(0) # Turn off screen updates for faster drawing

# --- Main Turtle for Drawing Circles and Flower ---
main_turtle = turtle.Turtle()
main_turtle.speed(0)
main_turtle.hideturtle()
main_turtle.penup()

# --- Function to Draw the Flower in the Center ---
def draw_flower():
    flower_turtle = turtle.Turtle()
    flower_turtle.speed(0)
    flower_turtle.hideturtle()
    flower_turtle.penup()
    
    # Draw petals
    flower_turtle.color("gold")
    for _ in range(12):
        flower_turtle.forward(50)
        flower_turtle.pendown()
        flower_turtle.begin_fill()
        flower_turtle.circle(10)
        flower_turtle.end_fill()
        flower_turtle.penup()
        flower_turtle.backward(50)
        flower_turtle.right(30)
    
    # Draw center of the flower
    flower_turtle.color("white")
    flower_turtle.goto(0, -10)
    flower_turtle.pendown()
    flower_turtle.begin_fill()
    flower_turtle.circle(10)
    flower_turtle.end_fill()
    flower_turtle.penup()

# --- Function to Draw a Clickable Circle ---
def draw_clickable_circle(t, color, radius, link):
    t.penup()
    t.goto(0, -radius) # Position to start drawing the circle from the bottom
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.penup() # Lift pen after drawing

    # Create a small, invisible turtle at the center of this circle to handle clicks
    click_handler_turtle = turtle.Turtle()
    click_handler_turtle.speed(0)
    click_handler_turtle.hideturtle()
    click_handler_turtle.penup()
    # Move the click handler turtle to draw an invisible circle for the click area
    # This ensures the click area matches the drawn circle
    click_handler_turtle.goto(0, -radius)
    click_handler_turtle.pendown()
    click_handler_turtle.circle(radius)
    click_handler_turtle.penup()

    # Define the function to open the link
    def open_link(x, y):
        webbrowser.open(link)
        print(f"Opening {link}") # For debugging

    # Bind the click event to this specific click_handler_turtle's 'hit area'
    click_handler_turtle.onclick(open_link)

# --- Define Circle Parameters ---
circles_data = [
    ("red", 100, "https://tinkerhub.org/@arfan"),
    ("green", 150, "https://tinkerhub.org/@seona"),
    ("yellow", 200, "https://tinkerhub.org/@priya_roy"),
    ("orange", 250, "https://tinkerhub.org/@_angeleena23_")
]

# --- Main Drawing Sequence ---
draw_flower() # Draw the flower first
for color, radius, link in circles_data:
    draw_clickable_circle(main_turtle, color, radius, link)

screen.update() # Update the screen to show all drawings at once
screen.exitonclick()