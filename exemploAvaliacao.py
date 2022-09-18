#https://www.youtube.com/watch?v=a4NVQC_2S2U&t=64s&ab_channel=NaseemShah
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

global x1,y1, x2,y2, x3,y3, xstep, ystep, rsize, windowWidth, windowHeight

x1, y1 = 0, 0
x2, y2 = 0, 0
x3, y3 = 0, 0

xstep = 0.1
ystep = 0.1

windowWidth = 200
windowHeight = 400

rsize = 5


def DesenhaBrasil(flagSize, x = 0, y = 0):
  glColor3f(0,.5,0)
  glBegin(GL_QUADS)

  glVertex2f(-1*flagSize + x,-1*flagSize + y)
  glVertex2f(-1*flagSize + x,1*flagSize + y)
  glVertex2f(1*flagSize + x,1*flagSize + y)
  glVertex2f(1*flagSize + x,-1*flagSize + y)

  glEnd()

  glColor3f(.8,.8,0)
  glBegin(GL_QUADS)

  glVertex2f(-1*flagSize/1.5 + x,0*flagSize/1.5 + y)
  glVertex2f(0*flagSize/1.5 + x,1*flagSize/1.5 + y)
  glVertex2f(1*flagSize/1.5 + x,0*flagSize/1.5 + y)
  glVertex2f(0*flagSize/1.5 + x,-1*flagSize/1.5 + y)

  glEnd()
  
  glColor3f(.0,.0,5)
  glBegin(GL_QUADS)
  
  glVertex2f(-1*flagSize/6 + x,-1*flagSize/6 + y)
  glVertex2f(-1*flagSize/6 + x,1*flagSize/6 + y)
  glVertex2f(1*flagSize/6 + x,1*flagSize/6 + y)
  glVertex2f(1*flagSize/6 + x,-1*flagSize/6 + y)

  glEnd()

def Desenha():
  global x1,y1, x2,y2, x3,y3, xstep, ystep, rsize, windowWidth, windowHeight

  glClear(GL_COLOR_BUFFER_BIT)

  glViewport(0,int(windowHeight/2),windowWidth,int(windowHeight / 2))
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  gluOrtho2D(-rsize,rsize,-rsize,rsize)
  DesenhaBrasil(1, x1, y1)

  glViewport(0,0,int(windowWidth/2),int(windowHeight / 2))
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  gluOrtho2D(-rsize,rsize,-rsize,rsize)
  DesenhaBrasil(4)

  glViewport(int(windowWidth/2),0,int(windowWidth/2),int(windowHeight / 2))
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  gluOrtho2D(-rsize,rsize,-rsize,rsize)
  DesenhaBrasil(2, x3, y3)

  glutSwapBuffers()

def Inicializa():
  glClearColor(255,255,255,1)

def Timer(value):
  global x1,y1, x2,y2, x3,y3, xstep, ystep, rsize, windowWidth, windowHeight

  if abs(x1) > rsize-1:
    xstep *= -1

  if abs(y1) > rsize-1:
    ystep *= -1

  x1 += xstep
  y1 += 1.5*ystep
  glutPostRedisplay()
  glutTimerFunc(33, Timer, 1)

def Teclado(key, x, y):
  global x1,y1, x2,y2, x3,y3, xstep, ystep, rsize, windowWidth, windowHeight

  match key:
    case b"w":
      y3 += abs(ystep)
    case b"a":
      x3 -= abs(xstep)
    case b"s":
      y3 -= abs(ystep)
    case b"d":
      x3 += abs(xstep)

    
  glutPostRedisplay()

def Mouse(button, state, x, y):
  global x1,y1, x2,y2, x3,y3, xstep, ystep, rsize, windowWidth, windowHeight
  if button == GLUT_LEFT_BUTTON:
    if state == GLUT_DOWN:
      x3 = 4*rsize/windowWidth * x - 3*rsize
      y3 = -4*rsize/windowHeight*y + 3*rsize
  print(x,y)
  print(x3)

  print(y3)
  glutPostRedisplay()

def Responsivo(width, height):
  global x1,y1, x2,y2, x3,y3, xstep, ystep, rsize, windowWidth, windowHeight
  windowWidth = width
  windowHeight = height

def main():
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
  glutInitWindowPosition(0,0)
  glutInitWindowSize(windowWidth,windowHeight)
  glutCreateWindow(b"Brasil")
  glutDisplayFunc(Desenha)
  glutReshapeFunc(Responsivo)
  glutKeyboardFunc(Teclado)
  glutMouseFunc(Mouse)
  glutTimerFunc(33, Timer, 1)
  Inicializa()
  glutMainLoop()

main()
