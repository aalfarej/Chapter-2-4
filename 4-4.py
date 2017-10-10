import turtle
wn = turtle.Screen()
tess = turtle.Turtle()
wn.bgcolor("lightgreen")
tess.color("blue")
tess.pensize(3)


def make_pattern(turt,size,num,angle):
    for i in range(num):
    
        for i in range(4):
            turt.forward(size)
            turt.left(90)
        turt.left(angle)
        
        
make_pattern(tess,200,20,20)
