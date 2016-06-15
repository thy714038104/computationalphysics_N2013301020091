import turtle
import math
bob = turtle.Turtle()
def arc(t,r,angle):
    arc_length = 2.0 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n 
    step_angle = angle / n 
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

def flower(n,r,angle):
    turn_angle = 180 - (360.0 /7)
    for i in range(n):
        arc(bob,r,angle)
        bob.lt(turn_angle)
flower(20,100,180)
turtle.mainloop()
