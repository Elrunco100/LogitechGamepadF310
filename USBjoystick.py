import pygame
import numpy as npm

#initialize pygame to start
pygame.init()
clock=pygame.time.Clock()
pygame.joystick.init()

#enumerate the joysticks enable
joystick_count=pygame.joystick.get_count()

for i in range(joystick_count):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()

#obtain data about joystick
name =  joystick.get_name()
axes =  joystick.get_numaxes()
buttons=joystick.get_numbuttons()
hat =   joystick.get_numhats()

print(name)
while True:
    #call events
    event = pygame.event.get()

        #axis data
    XL=     joystick.get_axis(0)
    YL=     joystick.get_axis(1)
    TL=     joystick.get_axis(2)
    XR=     joystick.get_axis(3)
    YR=     joystick.get_axis(4)
    TR=     joystick.get_axis(5)
        #Buttons data
    a=      joystick.get_button(0)
    b=      joystick.get_button(1)
    x=      joystick.get_button(2)
    y=      joystick.get_button(3)
    l=      joystick.get_button(4)
    r=      joystick.get_button(5)
    back=   joystick.get_button(6)
    start=  joystick.get_button(7)
    logitec=joystick.get_button(8)
    axisl=  joystick.get_button(9)
    axisr=  joystick.get_button(10)
        #hat data
    arrow=   joystick.get_hat(0)

    print (XL)
