import turtle
sn = turtle.Screen()
sn.bgcolor("light green")
ali = turtle.Turtle()
ali.color("blue")
ali.pensize(3)

def draw_spiral(turt,sz,space):
    """
    draws on sprial
    """
    
    for i in range (75):
        sz = sz + space
        turt.right(90)
        turt.forward(sz)
        
draw_spiral(ali,5,5)
        
        
   
    
