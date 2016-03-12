import sys
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

# ====================================================================
#						      FUNCIONES
#
#
# ====================================================================
# 								DATOS
# Nombre : Jorge A. Castanio, Sebastian Velasquez, Oscar Eduardo Ramirez
# Codigo : 1153641, -----, -----
# Plan: Ingenieria de Sistemas
# Profesor: ----------
# Taller Numero 1 de Computacion Grafica
#=====================================================================
#3.2 Programa que genera una piramide aplicando una proyeccion paralela y el movimiento de la camara
# con gLookAt

def init():
  glClearColor(0.5, 0.5, 0.5, 0.0)
  glColor3f(0.6, 0.1, 0.4)
  glViewport(0, 0, 500, 500)
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  glOrtho(-1, 1, -1, 1, 1, -2) # Proyeccion paralela alternativa 1
  #glOrtho(-0.4, 0.3, -0.6, 1, 0.3, -1) # Proyeccion paralela alternativa 2
  #glOrtho(-0.8, 1, -0.5, 1, -0.5, 0.9) # Proyeccion paralela alternativa 3
  imprimirMatrizProyecccion()

def imprimirMatrizProyecccion():
  m = glGetFloatv(GL_PROJECTION_MATRIX)
  print "La matriz de proyeccion es:\n\n%s" % str(m) + "\n"


def imprimirMatrizModelado():
  mm = glGetFloatv(GL_MODELVIEW_MATRIX)
  print "La matriz de modelado es:\n\n%s" % str(mm) + "\n"

def dibujarPiramide():
  glClear(GL_COLOR_BUFFER_BIT)
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity ()

  #Puntos de vista gloLookAt
  #gluLookAt(0.1, 0.1, 0.5, 0.2, 0.1, 0.1, 0, 0.1, 0)
  gluLookAt(0.0, 0.0, 0.5, 0.2, 0.1, 0.1, 0, 0.1, 0)
  #glRotatef(90, 1,0,1)
  imprimirMatrizModelado()
  glutWireCone (0.4,0.4, 3, 4)
  glFlush()


def main():
  glutInit(sys.argv)
  glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
  glEnable(GL_DEPTH_TEST)
  glutInitWindowSize (500, 500)
  glutInitWindowPosition (100, 100)
  glutCreateWindow ("Taller3 - Piramide con proyeccion paralela")
  init ()
  glutDisplayFunc(dibujarPiramide)
  glutMainLoop()

if __name__ == '__main__':
    main()