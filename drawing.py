"""
This module imports the screen, turtle, and all necessary functions from pixart to either draw a 20x20
black and red checkerboard, draw pixels of corresponding color from pixels, or draw from a file.
"""

from turtle import Screen, Turtle
from pixart import initialization, draw_shape_from_string, draw_shape_from_file, draw_grid

def main():
    """
    The functions here are borrowed from the module pixart.
    Initialization will boot the the turtle graphic.
    draw_shape_from_string will draw colored pixels based on the users input and break if invalid
    draw_grid will draw a checkered grid
    """
    # Set up the turtle screen
    sc = Screen()
    turta = Turtle()
    turta.speed(0)
    # starts turtle
    initialization(turta)
    
    # Uncomment the following to draw pixels from user input
    #draw_shape_from_string(turta)

    # Uncomment the following line to draw a grid 
    #draw_grid(turta)

    # Uncomment the following line to draw from a file
    #draw_shape_from_file(turta)

    sc.exitonclick()  

if __name__ == "__main__":
    main()
