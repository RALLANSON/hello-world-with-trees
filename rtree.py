from turtle import *
from time import perf_counter as clock
"""
 # plist list of pens
 #l is length of branch
 #a is half of the angle between 2 branches
 #f is factor by which branch
 #from level to level.
 """
"3333"
def tree(plist, l, a, f) :
   #print(l)
   if l>7:
     lst=[]
     for p in plist:
         #if p.heading()==90: l*=1.4
         if l<8:
             p.pensize(l)
             p.pencolor(0,255,0)
         else:
            p.pensize(l/10)
            p.pencolor(150,125,0)
         if l>100: p.pencolor(150,75,0)
         if l>150: p.pencolor(100,50,0)
         p. forward(l)
         q = p.clone()
         o=p.clone()
         p.left(a)
         q.right(a)
         lst.append(p)
         lst.append(q)
         lst.append(o)
     for x in tree(lst,l*f,a*0.9,f):
         yield None
def maketree():
 p=Turtle()
 colormode(255)
 p.setundobuffer (None)
 p.hideturtle()
 p.speed(0)
 p.getscreen().tracer(30, 0)
 p.left(90)
 p.penup()
 p.forward(-310)
 p.pendown()
 t=tree([p], 200, 45, 0.6375)
 for x in t:
   pass
def main():
 a=clock()
 maketree()
 b=clock()
 return "done: %.2f sec."%(b-a)
if __name__=="__main__":
  msg = main()
  print(msg)
  mainloop()
