def main():
    import turtle               # allows us to use the turtles library
    wn = turtle.Screen()
    bg_color = input("Input background color: ")
    turtle_color = input("Input draw color: ")
    wn.bgcolor(bg_color)       # creates a graphics window
    alex = turtle.Turtle()      # create a turtle named alex
    alex.color(turtle_color)

    for i in range(2):
        alex.forward(150)           # tell alex to move forward by 150 units
        alex.left(90)               # turn by 90 degrees
        alex.forward(75)            # complete the second side of a rectangle
        alex.left(90)

    wn.exitonclick()


main()
