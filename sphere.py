from visual import *
floor = box(pos=(0,0.25,0), length = 3,height = 0.5, width = 4,color = color.white)
ball = sphere(pos=(0,4,0), color = color.red,radius=0.5)
ball.velocity = vector(0,-1,0)

dt = 0.01
while true:
    rate(30)
    ball.pos = ball.pos + ball.velocity*dt
    if ball.y < 1:
        ball.velocity.y = -ball.velocity.y
    else:
        ball.velocity.y = ball.velocity.y - 9.8*dt
