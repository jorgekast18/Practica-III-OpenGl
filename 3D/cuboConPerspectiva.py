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
#3.1 Programa que genera un cubo con L = 0.7 aplicando una proyeccion perspectiva y el movimiento de la camara
# con gLookAt

def init():
  glClearColor(0.5, 0.5, 0.5, 0.0)
  glColor3f(0.2, 0.5, 0.5)
  glViewport(0, 0, 500, 500)
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  #glFrustum(-0.2, 0.2, -0.2, 0.2, 0.2, 0.9) # Proyeccion perspectiva alternativa 1
  glFrustum(-0.6, 0.7, -0.7, 0.1, 0.1, 0.8) # Proyeccion perspectiva alternativa 2
  #glFrustum(-6, 7, -7, 1, 1, 50) # Proyeccion perspectiva alternativa 3
  imprimirMatrizProyecccion()


def imprimirMatrizProyecccion():
  m = glGetFloatv(GL_PROJECTION_MATRIX)
  print "La matriz de proyeccion es:\n\n%s" % str(m) + "\n"


def imprimirMatrizModelado():
  mm = glGetFloatv(GL_MODELVIEW_MATRIX)
  print "La matriz de modelado es:\n\n%s" % str(mm) + "\n"


def dibujarCubo():
  glClear (GL_COLOR_BUFFER_BIT) #Borramos buffer de color
  glMatrixMode (GL_MODELVIEW) # Matriz de modelado
  glLoadIdentity()
  #gluLookAt(0.1, 0.1, 0.5, 0.2, 0.1, 0.1, 0, 0.1, 0) # Posicion de la camara, altera a la matriz MODELVIEW
  #gluLookAt(0.1, 0.1, 0.5, 0.2, 0.1, 0.1, 0, 0.1, 0.3)
  gluLookAt(-0.6, 0.7, 0.7, 0.5, 0.5, 0.5, 0.9, 0.9, 0.3)
  #glRotatef(70, 1,3,6)#Hacemos una transformacion para apreciar mejor la figura
  imprimirMatrizModelado()

  #Lado frontal del cubo
  glBegin(GL_POLYGON);
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
  glBegin(GL_POLYGON)
  glColor3f(  0.5,  0.0,  0.5 )
  glVertex3f( 0.35, -0.35, -0.35 )
  glVertex3f( 0.35,  0.35, -0.35 )
  glVertex3f( 0.35,  0.35,  0.35 )
  glVertex3f( 0.35, -0.35,  0.35 )
  glEnd()

  # LADO IZQUIERDO: lado verde
  glBegin(GL_POLYGON)
  glColor3f(   0.0,  0.5,  0.0 )
  glVertex3f( -0.35, -0.35,  0.35 )
  glVertex3f( -0.35,  0.35,  0.35 )
  glVertex3f( -0.35,  0.35, -0.35 )
  glVertex3f( -0.35, -0.35, -0.35 )
  glEnd()

  # LADO SUPERIOR: lado azul
  glBegin(GL_POLYGON)
  glColor3f(   0.0,  0.0,  0.5 )
  glVertex3f(  0.35,  0.35,  0.35 )
  glVertex3f(  0.35,  0.35, -0.35 )
  glVertex3f( -0.35,  0.35, -0.35 )
  glVertex3f( -0.35,  0.35,  0.35 )
  glEnd()
  # LADO INFERIOR: lado rojo
  glBegin(GL_POLYGON)
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
  glutCreateWindow ("Taller3 - Cubo con proyeccion perspectiva")
  init ()
  glutDisplayFunc(dibujarCubo)
  glutMainLoop()

if __name__ == '__main__':
    main()