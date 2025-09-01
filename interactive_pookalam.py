import turtle
import webbrowser

# --- Setup the Screen ---
screen = turtle.Screen()
screen.setup(width=900, height=900) # Adjust screen size as needed
screen.bgcolor("black")
screen.title("Interactive Pookalam")
screen.tracer(0) # Turn off screen updates for faster drawing

# --- Main Turtle for Drawing Circles ---
main_turtle = turtle.Turtle()
main_turtle.speed(0)
main_turtle.hideturtle()
main_turtle.penup()

# --- Load the Logo ---
# IMPORTANT:
# 1. Convert your uploaded image to a GIF format (e.g., using an online converter or image editor).
# 2. Save the converted GIF file as 'logo_a.gif' in the SAME DIRECTORY as your Python script.
# If the file is not found or is not a valid GIF, the background will remain black.
logo_filename = "logo_a.gif"
try:
    screen.bgpic(logo_filename)
    print(f"Logo '{logo_filename}' loaded successfully.")
except (turtle.TurtleGraphicsError, turtle.TclError):
    print(f"Warning: Could not load '{logo_filename}'. Please ensure it's a valid GIF and in the script's directory.")
    print("The Pookalam will be drawn on a black background without the logo.")

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
# (color, radius, link)
circles_data = [
    ("red", 100, "https://tinkerhub.org/@arfan"),
    ("green", 150, "https://tinkerhub.org/@seona"),
    ("yellow", 200, "https://tinkerhub.org/@priya_roy"),
    ("orange", 250, "https://tinkerhub.org/@_angeleena23_")
]

# --- Draw the Circles ---
# Starting point for the first circle's radius calculation.
# The logo is at the center, so the first circle's bottom edge will be at -radius.
# The radius values are cumulative for concentric circles.
for color, radius, link in circles_data:
    draw_clickable_circle(main_turtle, color, radius, link)

screen.update() # Update the screen to show all drawings at once
screen.exitonclick()