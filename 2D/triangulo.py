from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

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
#2.2 Programa que genera un triangulo con base = 0.7 y h = 0.2


def imprimirMatrizProyecccion():
	m = glGetFloatv(GL_PROJECTION_MATRIX)
	print "La matriz de proyeccion es:\n\n%s" % str(m) + "\n"


def imprimirMatrizModelado():
	mm = glGetFloatv(GL_MODELVIEW_MATRIX)
	print "La matriz de modelado es:\n\n%s" % str(mm) + "\n"


def inicio():
	glClearColor(0.53, 0.53, 0.53, 0.0)  # Color de fondo
	glMatrixMode(GL_PROJECTION) # Matriz de proyecccion
	glLoadIdentity()
	imprimirMatrizProyecccion()


def dibujaTriangulo():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    imprimirMatrizModelado()
    glBegin(GL_TRIANGLES)
    glVertex2f(0, 0.1)
    glVertex2f(-0.45, -0.2)
    glVertex2f(0.45, 0.2)
    glEnd()
    glFlush()


def teclaPresionada(*args):  #  Otras configuraciones
    tecla = args[0]
    if tecla == "n" or tecla == "N":
    	glViewport(100, 100, 500, 500)
    	dibujaTriangulo()
    if tecla == "r" or tecla == "R":
    	glViewport(250, 250, 500, 500)
    	dibujaTriangulo()
    elif tecla == "g" or tecla == "G":
        glViewport(0, 250, 250, 500)
        dibujaTriangulo()
    elif tecla == "b" or tecla == "B":
        glViewport(250, 0, 500, 250)
        dibujaTriangulo()


def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
	glutInitWindowSize(500, 500)
	glEnable(GL_LIGHT0)
	glutInitWindowPosition(200, 200)
	glutCreateWindow("Taller3 - Triangulo")
	inicio()
	glutDisplayFunc(dibujaTriangulo)
	glutKeyboardFunc(teclaPresionada)
	glutMainLoop()


if __name__ == '__main__':
	main()