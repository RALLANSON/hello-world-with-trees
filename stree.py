from turtle import *
from time import perf_counter as clock
"""
 # plist list of pens
 #l is length of branch
 #a is half of the angle between 2 branches
 #f is factor by which branch
 #from level to level.
 """


def maketree():
 p=Turtle()
 p.setundobuffer (None)
 p.hideturtle()
 p.speed(0)
 p.getscreen().tracer(30, 0)
 p.left(90)
 p.penup()
 p.forward(-310)
 p.pendown()
 sl,sa=145,60
 p.forward(sl)
 #       200, 65, 0.6375) a*0.9
 pstak=[]
 pstak.append([p,sl,sa])
 while len(pstak)>0:
    [p,l,a]=pstak.pop(0)
    p.forward(l)
    q=p.clone()
    p.left(a)
    q.right(a)
    if l>7:
     pstak.append([q,l*0.7375,a*0.8])
     pstak.append([p,l*0.7375,a*0.8])

def main():
 a=clock()
 maketree()
 b=clock()
 return "done: %.2f sec."%(b-a)
if __name__=="__main__":
  msg = main()
  print(msg)
  mainloop()
