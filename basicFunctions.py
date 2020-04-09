import turtle 
from GHD.Punct import *

turty= turtle.Turtle()
turty.speed(0)
def DeseneazaPunct(P,colour):
    turty.pu()
    turty.setx(P.x)
    turty.sety(P.y)
    turty.pd()
    turty.pencolor(colour) 
    turty.dot(size=3)
    
def draw_axis(s):
    # draws x, y axis
    turty.setpos(0, 0)
    turty.color("black")
    turty.pensize(3)
    for i in range(4):
        turty.fd(s)
        turty.pu()
        turty.goto(0, 0)
        turty.pd()
        turty.lt(90)
    turty.ht()    
    
def draw_segment(P1,P2,colour):
    turty.pu()
    turty.setpos(P1.x,P1.y)
    turty.pencolor(colour)
    turty.pd()
    turty.goto(P2.x,P2.y)
    turty.ht()
    
def PunctRaport(P1,P2,t):

    x=(1-t)*P1.x+t*P2.x 
    y=(1-t)*P1.y+t*P2.y 
    return Punct(x,y)

def DeseneazaPoligon(l,colour):
    
    for i in range(1,len(l)):
        draw_segment(l[i-1],l[i],colour)
        
def PointsSum(P1,P2):
    
    return Punct(P1.x+P2.x,P1.y+P2.y)        
           
def PointsDifference(P1,P2):
    
    return Punct(P1.x-P2.x,P1.y-P2.y)    

def ScalarProduct(n,P):
    
    return Punct(n*P.x,n*P.y)  
    