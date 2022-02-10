from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

cores = ((1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 1, 1),
         (0, 0, 1), (1, 0, 1), (0.5, 1, 1), (1, 0, 0.5))
quadro = 0


def drawSide(raio, n, cores):
    glBegin(GL_TRIANGLES)
    for i in range(0, n):
        glColor3fv(cores[(i) % len(cores)])
        glVertex3f(0.0, 0.0, -1.0)
        a = (i/n) * 2 * math.pi
        x = raio * math.cos(a)
        y = raio * math.sin(a)
        glVertex3f(x, y, 0.0)
        a = ((i+1)/n) * 2 * math.pi
        x = raio * math.cos(a)
        y = raio * math.sin(a)
        glVertex3f(x, y, 0.0)
    glEnd()


def drawBase(raio, n):
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0.3, 0.3, 0.3)
    glVertex3f(0.0, 0.0, 0.0)
    for i in range(0, n+1):
        a = (i/n) * 2 * math.pi
        x = raio * math.cos(a)
        y = raio * math.sin(a)
        glVertex3f(x, y, 0.0)
    glEnd()


def drawPiramide():
    glPushMatrix()
    glRotatef(50+quadro, 1.0, 0.0, 0.0)
    raio = 0.7
    n_sides = 3

    # SIDES
    drawSide(raio, n_sides, cores)

    # BASE
    drawBase(raio, n_sides)
    glPopMatrix()


def draw():
    global quadro
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    drawPiramide()
    glutSwapBuffers()
    quadro += 1


def timer(i):
    glutPostRedisplay()
    glutTimerFunc(10, timer, 1)


# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800, 600)
glutCreateWindow("PIRÂMIDE")
glutDisplayFunc(draw)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0., 0., 0., 1.)
gluPerspective(45.0,  800.0/600.0,  0.1,       100.0)
glTranslatef(0.0, 0.0, -5.0)
glutTimerFunc(10, timer, 1)
glutMainLoop()
