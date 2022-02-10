from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *


quadro = 360

def drawPoints(points, n, raio):
    for i in range(0,n):
        theta = i* (2*pi/n) - pi/2
        x = raio * cos(theta)
        y = raio * sin(theta)
        points.append((x,y))
    
def drawDonut():
    glRotatef(1.5,1,0,0)
    raio = 0.5
    n = 50
    points = []
    drawPoints(points, n, raio)

    for i in range(0,n):
        a = (quadro/n) * i
        glPushMatrix()
        glRotatef(a,0,1,0)
        glTranslatef(1.5,0,0)
        for j in range(0,n):
            glBegin(GL_POINTS)
            glVertex3f(points[j][0],points[j][1],0)
            glEnd()
        glPopMatrix()


def draw():
    global quadro
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    drawDonut()
    glutSwapBuffers()


def timer(i):
    glutPostRedisplay()
    glutTimerFunc(10, timer, 1)


# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800, 600)
glutCreateWindow("DONUT")
glutDisplayFunc(draw)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0., 0., 0., 1.)
gluPerspective(45.0,  800.0/600.0,  0.1,100.0)
glTranslatef(0.0, 0.0, -10.0)
glutTimerFunc(10, timer, 1)
glutMainLoop()
