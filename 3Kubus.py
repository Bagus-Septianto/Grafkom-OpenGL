#import
import pygame
import sys
from OpenGL.GL import *
from OpenGL.GLU import *

display = (800,600)

def inisialisasi():
     glClearColor(1.0, 1.0, 1.0, 1.0)	#Warna latar belakang putih
     glViewport(0,0,display[0],display[1])
     gluPerspective(45, display[0]/display[1],0.1,50.0)
     #loadTexture()
     
def loadTexture(file, format=1):
    # edit disini kalo ada perubahan file location
    textureSurface = pygame.image.load(file)
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()

    glEnable(GL_TEXTURE_2D)
    texid = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, texid)
    #change GL_RGB TO GL_RED/GL_GREEN
    if format == "coklat":
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_LUMINANCE_ALPHA, GL_UNSIGNED_BYTE, textureData)
    elif format == "hijau":
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_GREEN, GL_UNSIGNED_BYTE, textureData)
    else: #GL_LUMINANCE_ALPHA(abu-abu tua), GL_LUMINANCE(abu-abu muda), sisanya item/ warna
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)
    
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    return texid

def gambar_Kubus(lines=False):
    if lines:
        glBegin(GL_LINES)
        for edge in edges:
            glColor3fv((1, 1, 1))
            for vertex in edge:
                glVertex3fv(vertices[vertex])
        glEnd()
    else:
		# DEPAN
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 1.0); glVertex3f(-0.5, -5.5,  0.5);
        glTexCoord2f(1.0, 1.0); glVertex3f( 0.5, -5.5,  0.5);
        glTexCoord2f(1.0, 0.0); glVertex3f( 0.5, -4.5,  0.5);
        glTexCoord2f(0.0, 0.0); glVertex3f(-0.5, -4.5,  0.5);
        glEnd();
        
        # BELAKANG
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 1.0); glVertex3f(-0.5, -5.5, -0.5);
        glTexCoord2f(1.0, 1.0); glVertex3f(-0.5, -4.5, -0.5);
        glTexCoord2f(1.0, 0.0); glVertex3f( 0.5, -4.5, -0.5);
        glTexCoord2f(0.0, 0.0); glVertex3f( 0.5, -5.5, -0.5);
        glEnd();
        
        # KIRI
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 1.0); glVertex3f(-0.5, -5.5,  0.5);
        glTexCoord2f(1.0, 1.0); glVertex3f(-0.5, -4.5,  0.5);
        glTexCoord2f(1.0, 0.0); glVertex3f(-0.5, -4.5, -0.5);
        glTexCoord2f(0.0, 0.0); glVertex3f(-0.5, -5.5, -0.5);
        glEnd();
        
        # KANAN
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 1.0); glVertex3f( 0.5, -5.5, -0.5);
        glTexCoord2f(1.0, 1.0); glVertex3f( 0.5, -4.5, -0.5);
        glTexCoord2f(1.0, 0.0); glVertex3f( 0.5, -4.5,  0.5);
        glTexCoord2f(0.0, 0.0); glVertex3f( 0.5, -5.5,  0.5);
        glEnd();
        
        # ATAS
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 1.0); glVertex3f(-0.5, -4.5,  0.5);
        glTexCoord2f(1.0, 1.0); glVertex3f( 0.5, -4.5,  0.5);
        glTexCoord2f(1.0, 0.0); glVertex3f( 0.5, -4.5, -0.5);
        glTexCoord2f(0.0, 0.0); glVertex3f(-0.5, -4.5, -0.5);
        glEnd();
        
        # BAWAH
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 1.0); glVertex3f(-0.5, -5.5,  0.5);
        glTexCoord2f(1.0, 1.0); glVertex3f(-0.5, -5.5, -0.5);
        glTexCoord2f(1.0, 0.0); glVertex3f( 0.5, -5.5, -0.5);
        glTexCoord2f(0.0, 0.0); glVertex3f( 0.5, -5.5,  0.5);
        glEnd();

def gambarKu():
    #kiri mungkin kalo kepala atas
    loadTexture("pic.bmp", "coklat")
    glPushMatrix()
    glTranslated(1,0,0)
    glRotatef(180, 0, 1, 1)
    gambar_Kubus(0)
    glPopMatrix()

    #kanan mungkin kalo kepala atas
    loadTexture("pic.bmp", "hijau")
    glPushMatrix()
    glTranslated(-1,0,0)
    glRotatef(180, 0, 1, 1)
    gambar_Kubus(0)
    glPopMatrix()

    #tengah
    loadTexture("pic.bmp")
    glPushMatrix()
    glTranslated(0,0,0)
    glRotatef(180, 0, 1, 1)
    gambar_Kubus(0)
    glPopMatrix()

def Ruangan():
    loadTexture("lantai.bmp") #lantai
    glPushMatrix()
    glTranslatef(0, 0, 0)
    # Lantai/BAWAH
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f(-5.5, -0.5,  5.5);
    glTexCoord2f(1.0, 1.0); glVertex3f(-5.5, -0.5, -5.5);
    glTexCoord2f(1.0, 0.0); glVertex3f( 5.5, -0.5, -5.5);
    glTexCoord2f(0.0, 0.0); glVertex3f( 5.5, -0.5,  5.5);
    glEnd();

    loadTexture("tembok.bmp") #tembok
    # loadTexture("black.bmp") #tembok Testing
    glTranslatef(0, 0, 0)
    # Tembok BELAKANG
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f(-5.5, -0.5, -5.5);
    glTexCoord2f(1.0, 1.0); glVertex3f(-5.5,  5.5, -5.5);
    glTexCoord2f(1.0, 0.0); glVertex3f( 5.5,  5.5, -5.5);
    glTexCoord2f(0.0, 0.0); glVertex3f( 5.5, -0.5, -5.5);
    glEnd();
    # Tembok KANAN
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 5.5, -0.5, -5.5);
    glTexCoord2f(1.0, 1.0); glVertex3f( 5.5,  5.5, -5.5);
    glTexCoord2f(1.0, 0.0); glVertex3f( 5.5,  5.5,  5.5);
    glTexCoord2f(0.0, 0.0); glVertex3f( 5.5, -0.5,  5.5);
    glEnd();
    # Tembok KIRI
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f(-5.5, -0.5,  5.5);
    glTexCoord2f(1.0, 1.0); glVertex3f(-5.5,  5.5,  5.5);
    glTexCoord2f(1.0, 0.0); glVertex3f(-5.5,  5.5, -5.5);
    glTexCoord2f(0.0, 0.0); glVertex3f(-5.5, -0.5, -5.5);
    glEnd();

    loadTexture("atap.bmp")
    glTranslatef(0, 0, 0)
    # Atap/ATAS
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f(-5.5,  5.5,  5.5);
    glTexCoord2f(1.0, 1.0); glVertex3f( 5.5,  5.5,  5.5);
    glTexCoord2f(1.0, 0.0); glVertex3f( 5.5,  5.5, -5.5);
    glTexCoord2f(0.0, 0.0); glVertex3f(-5.5,  5.5, -5.5);
    glEnd();
    glPopMatrix()
    glFlush()
	        
def lemariKanan():
    loadTexture("lemari1.bmp")
    glPushMatrix()
    glTranslatef(0, 0, 0)
    # belakang
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 5.5, -0.5, -3.5);
    glTexCoord2f(1.0, 1.0); glVertex3f( 5.5,  2.5, -3.5);
    glTexCoord2f(1.0, 0.0); glVertex3f( 5.5,  2.5,  0.5);
    glTexCoord2f(0.0, 0.0); glVertex3f( 5.5, -0.5,  0.5);
    glEnd();

    loadTexture("muka.png")
    glTranslatef(0, 0, 0)
    glBegin(GL_QUADS)
    # muka
    glTexCoord2f(0.0, 1.0); glVertex3f(   4, -0.5, -3.5);
    glTexCoord2f(1.0, 1.0); glVertex3f(   4,  2.5, -3.5);
    glTexCoord2f(1.0, 0.0); glVertex3f(   4,  2.5,  0.5);
    glTexCoord2f(0.0, 0.0); glVertex3f(   4, -0.5,  0.5);
    glEnd();
    
    loadTexture("lemari1.bmp")
    glTranslatef(0, 0, 0)
    glBegin(GL_QUADS)
    # kiri
    glTexCoord2f(0.0, 1.0); glVertex3f(   4, -0.5, -3.5);
    glTexCoord2f(1.0, 1.0); glVertex3f(   4,  2.5, -3.5);
    glTexCoord2f(1.0, 0.0); glVertex3f( 5.5,  2.5, -3.5);
    glTexCoord2f(0.0, 0.0); glVertex3f( 5.5, -0.5, -3.5);
    glEnd();

    loadTexture("lemari1.bmp")
    glTranslatef(0, 0, 0)
    glBegin(GL_QUADS)
    # kanan
    glTexCoord2f(0.0, 1.0); glVertex3f(   4, -0.5, 0.5);
    glTexCoord2f(1.0, 1.0); glVertex3f(   4,  2.5, 0.5);
    glTexCoord2f(1.0, 0.0); glVertex3f( 5.5,  2.5, 0.5);
    glTexCoord2f(0.0, 0.0); glVertex3f( 5.5, -0.5, 0.5);
    glEnd();

    loadTexture("lemari1.bmp")
    glTranslatef(0, 0, 0)
    # Atap/ATAS
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f(   4,  2.5,  0.5);
    glTexCoord2f(1.0, 1.0); glVertex3f( 5.5,  2.5,  0.5);
    glTexCoord2f(1.0, 0.0); glVertex3f( 5.5,  2.5, -3.5);
    glTexCoord2f(0.0, 0.0); glVertex3f(   4,  2.5, -3.5);
    glEnd();
    glPopMatrix()
    glFlush()

def lemariKanan1():
    loadTexture("lemari1.bmp")
    glPushMatrix()
    glTranslatef(0, 0, 0)
    # belakang
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 5.5, -0.5,  1);
    glTexCoord2f(1.0, 1.0); glVertex3f( 5.5,  2.5,  1);
    glTexCoord2f(1.0, 0.0); glVertex3f( 5.5,  2.5,  3.5);
    glTexCoord2f(0.0, 0.0); glVertex3f( 5.5, -0.5,  3.5);
    glEnd();

    loadTexture("muka.png")
    glTranslatef(0, 0, 0)
    glBegin(GL_QUADS)
    # muka
    glTexCoord2f(0.0, 1.0); glVertex3f(   4, -0.5,  1);
    glTexCoord2f(1.0, 1.0); glVertex3f(   4,  2.5,  1);
    glTexCoord2f(1.0, 0.0); glVertex3f(   4,  2.5,  3.5);
    glTexCoord2f(0.0, 0.0); glVertex3f(   4, -0.5,  3.5);
    glEnd();
    
    loadTexture("lemari1.bmp")
    glTranslatef(0, 0, 0)
    glBegin(GL_QUADS)
    # kiri
    glTexCoord2f(0.0, 1.0); glVertex3f(   4, -0.5,  1);
    glTexCoord2f(1.0, 1.0); glVertex3f(   4,  2.5,  1);
    glTexCoord2f(1.0, 0.0); glVertex3f( 5.5,  2.5,  1);
    glTexCoord2f(0.0, 0.0); glVertex3f( 5.5, -0.5,  1);
    glEnd();

    loadTexture("lemari1.bmp")
    glTranslatef(0, 0, 0)
    glBegin(GL_QUADS)
    # kanan
    glTexCoord2f(0.0, 1.0); glVertex3f(   4, -0.5, 3.5);
    glTexCoord2f(1.0, 1.0); glVertex3f(   4,  2.5, 3.5);
    glTexCoord2f(1.0, 0.0); glVertex3f( 5.5,  2.5, 3.5);
    glTexCoord2f(0.0, 0.0); glVertex3f( 5.5, -0.5, 3.5);
    glEnd();

    loadTexture("lemari1.bmp")
    glTranslatef(0, 0, 0)
    # Atap/ATAS
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f(   4,  2.5,  3.5);
    glTexCoord2f(1.0, 1.0); glVertex3f( 5.5,  2.5,  3.5);
    glTexCoord2f(1.0, 0.0); glVertex3f( 5.5,  2.5,  1);
    glTexCoord2f(0.0, 0.0); glVertex3f(   4,  2.5,  1);
    glEnd();
    glPopMatrix()
    glFlush()

def lemariKiri():
    loadTexture("lemari1.bmp")
    glPushMatrix()
    glTranslatef(0, 0, 0)
    # belakang
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( -5.5, -0.5, -3.5);
    glTexCoord2f(1.0, 1.0); glVertex3f( -5.5,  2.5, -3.5);
    glTexCoord2f(1.0, 0.0); glVertex3f( -5.5,  2.5,  0.5);
    glTexCoord2f(0.0, 0.0); glVertex3f( -5.5, -0.5,  0.5);
    glEnd();

    loadTexture("muka.png")
    glTranslatef(0, 0, 0)
    glBegin(GL_QUADS)
    # muka
    glTexCoord2f(0.0, 1.0); glVertex3f(   -4, -0.5, -3.5);
    glTexCoord2f(1.0, 1.0); glVertex3f(   -4,  2.5, -3.5);
    glTexCoord2f(1.0, 0.0); glVertex3f(   -4,  2.5,  0.5);
    glTexCoord2f(0.0, 0.0); glVertex3f(   -4, -0.5,  0.5);
    glEnd();
    
    loadTexture("lemari1.bmp")
    glTranslatef(0, 0, 0)
    glBegin(GL_QUADS)
    # kiri
    glTexCoord2f(0.0, 1.0); glVertex3f(   -4, -0.5, -3.5);
    glTexCoord2f(1.0, 1.0); glVertex3f(   -4,  2.5, -3.5);
    glTexCoord2f(1.0, 0.0); glVertex3f( -5.5,  2.5, -3.5);
    glTexCoord2f(0.0, 0.0); glVertex3f( -5.5, -0.5, -3.5);
    glEnd();

    loadTexture("lemari1.bmp")
    glTranslatef(0, 0, 0)
    glBegin(GL_QUADS)
    # kanan
    glTexCoord2f(0.0, 1.0); glVertex3f(   -4, -0.5, 0.5);
    glTexCoord2f(1.0, 1.0); glVertex3f(   -4,  2.5, 0.5);
    glTexCoord2f(1.0, 0.0); glVertex3f( -5.5,  2.5, 0.5);
    glTexCoord2f(0.0, 0.0); glVertex3f( -5.5, -0.5, 0.5);
    glEnd();

    loadTexture("lemari1.bmp")
    glTranslatef(0, 0, 0)
    # Atap/ATAS
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f(   -4,  2.5,  0.5);
    glTexCoord2f(1.0, 1.0); glVertex3f( -5.5,  2.5,  0.5);
    glTexCoord2f(1.0, 0.0); glVertex3f( -5.5,  2.5, -3.5);
    glTexCoord2f(0.0, 0.0); glVertex3f(   -4,  2.5, -3.5);
    glEnd();
    glPopMatrix()
    glFlush()

def lemariKiri1():
    loadTexture("lemari1.bmp")
    glPushMatrix()
    glTranslatef(0, 0, 0)
    # belakang
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( -5.5, -0.5,  1);
    glTexCoord2f(1.0, 1.0); glVertex3f( -5.5,  2.5,  1);
    glTexCoord2f(1.0, 0.0); glVertex3f( -5.5,  2.5,  3.5);
    glTexCoord2f(0.0, 0.0); glVertex3f( -5.5, -0.5,  3.5);
    glEnd();

    loadTexture("muka.png")
    glTranslatef(0, 0, 0)
    glBegin(GL_QUADS)
    # muka
    glTexCoord2f(0.0, 1.0); glVertex3f(   -4, -0.5,  1);
    glTexCoord2f(1.0, 1.0); glVertex3f(   -4,  2.5,  1);
    glTexCoord2f(1.0, 0.0); glVertex3f(   -4,  2.5,  3.5);
    glTexCoord2f(0.0, 0.0); glVertex3f(   -4, -0.5,  3.5);
    glEnd();
    
    loadTexture("lemari1.bmp")
    glTranslatef(0, 0, 0)
    glBegin(GL_QUADS)
    # kiri
    glTexCoord2f(0.0, 1.0); glVertex3f(   -4, -0.5,  1);
    glTexCoord2f(1.0, 1.0); glVertex3f(   -4,  2.5,  1);
    glTexCoord2f(1.0, 0.0); glVertex3f( -5.5,  2.5,  1);
    glTexCoord2f(0.0, 0.0); glVertex3f( -5.5, -0.5,  1);
    glEnd();

    loadTexture("lemari1.bmp")
    glTranslatef(0, 0, 0)
    glBegin(GL_QUADS)
    # kanan
    glTexCoord2f(0.0, 1.0); glVertex3f(   -4, -0.5, 3.5);
    glTexCoord2f(1.0, 1.0); glVertex3f(   -4,  2.5, 3.5);
    glTexCoord2f(1.0, 0.0); glVertex3f( -5.5,  2.5, 3.5);
    glTexCoord2f(0.0, 0.0); glVertex3f( -5.5, -0.5, 3.5);
    glEnd();

    loadTexture("lemari1.bmp")
    glTranslatef(0, 0, 0)
    # Atap/ATAS
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f(   -4,  2.5,  3.5);
    glTexCoord2f(1.0, 1.0); glVertex3f( -5.5,  2.5,  3.5);
    glTexCoord2f(1.0, 0.0); glVertex3f( -5.5,  2.5,  1);
    glTexCoord2f(0.0, 0.0); glVertex3f(   -4,  2.5,  1);
    glEnd();
    glPopMatrix()
    glFlush()

def pigura():
    glTranslatef(0, 3.2, 0)
    loadTexture("lemari1.bmp")
    glPushMatrix()
    # kanan
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 1,  2, -5.5);
    glTexCoord2f(1.0, 1.0); glVertex3f( 1,  2, -5.3);
    glTexCoord2f(1.0, 0.0); glVertex3f( 1,  0, -5.3);
    glTexCoord2f(0.0, 0.0); glVertex3f( 1,  0, -5.5);
    glEnd();

    loadTexture("lemari1.bmp")
    glBegin(GL_QUADS)
    # kiri
    glTexCoord2f(0.0, 1.0); glVertex3f( -1,  2, -5.5);
    glTexCoord2f(1.0, 1.0); glVertex3f( -1,  2, -5.3);
    glTexCoord2f(1.0, 0.0); glVertex3f( -1,  0, -5.3);
    glTexCoord2f(0.0, 0.0); glVertex3f( -1,  0, -5.5);
    glEnd();

    loadTexture("lemari1.bmp")
    glBegin(GL_QUADS)
    # atas
    glTexCoord2f(0.0, 1.0); glVertex3f(  1,  2, -5.5);
    glTexCoord2f(1.0, 1.0); glVertex3f(  1,  2, -5.3);
    glTexCoord2f(1.0, 1.0); glVertex3f( -1,  2, -5.3);
    glTexCoord2f(0.0, 1.0); glVertex3f( -1,  2, -5.5);
    glEnd();

    loadTexture("lemari1.bmp")
    glBegin(GL_QUADS)
    # bawah
    glTexCoord2f(0.0, 1.0); glVertex3f( 1,  0, -5.5);
    glTexCoord2f(1.0, 1.0); glVertex3f( 1,  0, -5.3);
    glTexCoord2f(1.0, 0.0); glVertex3f( -1,  0, -5.3);
    glTexCoord2f(0.0, 0.0); glVertex3f( -1,  0, -5.5);
    glEnd();

    loadTexture("lemari1.bmp")
    glBegin(GL_QUADS)
    # muka
    glTexCoord2f(0.0, 1.0); glVertex3f( -1,  2, -5.3);
    glTexCoord2f(1.0, 1.0); glVertex3f( 1,  2, -5.3);
    glTexCoord2f(1.0, 0.0); glVertex3f( 1,  0, -5.3);
    glTexCoord2f(0.0, 0.0); glVertex3f( -1,  0, -5.3);
    glEnd();
    
    loadTexture("pic.bmp")
    glBegin(GL_QUADS)
    # fotonya
    glTexCoord2f(0.0, 1.0); glVertex3f( -0.8,  1.8, -5.29);
    glTexCoord2f(1.0, 1.0); glVertex3f( 0.8,  1.8, -5.29);
    glTexCoord2f(1.0, 0.0); glVertex3f( 0.8,  0.2, -5.29);
    glTexCoord2f(0.0, 0.0); glVertex3f( -0.8,  0.2, -5.29);
    glEnd();
    glPopMatrix()
    glTranslatef(0, -3.2, 0)
    glFlush()

def TV():
    glTranslatef(0, 0, 0)
    glPushMatrix()
    loadTexture("black.bmp")
    # depan
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( -2, 3,  -5.4);
    glTexCoord2f(1.0, 1.0); glVertex3f( 2, 3,  -5.4);
    glTexCoord2f(1.0, 0.0); glVertex3f( 2,  1,  -5.4);
    glTexCoord2f(0.0, 0.0); glVertex3f( -2, 1,  -5.4);
    glEnd();
    # kiri
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( -2, 3,  -5.5);
    glTexCoord2f(1.0, 1.0); glVertex3f( -2, 3,  -5.4);
    glTexCoord2f(1.0, 0.0); glVertex3f( -2, 1,  -5.4);
    glTexCoord2f(0.0, 0.0); glVertex3f( -2, 1,  -5.5);
    glEnd();
    # kanan
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 2, 3,  -5.5);
    glTexCoord2f(1.0, 1.0); glVertex3f( 2, 3,  -5.4);
    glTexCoord2f(1.0, 0.0); glVertex3f( 2, 1,  -5.4);
    glTexCoord2f(0.0, 0.0); glVertex3f( 2, 1,  -5.5);
    glEnd();
    # atas
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 2, 3,  -5.5);
    glTexCoord2f(1.0, 1.0); glVertex3f( 2, 3,  -5.4);
    glTexCoord2f(1.0, 0.0); glVertex3f( -2, 3,  -5.4);
    glTexCoord2f(0.0, 0.0); glVertex3f( -2, 3,  -5.5);
    glEnd();
    # bawah
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 2, 1,  -5.5);
    glTexCoord2f(1.0, 1.0); glVertex3f( 2, 1,  -5.4);
    glTexCoord2f(1.0, 0.0); glVertex3f( -2, 1,  -5.4);
    glTexCoord2f(0.0, 0.0); glVertex3f( -2, 1,  -5.5);
    glEnd();
    loadTexture("layarTV.bmp")
    # layar
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( -1.8, 2.8,  -5.39);
    glTexCoord2f(1.0, 1.0); glVertex3f( 1.8, 2.8,  -5.39);
    glTexCoord2f(1.0, 0.0); glVertex3f( 1.8,  1.2,  -5.39);
    glTexCoord2f(0.0, 0.0); glVertex3f( -1.8, 1.2,  -5.39);
    glEnd();

    glPopMatrix()
    glFlush()

def sofa():
    glTranslatef(0, 0, 0)
    loadTexture("sofa.bmp")
    glPushMatrix()
    # belakang
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 3,  1.5, -3);
    glTexCoord2f(1.0, 1.0); glVertex3f( 3,  1.5, 0);
    glTexCoord2f(1.0, 0.0); glVertex3f( 3,  -0.5, 0);
    glTexCoord2f(0.0, 0.0); glVertex3f( 3,  -0.5, -3);
    glEnd();
    # depan
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 1.5,  0.6, -3);
    glTexCoord2f(1.0, 1.0); glVertex3f( 1.5,  0.6, 0);
    glTexCoord2f(1.0, 0.0); glVertex3f( 1.5,  -0.5, 0);
    glTexCoord2f(0.0, 0.0); glVertex3f( 1.5,  -0.5, -3);
    glEnd();
    # tempat duduk
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 2.3,  0.6, -3);
    glTexCoord2f(1.0, 1.0); glVertex3f( 2.3,  0.6, 0);
    glTexCoord2f(1.0, 0.0); glVertex3f( 1.5,  0.6, 0);
    glTexCoord2f(0.0, 0.0); glVertex3f( 1.5,  0.6, -3);
    glEnd();
    # tempat punggung
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 2.5,  1.5, -3);
    glTexCoord2f(1.0, 1.0); glVertex3f( 2.5,  1.5, 0);
    glTexCoord2f(1.0, 0.0); glVertex3f( 2.3,  0.6, 0);
    glTexCoord2f(0.0, 0.0); glVertex3f( 2.3,  0.6, -3);
    glEnd();
    # atap
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 3,  1.5, -3);
    glTexCoord2f(1.0, 1.0); glVertex3f( 3,  1.5, 0);
    glTexCoord2f(1.0, 0.0); glVertex3f( 2.5,  1.5, 0);
    glTexCoord2f(0.0, 0.0); glVertex3f( 2.5,  1.5, -3);
    glEnd();
    # kanan kursi bawah
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 1.5,  0.6, -3);
    glTexCoord2f(1.0, 1.0); glVertex3f( 3,  0.6, -3);
    glTexCoord2f(1.0, 0.0); glVertex3f( 3, -0.5, -3);
    glTexCoord2f(0.0, 0.0); glVertex3f( 1.5,  -0.5, -3);
    glEnd();
    # kanan kursi atas
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 2.5,  1.5, -3); # punggung 2
    glTexCoord2f(1.0, 1.0); glVertex3f( 3,  1.5, -3); # belakang 2
    glTexCoord2f(1.0, 0.0); glVertex3f( 3, 0.6, -3); # kiri kursi bawah 2
    glTexCoord2f(0.0, 0.0); glVertex3f( 2.3,  0.6, -3); # tempat duduk 2
    glEnd();
    # kiri kursi bawah
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 1.5,  0.6, 0);
    glTexCoord2f(1.0, 1.0); glVertex3f( 3,  0.6, 0);
    glTexCoord2f(1.0, 0.0); glVertex3f( 3, -0.5, 0);
    glTexCoord2f(0.0, 0.0); glVertex3f( 1.5,  -0.5, 0);
    glEnd();
    # kiri kursi atas
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 2.5,  1.5, 0); # punggung 2
    glTexCoord2f(1.0, 1.0); glVertex3f( 3,  1.5, 0); # belakang 2
    glTexCoord2f(1.0, 0.0); glVertex3f( 3, 0.6, 0); # kiri kursi bawah 2
    glTexCoord2f(0.0, 0.0); glVertex3f( 2.3,  0.6, 0); # tempat duduk 2
    glEnd();
    glPopMatrix()
    glFlush()

def meja():
    glTranslatef(0, 0, 0)
    glPushMatrix()
    loadTexture("atap.bmp")
    # atas
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 1, 0.8,  -3);
    glTexCoord2f(1.0, 1.0); glVertex3f( 1, 0.8,  -1);
    glTexCoord2f(1.0, 0.0); glVertex3f( -1, 0.8,  -1);
    glTexCoord2f(0.0, 0.0); glVertex3f( -1, 0.8,  -3);
    glEnd();
    loadTexture("lemari1.bmp")
    # samping belakang
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 1, 0.5,  -3);
    glTexCoord2f(1.0, 1.0); glVertex3f( 1, 0.8,  -3);
    glTexCoord2f(1.0, 0.0); glVertex3f( -1, 0.8,  -3);
    glTexCoord2f(0.0, 0.0); glVertex3f( -1, 0.5,  -3);
    glEnd();
    # samping kiri
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( -1, 0.5,  -3);
    glTexCoord2f(1.0, 1.0); glVertex3f( -1, 0.8,  -3);
    glTexCoord2f(1.0, 0.0); glVertex3f( -1, 0.8,  -1);
    glTexCoord2f(0.0, 0.0); glVertex3f( -1, 0.5,  -1);
    glEnd();
    # samping depan
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( -1, 0.5,  -1);
    glTexCoord2f(1.0, 1.0); glVertex3f( -1, 0.8,  -1);
    glTexCoord2f(1.0, 0.0); glVertex3f( 1, 0.8,  -1);
    glTexCoord2f(0.0, 0.0); glVertex3f( 1, 0.5,  -1);
    glEnd();
    # samping kanan
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 1, 0.5,  -1);
    glTexCoord2f(1.0, 1.0); glVertex3f( 1, 0.8,  -1);
    glTexCoord2f(1.0, 0.0); glVertex3f( 1, 0.8,  -3);
    glTexCoord2f(0.0, 0.0); glVertex3f( 1, 0.5,  -3);
    glEnd();
    # kaki luar
    # kaki depan kiri
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( -1, 0.8,  -1);
    glTexCoord2f(1.0, 1.0); glVertex3f( -0.8, 0.8,  -1);
    glTexCoord2f(1.0, 0.0); glVertex3f( -0.8, -0.5,  -1);
    glTexCoord2f(0.0, 0.0); glVertex3f( -1, -0.5,  -1);
    glEnd();
    # kaki depan kanan
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 0.8, 0.8,  -1);
    glTexCoord2f(1.0, 1.0); glVertex3f( 1, 0.8,  -1);
    glTexCoord2f(1.0, 0.0); glVertex3f( 1, -0.5,  -1);
    glTexCoord2f(0.0, 0.0); glVertex3f( 0.8, -0.5,  -1);
    glEnd();
    # kaki kiri kiri
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( -1, 0.8,  -3);
    glTexCoord2f(1.0, 1.0); glVertex3f( -1, 0.8,  -2.8);
    glTexCoord2f(1.0, 0.0); glVertex3f( -1, -0.5,  -2.8);
    glTexCoord2f(0.0, 0.0); glVertex3f( -1, -0.5,  -3);
    glEnd();
    # kaki kiri kanan
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( -1, 0.8,  -1.2);
    glTexCoord2f(1.0, 1.0); glVertex3f( -1, 0.8,  -1);
    glTexCoord2f(1.0, 0.0); glVertex3f( -1, -0.5,  -1);
    glTexCoord2f(0.0, 0.0); glVertex3f( -1, -0.5,  -1.2);
    glEnd();
    # kaki kanan kiri
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 1, 0.8,  -1);
    glTexCoord2f(1.0, 1.0); glVertex3f( 1, 0.8,  -1.2);
    glTexCoord2f(1.0, 0.0); glVertex3f( 1, -0.5,  -1.2);
    glTexCoord2f(0.0, 0.0); glVertex3f( 1, -0.5,  -1);
    glEnd();
    # kaki kanan kanan
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 1, 0.8,  -2.8);
    glTexCoord2f(1.0, 1.0); glVertex3f( 1, 0.8,  -3);
    glTexCoord2f(1.0, 0.0); glVertex3f( 1, -0.5,  -3);
    glTexCoord2f(0.0, 0.0); glVertex3f( 1, -0.5,  -2.8);
    glEnd();
    # kaki belakang kiri
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 0.8, 0.8,  -3);
    glTexCoord2f(1.0, 1.0); glVertex3f( 1, 0.8,  -3);
    glTexCoord2f(1.0, 0.0); glVertex3f( 1, -0.5,  -3);
    glTexCoord2f(0.0, 0.0); glVertex3f( 0.8, -0.5,  -3);
    glEnd();
    # kaki belakang kanan
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( -0.8, 0.8,  -3);
    glTexCoord2f(1.0, 1.0); glVertex3f( -1, 0.8,  -3);
    glTexCoord2f(1.0, 0.0); glVertex3f( -1, -0.5,  -3);
    glTexCoord2f(0.0, 0.0); glVertex3f( -0.8, -0.5,  -3);
    glEnd();
    # kaki dalem
    # kaki depan kiri kanan
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( -0.8, 0.8,  -1);
    glTexCoord2f(1.0, 1.0); glVertex3f( -0.8, 0.8,  -1.2);
    glTexCoord2f(1.0, 0.0); glVertex3f( -0.8, -0.5,  -1.2);
    glTexCoord2f(0.0, 0.0); glVertex3f( -0.8, -0.5,  -1);
    glEnd();
    # kaki depan kiri belakang
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( -1, 0.8,  -1.2);
    glTexCoord2f(1.0, 1.0); glVertex3f( -0.8, 0.8,  -1.2);
    glTexCoord2f(1.0, 0.0); glVertex3f( -0.8, -0.5,  -1.2);
    glTexCoord2f(0.0, 0.0); glVertex3f( -1, -0.5,  -1.2);
    glEnd();
    # kaki depan kanan kiri
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 0.8, 0.8,  -1);
    glTexCoord2f(1.0, 1.0); glVertex3f( 0.8, 0.8,  -1.2);
    glTexCoord2f(1.0, 0.0); glVertex3f( 0.8, -0.5,  -1.2);
    glTexCoord2f(0.0, 0.0); glVertex3f( 0.8, -0.5,  -1);
    glEnd();
    # kaki depan kanan belakang
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 1, 0.8,  -1.2);
    glTexCoord2f(1.0, 1.0); glVertex3f( 0.8, 0.8,  -1.2);
    glTexCoord2f(1.0, 0.0); glVertex3f( 0.8, -0.5,  -1.2);
    glTexCoord2f(0.0, 0.0); glVertex3f( 1, -0.5,  -1.2);
    glEnd();

    # kaki belakang kiri depan
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( -1, 0.8,  -2.8);
    glTexCoord2f(1.0, 1.0); glVertex3f( -0.8, 0.8,  -2.8);
    glTexCoord2f(1.0, 0.0); glVertex3f( -0.8, -0.5,  -2.8);
    glTexCoord2f(0.0, 0.0); glVertex3f( -1, -0.5,  -2.8);
    glEnd();
    # kaki belakang kiri kanan
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( -0.8, 0.8,  -2.8);
    glTexCoord2f(1.0, 1.0); glVertex3f( -0.8, 0.8,  -3);
    glTexCoord2f(1.0, 0.0); glVertex3f( -0.8, -0.5,  -3);
    glTexCoord2f(0.0, 0.0); glVertex3f( -0.8, -0.5,  -2.8);
    glEnd();
    # kaki belakang kanan depan
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 1, 0.8,  -2.8);
    glTexCoord2f(1.0, 1.0); glVertex3f( 0.8, 0.8,  -2.8);
    glTexCoord2f(1.0, 0.0); glVertex3f( 0.8, -0.5,  -2.8);
    glTexCoord2f(0.0, 0.0); glVertex3f( 1, -0.5,  -2.8);
    glEnd();
    # kaki belakang kanan kiri
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 0.8, 0.8,  -2.8);
    glTexCoord2f(1.0, 1.0); glVertex3f( 0.8, 0.8,  -3);
    glTexCoord2f(1.0, 0.0); glVertex3f( 0.8, -0.5,  -3);
    glTexCoord2f(0.0, 0.0); glVertex3f( 0.8, -0.5,  -2.8);
    glEnd();
    glPopMatrix()
    glFlush()

def AC():
    glTranslatef(0, 0, 0)
    glPushMatrix()
    loadTexture("ac.bmp")
    # atas
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 5.5, 5, -1.5);
    glTexCoord2f(1.0, 1.0); glVertex3f( 5.5, 5, 1.5);
    glTexCoord2f(1.0, 0.0); glVertex3f( 4.5,  5,  1.5);
    glTexCoord2f(0.0, 0.0); glVertex3f( 4.5,  5,  -1.5);
    glEnd();
    # kiri
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 4.5,  5,   -1.5);
    glTexCoord2f(1.0, 1.0); glVertex3f( 5.5,  5,   -1.5);
    glTexCoord2f(1.0, 0.0); glVertex3f( 5.5,  4.3, -1.5);
    glTexCoord2f(0.0, 0.0); glVertex3f( 4.5,  4.3, -1.5);
    glEnd();
    # kiri bawah
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 4.5,  4.3, -1.5);
    glTexCoord2f(1.0, 1.0); glVertex3f( 5.5,  4.3, -1.5);
    glTexCoord2f(1.0, 0.0); glVertex3f( 5.5,  4, -1.5);
    glTexCoord2f(0.0, 0.0); glVertex3f( 4.8,  4, -1.5);
    glEnd();
    # kanan
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 4.5,  5,   1.5);
    glTexCoord2f(1.0, 1.0); glVertex3f( 5.5,  5,   1.5);
    glTexCoord2f(1.0, 0.0); glVertex3f( 5.5,  4.3, 1.5);
    glTexCoord2f(0.0, 0.0); glVertex3f( 4.5,  4.3, 1.5);
    glEnd();
    # kanan bawah
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 4.5,  4.3, 1.5);
    glTexCoord2f(1.0, 1.0); glVertex3f( 5.5,  4.3, 1.5);
    glTexCoord2f(1.0, 0.0); glVertex3f( 5.5,  4, 1.5);
    glTexCoord2f(0.0, 0.0); glVertex3f( 4.8,  4, 1.5);
    glEnd();
    # mulut
    loadTexture("mulutac.bmp")
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 4.5,  4.3, -1.5);
    glTexCoord2f(1.0, 1.0); glVertex3f( 4.5,  4.3, 1.5);
    glTexCoord2f(1.0, 0.0); glVertex3f( 4.8,  4, 1.5);
    glTexCoord2f(0.0, 0.0); glVertex3f( 4.8,  4, -1.5);
    glEnd();
    loadTexture("ac.bmp")
    # depan
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 4.5,  5,  -1.5);
    glTexCoord2f(1.0, 1.0); glVertex3f( 4.5,  5,   1.5);
    glTexCoord2f(1.0, 0.0); glVertex3f( 4.5,  4.3, 1.5);
    glTexCoord2f(0.0, 0.0); glVertex3f( 4.5,  4.3, -1.5);
    glEnd();
    # bawah
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 4.8,  4, -1.5);
    glTexCoord2f(1.0, 1.0); glVertex3f( 5.5,  4, -1.5);
    glTexCoord2f(1.0, 0.0); glVertex3f( 5.5,  4, 1.5);
    glTexCoord2f(0.0, 0.0); glVertex3f( 4.8,  4, 1.5);
    glEnd();
    # Lidah
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 4.8,  4.3, -1.5);
    glTexCoord2f(1.0, 1.0); glVertex3f( 4.8,  4.3, 1.5);
    glTexCoord2f(1.0, 0.0); glVertex3f( 4.5,  4, 1.5);
    glTexCoord2f(0.0, 0.0); glVertex3f( 4.5,  4, -1.5);
    glEnd();
    # kiri kanan | atas bawah | depan belakang (glVertex3f)
    # urutan glTexCoord2f
    # 1 2
    # 4 3

    glPopMatrix()
    glFlush()

def jam():
    glTranslatef(0, 0, 0)
    glPushMatrix()
    loadTexture("jam.bmp")
    # depan / gambar jamnya
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( -3.8, 5,  -5.3);
    glTexCoord2f(1.0, 1.0); glVertex3f( -2.5, 5,  -5.3);
    glTexCoord2f(1.0, 0.0); glVertex3f( -2.5, 4,  -5.3);
    glTexCoord2f(0.0, 0.0); glVertex3f( -3.8, 4,  -5.3);
    glEnd();
    loadTexture("white.bmp")
    # kiri
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( -3.8, 5,  -5.5);
    glTexCoord2f(1.0, 1.0); glVertex3f( -3.8, 5,  -5.3);
    glTexCoord2f(1.0, 0.0); glVertex3f( -3.8, 4,  -5.3);
    glTexCoord2f(0.0, 0.0); glVertex3f( -3.8, 4,  -5.5);
    glEnd();
    # kanan
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( -2.5, 5,  -5.5);
    glTexCoord2f(1.0, 1.0); glVertex3f( -2.5, 5,  -5.3);
    glTexCoord2f(1.0, 0.0); glVertex3f( -2.5, 4,  -5.3);
    glTexCoord2f(0.0, 0.0); glVertex3f( -2.5, 4,  -5.5);
    glEnd();
    # atas
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( -2.5, 5,  -5.5);
    glTexCoord2f(1.0, 1.0); glVertex3f( -2.5, 5,  -5.3);
    glTexCoord2f(1.0, 0.0); glVertex3f( -3.8, 5,  -5.3);
    glTexCoord2f(0.0, 0.0); glVertex3f( -3.8, 5,  -5.5);
    glEnd();
    # bawah
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( -2.5, 4,  -5.5);
    glTexCoord2f(1.0, 1.0); glVertex3f( -2.5, 4,  -5.3);
    glTexCoord2f(1.0, 0.0); glVertex3f( -3.8, 4,  -5.3);
    glTexCoord2f(0.0, 0.0); glVertex3f( -3.8, 4,  -5.5);
    glEnd();

    glPopMatrix()
    glFlush()

def kulkas():
    glTranslatef(0.5, 0, 0)
    glPushMatrix()
    loadTexture("kulkas.bmp")
    # pintu bawah
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 2, 2,  -2.5);
    glTexCoord2f(1.0, 1.0); glVertex3f( 4, 2,  -2.5);
    glTexCoord2f(1.0, 0.0); glVertex3f( 4, -0.5, -2.5);
    glTexCoord2f(0.0, 0.0); glVertex3f( 2, -0.5, -2.5);
    glEnd();
    # pintu atas
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 2, 3,  -2.5);
    glTexCoord2f(1.0, 1.0); glVertex3f( 4, 3,  -2.5);
    glTexCoord2f(1.0, 0.0); glVertex3f( 4, 2, -2.5);
    glTexCoord2f(0.0, 0.0); glVertex3f( 2, 2, -2.5);
    glEnd();
    loadTexture("white.bmp")
    # kiri
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 2, 3,  -5.5);
    glTexCoord2f(1.0, 1.0); glVertex3f( 2, 3,  -2.5);
    glTexCoord2f(1.0, 0.0); glVertex3f( 2, -0.5, -2.5);
    glTexCoord2f(0.0, 0.0); glVertex3f( 2, -0.5, -5.5);
    glEnd();
    # kanan
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 4, 3,  -5.5);
    glTexCoord2f(1.0, 1.0); glVertex3f( 4, 3,  -2.5);
    glTexCoord2f(1.0, 0.0); glVertex3f( 4, -0.5, -2.5);
    glTexCoord2f(0.0, 0.0); glVertex3f( 4, -0.5, -5.5);
    glEnd();
    # atas
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 2, 3,  -5.5);
    glTexCoord2f(1.0, 1.0); glVertex3f( 4, 3,  -5.5);
    glTexCoord2f(1.0, 0.0); glVertex3f( 4, 3, -2.5);
    glTexCoord2f(0.0, 0.0); glVertex3f( 2, 3, -2.5);
    glEnd();
    # bawah
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 2, -0.5,  -5.5);
    glTexCoord2f(1.0, 1.0); glVertex3f( 4, -0.5,  -5.5);
    glTexCoord2f(1.0, 0.0); glVertex3f( 4, -0.5, -2.5);
    glTexCoord2f(0.0, 0.0); glVertex3f( 2, -0.5, -2.5);
    glEnd();
    # belakang
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f( 2, 3,  -5.5);
    glTexCoord2f(1.0, 1.0); glVertex3f( 4, 3,  -5.5);
    glTexCoord2f(1.0, 0.0); glVertex3f( 4, -0.5, -5.5);
    glTexCoord2f(0.0, 0.0); glVertex3f( 2, -0.5, -5.5);
    glEnd();
    
    glPopMatrix()
    glTranslatef(-0.5, 0, 0)
    glFlush()

def main():
    # jangan diubah, punyanya pygame
    pygame.init()
    pygame.display.set_mode(display, pygame.OPENGL|pygame.DOUBLEBUF)
    pygame.display.set_caption('Kubus dan Tekstur')

    inisialisasi()
    glTranslatef(0.0,0.0,-14)
    # glTranslatef(0.0,0.0,-25)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        #glRotatef(1, 0, 0, 1)
        glEnable( GL_TEXTURE_2D )
        glEnable( GL_DEPTH_TEST )

        glPushMatrix()
        glRotatef(15, 1, 0, 0) # rotate atas bawah
        glRotatef(10, 0, 1, 0) # rotate kiri kanan
        Ruangan()
        kulkas()
        jam()
        AC()
        glTranslatef(0,0,1.5)
        lemariKanan()
        lemariKanan1()
        glTranslatef(0,0,-1.5)
        gambarKu()
        lemariKiri()
        lemariKiri1()
        TV()
        pigura()
        meja()
        sofa()
        
        glRotatef(180,0,1,0)
        glTranslatef(0,0,3)
        sofa()

        glRotatef(90,0,1,0)
        glTranslatef(2,0,0)
        sofa()

        glRotatef(90,0,1,0) # untuk ngembaliin rotasinya
        glTranslatef(0,0,1) # translate sudah cancelling

        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(100)
    
#if python says run, let's run!
if __name__ == '__main__':
    main()
