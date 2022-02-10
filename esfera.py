from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math


quadro = 0

def drawSide(raio, n):
    glBegin(GL_POINTS)
    for i in range(0, n):
        theta = (i * math.pi/n) - math.pi/2
        for j in range(0,n):
            phi = (j * 2 * math.pi)/ n
            x = raio * math.cos(theta) * math.cos(phi)
            y = raio * math.sin(theta)
            z = raio * math.cos(theta) * math.sin(phi)
            glVertex3f(x,y,z)
    glEnd()


def drawEsfera():
    raio = 1
    n_sides = 50
    glPushMatrix()
    glRotatef(quadro, 1, 0, 0)
    drawSide(raio, n_sides)
    glPopMatrix()


def draw():
    global quadro
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    drawEsfera()
    glutSwapBuffers()
    quadro += 1


def timer(i):
    glutPostRedisplay()
    glutTimerFunc(10, timer, 1)


# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800, 600)
glutCreateWindow("ESFERA")
glutDisplayFunc(draw)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0., 0., 0., 1.)
gluPerspective(45.0,  800.0/600.0,  0.1,100.0)
glTranslatef(0.0, 0.0, -5.0)
glutTimerFunc(10, timer, 1)
glutMainLoop()
