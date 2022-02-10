from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

cores = ((1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 1, 1),
         (0, 0, 1), (1, 0, 1), (0.5, 1, 1), (1, 0, 0.5))
quadro = 0


def drawBase(raio,  n, a, base, height):
    glColor3f(0.7, 0.7, 0.7)
    glBegin(GL_POLYGON)
    auxPosition = height if height else 0.0

    for i in range(0, n):
        x = raio * math.cos(i * a)
        y = raio * math.sin(i * a)
        base.append((x, y))
        glVertex3f(x, y, auxPosition)
    glEnd()



def drawSide(n, height, baseTop, baseBottom):
    glBegin(GL_QUADS)
    for i in range(0, n):
      glColor3fv(cores[(i + 1) % len(cores)])
      x = baseBottom[i][0]
      y = baseBottom[i][1]
      glVertex3f(x, y, 0.0)
      x = baseBottom[(i+1) % n][0]
      y = baseBottom[(i+1) % n][1]
      glVertex3f(x, y, 0.0)
      y = baseTop[(i+1) % n][1]
      glVertex3f(x, y, height)
      x = baseTop[i][0]
      y = baseTop[i][1]
      glVertex3f(x,  y, height)
    glEnd()

def drawPrisma():
    glRotatef(0.7, 0.0, 1.0, 0.0)
    raio = 0.7
    n_side = 50
    height = 2
    a = (2 * math.pi) / n_side
    baseTop = []
    baseBottom = []
    glPushMatrix()
    
    # BASE BOTTOM
    drawBase(raio, n_side, a, baseBottom, None)

    # BASE TOP
    drawBase(raio, n_side, a, baseTop,  height)
    
     # LADOS
    drawSide(n_side, height, baseTop, baseBottom)

    glPopMatrix()


def draw():
    global quadro
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    drawPrisma()
    glutSwapBuffers()
    quadro += 1


def timer(i):
    glutPostRedisplay()
    glutTimerFunc(15, timer, 1)


# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800, 600)
glutCreateWindow("PRISMA")
glutDisplayFunc(draw)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0., 0., 0., 1.)
gluPerspective(45.0,  800.0/600.0,  0.1, 100.0)
glTranslatef(0.0, 0.0, -7.0)
glutTimerFunc(10, timer, 1)
glutMainLoop()
