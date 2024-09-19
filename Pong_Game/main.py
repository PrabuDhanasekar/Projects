import turtle

wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

## player A
Player_A = turtle.Turtle()
Player_A.speed(0)
Player_A.shape("square")
Player_A.color("red")
Player_A.shapesize(stretch_wid=5, stretch_len=1)
Player_A.penup()
Player_A.goto(-350,0)

# #PlayerB
Player_B = turtle.Turtle()
Player_B.speed(0)
Player_B.shape("square")
Player_B.color("red")
Player_B.shapesize(stretch_wid=5, stretch_len=1)
Player_B.penup()
Player_B.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.2
ball.dy = -0.2

# Player_A_moving
def player_A_up():
    y = Player_A.ycor()
    y += 20
    Player_A.sety(y)

def player_A_down():
    y = Player_A.ycor()
    y -= 20
    Player_A.sety(y)

# player_B_moving
def player_B_up():
    y = Player_B.ycor()
    y += 20
    Player_B.sety(y)

def player_B_down():
    y = Player_B.ycor()
    y -= 20
    Player_B.sety(y)

# Pressing keys
wn.listen()
wn.onkeypress(player_A_up, "w")
wn.onkeypress(player_A_down, "s")
wn.onkeypress(player_B_up, "Up")
wn.onkeypress(player_B_down, "Down")

# Main game loop
while True:
    wn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

    # player and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < Player_B.ycor() + 40 and ball.ycor() > Player_B.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < Player_A.ycor() + 40 and ball.ycor() > Player_A.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1