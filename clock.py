#!/usr/local/bin/python3
#_*_coding: UTF-8 _*_

from turtle import *
from datetime import *
import time


def drawCircle(radius, hour, minute, tick, color):
    pensize(3)
    penup()
    goto(0, radius)
    pendown()
    fillcolor(color)
    pencolor("blue")
    begin_fill()
    for degree in range(0, 360, 360 // minute):
        circle(-radius, 360 // minute)
        rt(90)
        fd(tick / 3)
        bk(tick / 3)
        lt(90)
    end_fill()
    pencolor("purple")
    for degree in range(0, 360, 360 // hour):
        circle(-radius, 360 // hour)
        rt(90)
        fd(tick)
        bk(tick)
        lt(90)
    circle(-radius)


def drawHand(angle, radius, width, color):
    pensize(2)
    penup()
    home()
    fillcolor(color)
    begin_fill()
    lt(90)
    rt(angle)
    fd(radius)
    pendown()
    lt(150)
    fd(width)
    home()
    lt(90)
    rt(angle)
    penup()
    fd(radius)
    pendown()
    rt(150)
    fd(width)
    home()
    end_fill()

goto(-280,300)
write("3학년 6반 최고 !!  ", font=("맑은 고딕",30,"bold"))
shape("turtle")
color("darkblue")
radius = 300
speed(15)
drawCircle(300, 12, 60, radius * .1, "paleturquoise")
c_time = datetime.now().time()
title(c_time.strftime("%H: %M clock"))
drawHand(c_time.minute * 6, radius * .9, radius // 10, "skyblue")
drawHand(((c_time.hour + c_time.minute / 60) % 12) * 30, radius * .6, radius // 10, "purple")

while True:
    new_time = datetime.now().time()
    if c_time.minute is not new_time.minute:
        title(new_time.strftime("%H:%M clock"))
        pencolor("paleturquoise")
        drawHand(c_time.minute * 6, radius * .9, radius // 10, "paleturquoise")
        drawHand(((c_time.hour + c_time.minute / 60) % 12) * 30, radius * .6, radius // 10, "paleturquoise")
        drawHand(new_time.minute * 6, radius * .9, radius // 8, "skyblue")
        drawHand(((new_time.hour + new_time.minute / 60) % 12) * 30, radius * .6, radius // 8, "purple")
    c_time = new_time
    time.sleep(60)






