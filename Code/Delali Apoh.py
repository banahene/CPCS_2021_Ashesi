import turtle

t = turtle.Turtle()

t.getscreen()


def draw_pent(length, angle):
    if length <= 5:
        pass
    else:
        for i in range(10):
            t.forward(length)
            t.left(angle)
        draw_pent(length - 5, angle)
        return draw_pent(length, angle)


pent1 = draw_pent(200, 80)
pent2 = draw_pent(250, 85)

print(pent2)
t.screen.mainloop()
