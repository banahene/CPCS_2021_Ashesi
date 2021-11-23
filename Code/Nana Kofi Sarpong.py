# a program that creates an interesting picture using recursion - neon tree with fruits
import turtle

# turtle object
t = turtle.Turtle()

# increasing speed of drawing by 12
fasterspeed = t.speed() * 12
t.speed(fasterspeed)

# changing screen color to black
turtle.Screen().bgcolor("black")

# the shortest length of a branch
min_branch_length = 5


# the build_tree function builds a tree with fruits on it
# by making branches if the branch length is greater than the minimum branch length

def neon_build_tree(branch_len, shorten_by, angle):
    if branch_len > min_branch_length:

        # creating a branch with a given length
        t.forward(branch_len)

        # filling circle color
        t.fillcolor("medium spring green")
        t.begin_fill()
        # creating the fruits
        t.circle(2.5)
        t.end_fill()

        # creates a new, shorter length as a branch
        new_length = branch_len - shorten_by
        t.left(angle)

        # the new, shorter length becomes a branch with branches on it
        neon_build_tree(new_length, shorten_by, angle)

        t.right(angle * 2)
        # shorter length becomes a branch with branches on it but with an angle multiplied by 2
        neon_build_tree(new_length, shorten_by, angle)
        t.left(angle)

        t.backward(branch_len)


# sets the orientation of the turtle to 90 degrees
t.setheading(90)
# changing color of branch
t.color('greenyellow')

neon_build_tree(30, 5, 30)


def neon_build_tree(branch_len, shorten_by, angle):
    if branch_len > min_branch_length:
        t.forward(branch_len)
        t.fillcolor("orange")
        t.begin_fill()
        t.circle(2.5)
        t.end_fill()
        new_length = branch_len - shorten_by
        t.left(angle)
        neon_build_tree(new_length, shorten_by, angle)
        t.right(angle * 2)
        neon_build_tree(new_length, shorten_by, angle)
        t.left(angle)
        t.backward(branch_len)


t.setheading(180)
t.color('blue')

neon_build_tree(50, 5, 30)


def neon_build_tree(branch_len, shorten_by, angle):
    if branch_len > min_branch_length:
        t.forward(branch_len)
        t.fillcolor("maroon1")
        t.begin_fill()
        t.circle(2.5)
        t.end_fill()
        new_length = branch_len - shorten_by
        t.left(angle)
        neon_build_tree(new_length, shorten_by, angle)
        t.right(angle * 2)
        neon_build_tree(new_length, shorten_by, angle)
        t.left(angle)
        t.backward(branch_len)


t.setheading(270)
t.color('orange')

neon_build_tree(30, 5, 30)


def neon_build_tree(branch_len, shorten_by, angle):
    if branch_len > min_branch_length:
        t.forward(branch_len)
        t.fillcolor("yellow")
        t.begin_fill()
        t.circle(2.5)
        t.end_fill()
        new_length = branch_len - shorten_by
        t.left(angle)
        neon_build_tree(new_length, shorten_by, angle)
        t.right(angle * 2)
        neon_build_tree(new_length, shorten_by, angle)
        t.left(angle)
        t.backward(branch_len)


t.setheading(0)
t.color('red')

neon_build_tree(50, 5, 30)
turtle.mainloop()
