"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Aaron Wilkin, their colleagues, and John Neill.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:

    #two_circles()
    #circle_and_rectangle()
    lines()

def two_circles():

    window = rg.RoseWindow()

    circle = rg.Circle(rg.Point(100, 100), 50)
    circle1 = rg.Circle(rg.Point(200, 200), 25)
    circle.fill_color = 'red'

    circle.attach_to(window)
    circle1.attach_to(window)

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
    # -------------------------------------------------------------------------
    # DONE: 2. Implement this function, per its green doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.pdf  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # -------------------------------------------------------------------------


def circle_and_rectangle():

    window = rg.RoseWindow()

    alexeileonov = rg.Circle(rg.Point(200, 200), 50)
    Влади́мирВлади́мировичПу́тин = rg.Rectangle(rg.Point(20, 100), rg.Point(100, 200))
    alexeileonov.fill_color = 'blue'
    Влади́мирВлади́мировичПу́тин.fill_color = 'red'
    print(alexeileonov.outline_thickness)
    print(alexeileonov.fill_color)
    print(alexeileonov.center)
    print(alexeileonov.center.x)
    print(alexeileonov.center.y)

    print(Влади́мирВлади́мировичПу́тин.outline_thickness)
    print(Влади́мирВлади́мировичПу́тин.fill_color)
    print(Влади́мирВлади́мировичПу́тин.get_center())
    print(Влади́мирВлади́мировичПу́тин.get_center().x)
    print(Влади́мирВлади́мировичПу́тин.get_center().y)




    alexeileonov.attach_to(window)
    Влади́мирВлади́мировичПу́тин.attach_to(window)
    window.render()
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
    # -------------------------------------------------------------------------
    # DONE: 3. Implement this function, per its green doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # -------------------------------------------------------------------------


def lines():

    window = rg.RoseWindow()

    товарищсталин = rg.Line(rg.Point(20, 70), rg.Point(100, 250))
    товарищЛенин = rg.Line(rg.Point(40, 10), rg.Point(275, 80))
    товарищсталин.thickness = 40
    gloriousmidpoint = товарищсталин.get_midpoint()
    print(gloriousmidpoint)
    print(gloriousmidpoint.x)
    print(gloriousmidpoint.y)

    товарищсталин.attach_to(window)
    товарищЛенин.attach_to(window)
    window.render()
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
    # DONE: 4. Implement and test this function.


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
