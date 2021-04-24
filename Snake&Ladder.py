import turtle
import tkinter
from tkinter import PhotoImage

turtle.speed(10)  # Speed of the turtle pen
turtle.pensize(2)  # pen size for turtle
turtle.title("Snakes and ladders")  # Giving the window custom name
turtle.setup(1100, 1100, 0, 0)  # screen size of turtle window
turtle.hideturtle()  # Hiding the turtle pen
turtle.bgcolor("ivory")  # background colour of turtle window
turtle.penup()
turtle.goto(-300, -300)
turtle.pendown()



def outersquare():  # Name of function for drawing of board
    for i in range(4):  # This will repeat the loop x4 making an outskirts of board
        turtle.forward(600)  # turtle drawing one line of the outskirt of board
        turtle.left(90)  # turtle pointer turning left and plans to draw the next outskirt
    for i in range(2):  # Loop done twice to make verticle lines
        turtle.forward(120)
        turtle.left(90)
        turtle.forward(600)
        turtle.right(90)
        turtle.forward(120)
        turtle.right(90)
        turtle.forward(600)
        turtle.left(90)
    turtle.forward(120)
    for i in range(2):  # Loop done twice to make horizontal lines
        turtle.left(90)
        turtle.forward(120)
        turtle.left(90)
        turtle.forward(600)
        turtle.right(90)
        turtle.forward(120)
        turtle.right(90)
        turtle.forward(600)


def digitrows():  # Function to display the numbers in rows on the board
    turtle.penup()
    turtle.goto(-300, -200)
    turtle.pendown()

    for i in range(5):
        turtle.penup()
        turtle.write(i + 1, align="left", font=("Calibri", 18))
        turtle.forward(120)

    turtle.penup()
    turtle.goto(-300, -80)
    turtle.pendown()

    for i in range(10, 5, -1):
        turtle.penup()
        turtle.write(i, align="left", font=("Calibri", 18))
        turtle.forward(120)

    turtle.penup()
    turtle.goto(-300, 40)
    turtle.pendown()

    for i in range(11, 16):
        turtle.penup()
        turtle.write(i, align="left", font=("Calibri", 18))
        turtle.forward(120)

    turtle.penup()
    turtle.goto(-300, 160)
    turtle.pendown()

    for i in range(20, 15, -1):
        turtle.penup()
        turtle.write(i, align="left", font=("Calibri", 18))
        turtle.forward(120)

    turtle.penup()
    turtle.goto(-300, 280)
    turtle.pendown()

    for i in range(21, 26):
        turtle.penup()
        turtle.write(i, align="left", font=("Calibri", 18))
        turtle.forward(120)


from turtle import *

screen = Screen()

def photo_snakes():  # Function for inserting the snake images
    image1 = Turtle()
    screen.addshape("./icons/snake.gif")
    # print(screen.getshapes())
    image1.shape("./icons/snake.gif")
    image1.speed(4)

    image2 = Turtle()
    screen.addshape("./icons/snake2.gif")
    # print(screen.getshapes())
    image2.shape("./icons/snake2.gif")
    image2.speed(4)

    image3 = Turtle()
    screen.addshape("./icons/snake3.gif")
    # print(screen.getshapes())
    image3.shape("./icons/snake3.gif")
    image3.speed(4)

    image1.penup()
    image1.goto(130, 110)
    image2.penup()
    image2.goto(10, -170)
    image3.penup()
    image3.goto(-250, -50)


def photo_ladders():  # Function for inserting the ladder images
    photo1 = Turtle()
    screen.addshape("./icons/ladder.gif")
    # print(screen.getshapes())
    photo1.shape("./icons/ladder.gif")
    photo1.speed(4)

    photo2 = Turtle()
    screen.addshape("./icons/ladder2.gif")
    # print(screen.getshapes())
    photo2.shape("./icons/ladder2.gif")
    photo2.speed(4)

    photo3 = Turtle()
    screen.addshape("./icons/ladder3.gif")
    # print(screen.getshapes())
    photo3.shape("./icons/ladder3.gif")
    photo3.speed(4)

    photo1.penup()
    photo1.goto(-10, 170)
    photo2.penup()
    photo2.goto(-110, -80)
    photo3.penup()
    photo3.goto(220, -110)

def photo_cow(row, col):  # Function for inserting the Cow image
    photocow.penup()
    photocow.goto(row, col)

def photo_bull(row, col):  # Function for inserting the Bull image
    photobull.penup()
    photobull.goto(row, col)

def diceimage_p1(d):
    dice1.shape(f"./icons/dice{d}.gif")
    dice1.speed(4)
    dice1.penup()
    dice1.goto(-400, -240)

def diceimage_p2(d):
    dice2.shape(f"./icons/dice{d}.gif")
    dice2.speed(4)
    dice2.penup()
    dice2.goto(400, -240)

def win_image():
    if player_1 is 25:
        win_img = PhotoImage(file="./icons/win.gif").zoom(1,1).subsample(3,3)
        screen.addshape("win_img", Shape("image", win_img))
        win = Turtle("win_img")
        win.penup()
        win.shape('win_img')
        win.goto(-360, 0)

    elif player_2 is 25:
        win_img = PhotoImage(file="./icons/win.gif").zoom(1,1).subsample(3,3)
        screen.addshape("win_img", Shape("image", win_img))
        win = Turtle("win_img")
        win.penup()
        win.shape('win_img')
        win.goto(360, 0)

import random

t2 = turtle.Turtle()
t2.penup()
t2.goto(-300, -300)

def turn():
    if Player:
        arrow.penup()
        arrow.goto(-400, 0)
    else:
        arrow.penup()
        arrow.goto(400, 0)
def roll_dice():
    rolldice = random.randint(1, 6)
    # print(rolldice)
    return rolldice

outersquare()
digitrows()
photo_snakes()
photo_ladders()

photobull = Turtle()
screen.addshape("./icons/bull.gif")
# print(screen.getshapes())
photobull.shape("./icons/bull.gif")
photobull.speed(2)

photocow = Turtle()
screen.addshape("./icons/cow.gif")
# print(screen.getshapes())
photocow.shape("./icons/cow.gif")
photocow.speed(2)

photo_cow(-240,-240)
photo_bull(-240,-240)

dice1 = turtle.Turtle()
screen.addshape("./icons/dice1.gif")
screen.addshape("./icons/dice2.gif")
screen.addshape("./icons/dice3.gif")
screen.addshape("./icons/dice4.gif")
screen.addshape("./icons/dice5.gif")
screen.addshape("./icons/dice6.gif")

dice2 = turtle.Turtle()
screen.addshape("./icons/dice1.gif")
screen.addshape("./icons/dice2.gif")
screen.addshape("./icons/dice3.gif")
screen.addshape("./icons/dice4.gif")
screen.addshape("./icons/dice5.gif")
screen.addshape("./icons/dice6.gif")


arrow_img = PhotoImage(file="./icons/arrow.gif").zoom(1,1).subsample(3,3)
screen.addshape("arrow_img", Shape("image", arrow_img))
arrow = Turtle("arrow_img")
arrow.speed(5)

# print(turtle.getshapes())
Player = 1

diceimage_p1(1)
diceimage_p2(1)
turn()

cor = {
    '1' : (-240, -240),
    '2' : (-120, -240),
    '3' : (0, -240),
    '4' : (120, -240),
    '5' : (240, -240),      # goto 15 ladder
    '6' : (240, -120),
    '7' : (120, -120),
    '8' : (0, -120),        # goto 3 Snake
    '9' : (-120, -120),     # goto 12 ladder
    '10' : (-240, -120),
    '11' : (-240, 0),
    '12' : (-120, 0),
    '13' : (0, 0),
    '14' : (120, 0),
    '15' : (240, 0),
    '16' : (240, 120),
    '17' : (120, 120),
    '18' : (0, 120),        # goto 23 ladder
    '19' : (-120, 120),
    '20' : (-240, 120),     # goto 1 Snake
    '21' : (-240, 240),
    '22' : (-120, 240),
    '23' : (0, 240),
    '24' : (120, 240),      # goto 14 Snake
    '25' : (240, 240),
}

ladders={
    '5': '15',  # goto 15 ladder
    '9': '12',  # goto 12 ladder
    '18': '23',  # goto 23 ladder
}
snakes={
    '8': '3',  # goto 3 Snake
    '20': '1',  # goto 1 Snake
    '24': '14',  # goto 14 Snake
}


player_1=1
player_2=1

def up():
    global Player
    global player_1, player_2
    global arrow
    if Player:
        d = roll_dice()
        diceimage_p1(d)
        if sum([player_1,d]) <= 25:
            player_1 += d
            # print("Player-1")
            for i in range(player_1 - d, player_1+1):
                photo_bull(cor.get(str(i))[0], cor.get(str(i))[1])

            if str(player_1) in ladders.keys():
                player_1 = int(ladders.get(str(player_1)))
                photo_bull(cor.get(str(player_1))[0], cor.get(str(player_1))[1])

            if str(player_1) in snakes.keys():
                player_1 = int(snakes.get(str(player_1)))
                photo_bull(cor.get(str(player_1))[0], cor.get(str(player_1))[1])
        win_image()
        Player = 0
        turn()

    else:
        d = roll_dice()
        diceimage_p2(d)

        if sum([player_2,d]) <= 25:
            player_2 += d
            # print("Player-2")
            for i in range(player_2 - d, player_2+1):
                photo_cow(cor.get(str(i))[0], cor.get(str(i))[1])

            if str(player_2) in ladders.keys():
                player_2 = int(ladders.get(str(player_2)))
                photo_cow(cor.get(str(player_2))[0], cor.get(str(player_2))[1])

            if str(player_2) in snakes.keys():
                player_2 = int(snakes.get(str(player_2)))
                photo_cow(cor.get(str(player_2))[0], cor.get(str(player_2))[1])

        win_image()
        Player = 1
        turn()

screen.listen()
screen.onkey(up, "Up")

tkinter.mainloop()

