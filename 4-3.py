import turtle

def draw_poly(turt, sidenum, sz):
    for i in range(sidenum):
        tess.forward(sz)
        tess.left(360/sidenum)
    
        
tess = turtle.Turtle()   
draw_poly(tess, 8 , 50)

