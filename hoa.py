import turtle
quynh=turtle.Turtle()
quynh.screen.bgcolor("pink")
quynh.pensize(4.25)
quynh.color("green")
quynh.left(90)
quynh.backward(80)
quynh.speed(0)
quynh.shape("triangle")
def tree(i):
    if i<5:
        return
    else:
        quynh.forward(i)
        quynh.color("hotpink")
        quynh.circle(6)
        quynh.color("green")
        quynh.left(300)
        tree(2*i/4)
        quynh.right(600)
        tree(3*i/4)
        quynh.left(300)
        quynh.backward(i)
tree(130)
turtle.done()
