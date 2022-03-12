from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
from math import *
import sys

cores = ((1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 1, 1),
         (0, 0, 1), (1, 0, 1), (0.5, 1, 1), (1, 0, 0.5))
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
    

def drawSide(raio, n, cores):
    glBegin(GL_TRIANGLES)
    for i in range(0, n):
        ligth_coord_1 = (0.0, 0.0, -1.0)

        a = (i/n) * 2 * math.pi
        x_1 = raio * math.cos(a)
        y_1 = raio * math.sin(a)
        ligth_coord_2 = (x_1, y_1, 0.0)

        a = ((i+1)/n) * 2 * math.pi
        x_2 = raio * math.cos(a)
        y_2 = raio * math.sin(a)
        ligth_coord_3 = (x_2, y_2, 0.0)

        glNormal3fv(calculaNormalFace(ligth_coord_1,ligth_coord_2,ligth_coord_3))

        glVertex3f(0.0, 0.0, -1.0)
        glVertex3f(x_1, y_1, 0.0)
        glVertex3f(x_2, y_2, 0.0)
    glEnd()


def drawBase(raio, n):
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0.0, 0.0, 0.0)
    basePoints = []
    for i in range(0, n+1):
        a = (i/n) * 2 * math.pi
        x = raio * math.cos(a)
        y = raio * math.sin(a)
        basePoints.append((x,y)) 
        glVertex3f(x, y, 0.0)

    ligth_coord_1 = (basePoints[0][0], basePoints[0][1], 0.0)
    ligth_coord_2 = (basePoints[1][0], basePoints[1][1], 0.0)
    ligth_coord_3 = (basePoints[2][0], basePoints[2][1], 0.0)

    glNormal3fv(calculaNormalFace(ligth_coord_1,ligth_coord_2,ligth_coord_3))
    glEnd()


def drawPiramide():
    glPushMatrix()    
    glTranslatef(6,0.001,0)
    glRotatef(quadro, 0.0, 1.0, 0.0)
    glRotatef(85, 1.0, 0.0, 0.0)
    raio = 1
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
    
def reshape(w,h):
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45,float(w)/float(h),0.1,50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(10,0,0,0,0,0,0,1,0)

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(15,timer,1)

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
    glutCreateWindow("Piramide Iluminada")
    glutReshapeFunc(reshape)
    glutDisplayFunc(draw)
    glEnable(GL_MULTISAMPLE)
    glEnable(GL_DEPTH_TEST)
    gluPerspective(45,800.0/600.0,0.1,100.0)
    glTranslatef(0.0,0.0,0)
    glutTimerFunc(50,timer,1)
    init()
    glutMainLoop()

main()