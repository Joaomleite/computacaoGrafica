from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
from math import *
import sys

a = 0
quadro = 0

def calculaNormalFace(v0, v1, v2):
    x = 0
    y = 1
    z = 2
    U = (v2[x]-v0[x], v2[y]-v0[y], v2[z]-v0[z])
    V = (v1[x]-v0[x], v1[y]-v0[y], v1[z]-v0[z])
    N = ((U[y]*V[z]-U[z]*V[y]),(U[z]*V[x]-U[x]*V[z]),(U[x]*V[y]-U[y]*V[x]))
    NLength = sqrt(N[x]*N[x]+N[y]*N[y]+N[z]*N[z])
    return (N[x]/NLength, N[y]/NLength, N[z]/NLength)
    
def drawBase(raio,  n, a, base, height):
    glBegin(GL_POLYGON)
    auxPosition = height

    for i in range(0, n):
        x = raio * math.cos(i * a)
        y = raio * math.sin(i * a)
        base.append((x, y))
        glVertex3f( x,  y, auxPosition)
        
    u = (base[0][0], base[0][1], auxPosition)
    v = (base[1][0], base[1][1], auxPosition)
    p = (base[2][0], base[2][1], auxPosition)
    glNormal3fv(calculaNormalFace(u,v,p))
    glEnd()



def drawSide(n, height, baseTop, baseBottom):
    glBegin(GL_QUADS)

    for i in range(0, n):
      x_1 = baseBottom[i][0]
      y_1 = baseBottom[i][1]
      
      ligth_coord_1 = (x_1, y_1, 0.0)

      x_2 = baseTop[i][0]
      y_2 = baseTop[i][1]

      ligth_coord_2 = (x_2, y_2, height)

      x_3 = baseTop[(i+1) % n][0]
      y_3 = baseTop[(i+1) % n][1]

      x_4 = baseBottom[(i+1) % n][0]
      y_4 = baseBottom[(i+1) % n][1]    
      ligth_coord_3 = (x_4,y_4, 0.0)

      glNormal3fv(calculaNormalFace(ligth_coord_1,ligth_coord_2,ligth_coord_3))
      glVertex3f(x_1, y_1, 0.0)
      glVertex3f(x_2, y_2, height)
      glVertex3f(x_3, y_3, height)
      glVertex3f(x_4, y_4, 0.0)
    glEnd()

def drawPrisma():
  
    raio = 2
    n_side = 5
    height = 3
    a = (2 * math.pi) / n_side
    baseTop = []
    baseBottom = []
    glPushMatrix()
    glTranslatef(0,-1.2,0)
    glRotatef(quadro,0.0,1.0,0.0)
    glRotatef(-60,1.0,0.0,0.0)

    # BASE BOTTOM
    drawBase(raio, n_side, a, baseBottom, 0)
    
    # BASE TOP
    drawBase(raio, n_side, a, baseTop,  height)
    
     # LADOS
    drawSide(n_side, height, baseTop, baseBottom)

    glPopMatrix()

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(15,timer,1)


def draw():
    global quadro
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    quadro+=1
    drawPrisma()
    glutSwapBuffers()

def reshape(w,h):
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45,float(w)/float(h),0.1,50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(10,0,0,0,0,0,0,1,0)

def init():
    mat_ambient = (0.4, 0.0, 0.0, 1.0)
    mat_diffuse = (1.0, 0.0, 0.0, 1.0)
    mat_specular = (1.0, 0.5, 0.5, 1.0)
    mat_shininess = (50,)
    light_position = (10, 0, 0)
    glClearColor(0.0,0.0,0.0,0.0)
#    glShadeModel(GL_FLAT)
    glShadeModel(GL_SMOOTH)

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_MULTISAMPLE)

# PROGRAMA PRINCIPAL
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(800,600)
    glutCreateWindow("Prisma Iluminado")
    glutReshapeFunc(reshape)
    glutDisplayFunc(draw)
    glEnable(GL_MULTISAMPLE)
    glEnable(GL_DEPTH_TEST)
    gluPerspective(45,800.0/600.0,0.1,100.0)
    glTranslatef(0.0,0.0,20)
    glutTimerFunc(50,timer,1)
    init()
    glutMainLoop()

main()