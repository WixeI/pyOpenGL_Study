import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (1,-1,-1),
    (1,1,-1),
    (-1,1,-1),
    (-1,-1,-1),
    (1,-1,1),
    (1,1,1),
    (-1,-1,1),
    (-1,1,1)
)

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
)

def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])

    glEnd()

def main():
    #Criação da janela
    pygame.init()
    #Tamanho da Janela
    display = (800,600)
    #indica o tamanho da janela e o que será rodado nela. Para rodar gráficos 3d, precisamos avisar antes e utilizar double buffer
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    #Indica onde fica a viewport
    #Os últimos 2 parâmetros indicam onde fica o plano de começo e de limite da render distance
        #Ou seja, tudo que estiver atrás do plano limite não será desenhado
        #Tudo que estiver mais perto que o plano de começo não será desenhado
    #Par(ângulo de abertura da câmera, aspect ratio, init_render_distance_plane, end_render_distance_plane  )
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)

    glRotate(0, 0, 0, 0)

    #Loop da passagem de frames
    while True:
        #Evento de fechar janela no botão "X"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        #Limpar o canvas e os buffers
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        #--------------- De fato seu código ---------------

        Cube()
        #Par(Velocidade, Eixo X, Eixo Y, Eixo Z)
        glRotate(0.7, 2, 3, 0)

        #--------------------------------------------------

        #Flip() ao invés de Update() porque estamos usando Double Buffer, e flip alterna entre eles.
        pygame.display.flip()
        #Para não ser em tempo de execução, colocamos um intervalo forçado
        pygame.time.wait(10)

#Início da Execução
main()