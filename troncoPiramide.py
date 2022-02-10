from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math


cores = ((1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 1, 1),
         (0, 0, 1), (1, 0, 1), (0.5, 1, 1), (1, 0, 0.5))
quadro = 0


def drawSide(n, cores, baseTop, baseBottom, h):
    # Gerando os pontos e vertices dos lados a partir dos valores das bases 
    glBegin(GL_QUAD_STRIP)
    for i in range(0, n):
        glColor3fv(cores[(i) % len(cores)])
        x = baseBottom[i][0]
        y = baseBottom[i][1]
        glVertex3f(x, y, 0.0)
        x = baseBottom[(i+1) % n][0]
        y = baseBottom[(i+1) % n][1]
        glVertex3f(x, y, 0.0)
        x = baseTop[i][0]
        y = baseTop[i][1]
        glVertex3f(x, y, h)
        x = baseTop[(i+1) % n][0]
        y = baseTop[(i+1) % n][1]
        glVertex3f(x, y, h)
    glEnd()


def drawBase(raio, n, base, h):
    glVertex3f(0.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    a =  (2 * math.pi) / n
    zPosition = h if h else 0.0
    glColor3f(0.3, 0.3, 0.3)

    ## Gerando os pontos e vertices da base especifica
    for i in range(0, n):
        x = raio * math.cos(i * a) 
        y = raio * math.sin(i * a) 
        base.append((x,y))
        glVertex3f(x, y, zPosition)
    glEnd()


def drawTroncoPiramide():
    glPushMatrix()
    glRotatef(50+quadro, 1.0, 0.0, 0.0)

    # A ideia é a mesma do Prisma, porém, nesse modelo devemos ter dois raios, um maior e menor, 
    # para podermos desenhar o tronco da piramide corretamente
    raio1 = 4
    raio2 = 2
    n_sides = 3
    height = 2
    baseTop = []
    baseBottom = []

    # BASE BOTTOM
    drawBase(raio1, n_sides, baseBottom, None)

    # BASE TOP
    drawBase(raio2, n_sides, baseTop, height)

    # SIDES
    drawSide(n_sides, cores, baseTop, baseBottom, height)

    glPopMatrix()


def draw():
    global quadro
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    drawTroncoPiramide()
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
glTranslatef(0.0, 0.0, -15.0)
glutTimerFunc(10, timer, 1)
glutMainLoop()
