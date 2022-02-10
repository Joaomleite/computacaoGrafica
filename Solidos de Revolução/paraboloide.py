from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math


quadro = 0

def drawSide(n, rf, r0):
    glBegin(GL_POINTS)
    for i in range(0, n):
        r = i * (rf - r0)/n + r0
        for j in range(0,n):
            glColor3fv(((1.0*(i+1)/(50-1)),0,1 - (1.0*(i+1)/(50-1))))
            phi = (j * math.pi)/ n
            x = r * math.cos(phi) 
            y = r**2
            z = r * math.sin(phi)
            glVertex3f(x,y,z)
    glEnd()


def drawParaboloide():
    glPushMatrix()
    glRotatef(quadro, 1, 0, 0)
    n_sides = 50
    r_inicial= -2
    r_final= 2

    drawSide(n_sides, r_inicial, r_final)
    glPopMatrix()


def draw():
    global quadro
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    drawParaboloide()
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
glTranslatef(0.0, 0.0, -10.0)
glutTimerFunc(10, timer, 1)
glutMainLoop()
