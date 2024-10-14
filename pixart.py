"""
This module will be used to build the functions that will be borrowed by drawing.py

By using incremental development to create pixal art from the users input, either reading user's string or the  txt file that the user inputted

"""


#  The Constants
PIX_SIZE = 30
NUMBER_COLUMNS = 20
NUMBER_ROWS = 20
DEFAULT_PEN_COLOR = 'black'
DEFAULT_PIXEL_COLOR = 'white'

def initialization(turta):
    """

    This function sets the speed, pencolor, fillcolor, and the starting point of the turtle to start drawing

    """
    turta.speed(0)
    turta.penup()
    turta.goto(-PIX_SIZE * NUMBER_COLUMNS / 2, PIX_SIZE * NUMBER_ROWS / 2)  # the initial coordinate of the turtle
    turta.setheading(0)
    turta.pendown()
    turta.pencolor(DEFAULT_PEN_COLOR)
    turta.fillcolor(DEFAULT_PIXEL_COLOR)

def get_color(character):
    """

    This function returns the corresponding string for the stated character

    """
    if character == "0":
        return "black"
    elif character == "1":
        return "white"
    elif character == "2":
        return "red"
    elif character == "3":
        return "yellow"
    elif character == "4":
        return "orange"
    elif character == "5":
        return "green"
    elif character == "6":
        return "yellowgreen"
    elif character == "7":
        return "sienna"
    elif character == "8":
        return "tan"
    elif character == "9":
        return "gray"
    elif character == "A":
        return "darkgray"
    else:
        return None

def draw_color_pixel(color_string, turta):
    """

    This function will draw one pixel with the specified color

    """
    turta.pendown()
    turta.begin_fill()
    turta.fillcolor(color_string)

    for pixel in range(4):  # will draw a square the size of a pixel
        turta.fd(PIX_SIZE)
        turta.right(90)

    turta.end_fill()
    turta.penup()
    turta.fd(PIX_SIZE)  # positions the turtle forward to draw the next pixel

def draw_pixel(color_string, turta):
    """ 

    This function will draw one pixel with the specified color

    """

    color = get_color(color_string)
    if color:
        draw_color_pixel(color, turta)
    else:
        print("Invalid Input")

def draw_line_from_string(color_string, turta):
    """

    This function will draw one pixel for each character in the string that corresponds to the colors listed in get_color

    """
    for character in color_string:
        color = get_color(character)
        if color:
            draw_pixel(character, turta)
        else:
            return False
    
    # This will move the turtle to the next row
    x_cor = turta.xcor()
    y_cor = turta.ycor()
    turta.goto(-PIX_SIZE * NUMBER_COLUMNS / 2, y_cor - PIX_SIZE)

    return True

def draw_shape_from_string(turta):
    """

    This function asks the user to input color strings in a loop and will draw the corresponding sequence of colored pixels

    """
    while True:
        color_string = input("Please enter a color string: ")
        
        if not color_string:
            break
        elif not draw_line_from_string(color_string, turta):
            print("Invalid color is entered.")
            break

def draw_grid(turta):
    """

    This function draws a 20x20 black and red checkerboard 

    """
    for row in range(NUMBER_ROWS):
        for col in range(NUMBER_COLUMNS):
            color_code = '0' if (row + col) % 2 == 0 else '2'
            draw_pixel(color_code, turta)

        # Moves the turtle to the next row
        turta.penup()
        turta.goto(-PIX_SIZE * NUMBER_COLUMNS / 2, turta.ycor() - PIX_SIZE)
        turta.pendown()

def draw_shape_from_file(turta):
    """

    This function asks the user for which txt file to read. Then it will read its content, and generate a drawing from it
    
    """
    file_path = input("Enter the path of the .txt file you want to read: ")
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()  # remove whitespace(empty spaces)
                if line: 
                    draw_line_from_string(line, turta)  # will draw each line
    except FileNotFoundError:
        print("File not found.")
