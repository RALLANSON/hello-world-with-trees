from turtle import *
from time import perf_counter as clock
"""
 # plist list of pens
 #l is length of branch
 #a is half of the angle between 2 branches
 #f is factor by which branch
 #from level to level.
 """
def branch(p,l,a):
    p.forward(l)
    q=p.clone()
    p.left(a)
    q.right(a)
    if l>7:
        branch(p,l*0.7375,a*0.8)
        branch(q,l*0.7375,a*0.8)
    return
def maketree():
 p=Turtle()
 p.setundobuffer (None)
 p.hideturtle()
 p.speed(0)
 p.getscreen().tracer(30, 0)
 p.left(90)
 p.penup()
 p.forward(-300)
 p.pendown()
 sl,sa=145,60
 #p.forward(sl)
 branch(p,sl,sa)

a=clock()
maketree()
b=clock()
print("done: %.2f sec."%(b-a))
a=input("any key quits")
