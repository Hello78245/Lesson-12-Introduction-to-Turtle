import turtle
turtle.Screen().bgcolor("Cyan")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()
num_sides=6
side_length=70
angle_sides=360.0/num_sides
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle_sides)
turtle.done()