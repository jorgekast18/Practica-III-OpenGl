import sys
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

# ====================================================================
#                 FUNCIONES
#
#
# ====================================================================
#                 DATOS
# Nombre : Jorge A. Castanio, Sebastian Velasquez, Oscar Eduardo Ramirez
# Codigo : 1153641, -----, -----
# Plan: Ingenieria de Sistemas
# Profesor: ----------
# Taller Numero 1 de Computacion Grafica
#=====================================================================
#3.1 Programa que genera un cubo con L = 0.7 aplicando una proyeccion paralela y el movimiento de la camara
# con gLookAt

def init():
  glClearColor(0.5, 0.5, 0.5, 0.0) #Fondo de la ventana
  glColor3f(0.2, 0.5, 0.5)
  glViewport(0, 0, 500, 500) # Matriz de mapeo
  glMatrixMode(GL_PROJECTION) # Matriz de proyecccion
  glLoadIdentity()
  glOrtho(-1, 1, -1, 1, 1, -2) # Proyeccion paralela alternativa 1
  # glOrtho(-1, 1, -0.5, 1, 1, -1) # Proyeccion paralela alternativa 2
  # glOrtho(-0.5, 0.4, -0.5, 1, -0.5, 0.9) # Proyeccion alternativa 3

  imprimirMatrizProyecccion()


def imprimirMatrizProyecccion():
  m = glGetFloatv(GL_PROJECTION_MATRIX)
  print "La matriz de proyeccion es:\n\n%s" % str(m) + "\n"


def imprimirMatrizModelado():
  mm = glGetFloatv(GL_MODELVIEW_MATRIX)
  print "La matriz de modelado es:\n\n%s" % str(mm) + "\n"


def dibujarCubo():
  glClear (GL_COLOR_BUFFER_BIT)
  glMatrixMode (GL_MODELVIEW)
  glLoadIdentity()
  # gluLookAt(0.1, 0.1, 0.5, 0.2, 0.1, 0.1, 0, 0.1, 0) # Posicion de la camara, altera a la matriz MODELVIEW
  # gluLookAt(-0.3, 0.2, -0.1, 0.2, 0.4, 0.4, 0.1, 0.1, 0)
  gluLookAt(-0.6, 0.7, 0.7, 0.5, 0.5, 0.5, 0.9, 0.9, 0.3)
  glRotatef(70, 1,3,6)
  imprimirMatrizModelado()

  #Lado frontal del cubo
  glBegin(GL_POLYGON);
  glColor3f(1.0,  0.2, 0.5)
  glVertex3f(  0.35, -0.35, -0.35 )
  glVertex3f(  0.35,  0.35, -0.35 )
  glVertex3f( -0.35,  0.35, -0.35 )
  glVertex3f( -0.35, -0.35, -0.35 )
  glEnd()

  #LADO TRASERO: lado blanco
  glBegin(GL_POLYGON)
  glColor3f(1.0,  1.0, 1.0)
  glVertex3f(0.35, -0.35, 0.35)
  glVertex3f(0.35,  0.35, 0.35)
  glVertex3f(-0.35,  0.35, 0.35)
  glVertex3f(-0.35, -0.35, 0.35)
  glEnd()
  

  # LADO DERECHO: lado morado
  glBegin(GL_TRIANGLES)
  glColor3f(  0.5,  0.0,  0.5 )
  glVertex3f( 0.35, -0.35, -0.35 )
  glVertex3f( 0.35,  0.35, -0.35 )
  glVertex3f( 0.35,  0.35,  0.35 )
  glVertex3f( 0.35, -0.35,  0.35 )
  glEnd()

 

  # LADO INFERIOR: lado rojo
  glBegin(GL_TRIANGLES)
  glColor3f(   0.5,  0.0,  0.0 )
  glVertex3f(  0.35, -0.35, -0.35 )
  glVertex3f(  0.35, -0.35,  0.35 )
  glVertex3f( -0.35, -0.35,  0.35 )
  glVertex3f( -0.35, -0.35, -0.35 )
  glEnd()

  glFlush()

def main():
  glutInit(sys.argv)
  glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
  glEnable(GL_DEPTH_TEST)
  glutInitWindowSize (500, 500)
  glutInitWindowPosition (100, 100)
  glutCreateWindow ("Taller3 - Irregular con proyeccion paralela")
  init ()
  glutDisplayFunc(dibujarCubo)
  glutMainLoop()

if __name__ == '__main__':
    main()