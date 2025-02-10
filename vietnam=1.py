import turtle
screen = turtle.Screen()
screen.bgcolor('white')
star= turtle.Turtle()
star.speed(5)

#Ham ve ngoi sao
def draw_star(size):
    star.color('yellow')
    star.begin_fill()
    for _ in range(5):
        star.forward(size)
        star.right(144)
        star.forward(size)
        star.left(72)
    star.end_fill()
    
    #Ham ve hinh chu nhat
def draw_rectangle(width, height):
    star.color('red')
    star.penup()
    star.goto(-width/2, height/2)#vi tri bat dau ve hinh chu nhat
    star.pendown()
    star.begin_fill()
    for _ in range(2):
        star.forward(width)
        star.right(90)
        star.forward(height)
        star.right(90)
    star.end_fill()
    
rectangle_width=600
rectangle_height=400
draw_rectangle(rectangle_width, rectangle_height)

star.penup()
star.goto(25, 20)
star.pendown()
draw_star(100)
star.hideturtle()
turtle.done()



