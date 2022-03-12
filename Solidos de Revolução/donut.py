from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *


quadro = 360


def drawPoints(points, n, raio):
    # Criando os pontos
    for i in range(0, n):
        theta = i * (2*pi/n) - pi/2
        x = raio * cos(theta)
        y = raio * sin(theta)
        points.append((x, y))


def connectPoints(points, n):
    for i in range(0, n):
        # Gerando o angulo de rotação
        a = ((quadro / n) * i) * pi/2
        glPushMatrix()
        # Rotacionando com base no eixo y
        glRotatef(a, 0, 1, 0)
        # Deslocamento de 1,5 da origem para o eixo x
        glTranslatef(1.5, 0, 0)
        for j in range(0, n):
            glBegin(GL_POINTS)
            glColor3fv(((1.0*(i+1)/(n-1)), 0, 1 - (1.0*(i+1)/(n-1))))
            # Criando os vertices a partir dos pontos
            glVertex3f(points[j][0], points[j][1], 0)
            glEnd()
        glPopMatrix()


def drawDonut():
    glRotatef(1.5, 1, 0, 0)
    raio = 1
    n = 80
    points = []
    drawPoints(points, n, raio)
    connectPoints(points, n)


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
gluPerspective(45.0,  800.0/600.0,  0.1, 100.0)
glTranslatef(0.0, 0.0, -10.0)
glutTimerFunc(10, timer, 1)
glutMainLoop()
