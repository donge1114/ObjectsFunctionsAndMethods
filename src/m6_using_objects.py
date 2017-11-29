"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Enyi Dong.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    circle_and_rectangle()
    lines()


def two_circles():
    window = rg.RoseWindow()
    center_point = rg.Point(100, 100)
    circle_1 = rg.Circle(center_point, 50)

    center_point_2 = rg.Point(200, 200)
    circle_2 = rg.Circle(center_point_2, 80)
    circle_1.fill_color = 'yellow'

    circle_1.attach_to(window)
    circle_2.attach_to(window)

    window.render()
    window.close_on_mouse_click()
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement this function, per its doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # ------------------------------------------------------------------


def circle_and_rectangle():
    window = rg.RoseWindow(500,500)
    x_1 = 300
    y_1 = 300
    center_point = rg.Point(x_1,y_1)
    circle_1 = rg.Circle(center_point, 50)
    circle_1.fill_color = 'blue'
    circle_1.attach_to(window)
    thickness = circle_1.outline_thickness
    color = circle_1.fill_color

    x1 = 100
    y1 = 150
    x2 = 200
    y2 = 50
    point1 = rg.Point(x1, y1)
    point2 = rg.Point(x2, y2)
    rectangle = rg.Rectangle(point1, point2)
    rectangle.attach_to(window)
    x3 = (x1+x2)/2
    y3 = (y1 + y2) / 2
    center_point2 = rg.Point(x3, y3)
    r_thickness = rectangle.outline_thickness
    r_color = rectangle.fill_color


    window.render()

    print(thickness)
    print(color)
    print(center_point)
    print(x_1)
    print(y_1)

    print(r_thickness)
    print(r_color)
    print(center_point2)
    print(x3)
    print(y3)

    window.close_on_mouse_click()

    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # ------------------------------------------------------------------
    # DONE: 3. Implement this function, per its doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # ------------------------------------------------------------------


def lines():

    window = rg.RoseWindow(500,500)
    x1 = 50
    y1 = 250
    x2 = 450
    y2 = 250
    point1 = rg.Point(x1, y1)
    point2 = rg.Point(x2, y2)
    line_1 = rg.Line(point1, point2)
    line_1.thickness = 5
    line_1.attach_to(window)

    x3 = 250
    y3 = 200
    x4 = 250
    y4 = 300
    point3 = rg.Point(x3, y3)
    point4 = rg.Point(x4, y4)
    line_2 = rg.Line(point3, point4)
    line_2.thickness = 10
    line_2.attach_to(window)

    window.render()

    x5 = (x1+x2)/2
    y5 = (y1+y2)/2
    midpoint = rg.Point(x5, y5)
    print(midpoint)
    print(x5)
    print(y5)

    window.close_on_mouse_click()


    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
