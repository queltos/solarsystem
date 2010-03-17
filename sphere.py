#!/usr/bin/env python

from pyglet import window
from OpenGL.GL import *
from OpenGL.GLU import *

from time import sleep

def myinit():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    global q
    q = gluNewQuadric();
    glEnable(GL_DEPTH_TEST)
    glPolygonMode( GL_FRONT_AND_BACK, GL_LINE)
    #glPolygonMode( GL_FRONT_AND_BACK, GL_FILL)
    
def myresize(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1.0*width/height, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def mydisplay():
    global t
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  
    glLoadIdentity()
    gluLookAt(0.0, 2.0, 4.0,  # eye
              0.0, 0.0, -1.0, # center
              0.0, 1.0, 0.0)  # up

#    glPushMatrix()

    #glRotatef((3*t) % 360,0,1,0)
    glColor(0,1,1)
    gluSphere(q, 0.4, 20, 20)

    """
    glRotatef(t % 360,0,1,0)
    glTranslatef(1,0,0)
    glColor3f(1,0,0)
    gluSphere(q,0.3,50,50)

    glPushMatrix()

    glRotatef((10 * t) % 360,0,1,0)
    glTranslatef(0.6,0,0)
    glColor3f(1,1,0)
    gluSphere(q,0.2,50,50)

    glPopMatrix()


    glPushMatrix()
    glRotatef(30,0,0,1)

    glRotatef((16 * t) % 360,0,1,0)
    glTranslatef(0.8,0,0)
    glColor3f(1,0,1)
    gluSphere(q,0.15,50,50)

    glPopMatrix()
    """

    
def main():
    win = window.Window()
    win.on_resize = myresize
    myinit()

    global t
    t = 0.0
    speed = 0.5

    while not win.has_exit:
        win.dispatch_events()
        mydisplay()
        win.flip()
	t += speed
	sleep(0.01)

if __name__ == "__main__":
    main()
