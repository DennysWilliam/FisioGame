# importando o pygame
import pygame
import random
# importanto as constantes
from pygame.locals import *

pygame.init()  # inicia o pygame

# ------------------------

""" jogo """
def fundoContinuo(posicaoFundo): #funcao de looping da tela
    if posicaoFundo[0] - 1 < - 1365: #enquanto a imagem nao chega o seu pixel final nao reposiciona
        posicaoFundo[0] = 1366 #designa o pixel qe sera reposicionado a imagem
    else:
        posicaoFundo[0] -= 1 #senao volta a imagem inicial

def obstaculu_pedra (pedra):
        
    if pedra [0] < 0:
        pedra[0] = 1366
    else:
        pedra[0] -= 1

def obstaculo_passaro (passaro):

    if passaro [0] + passaro[2] < 0:
        posNova = random.randint(0, 1)
        
        if posNova == 1:
            passaro[1] = 515 #altura do passaro
        else:
            passaro[1] = 578 #altura do passaro
        passaro[0] = 1366
    else:
        passaro[0] -= 1

def colide_obstaculo_esquerda(personagem, obstaculo):
    colidiu = False
    if personagem[1] < obstaculo[1] + obstaculo[3] and (personagem[1] + personagem[3]) > obstaculo[1]:
        if (personagem[0] + personagem[2]) == obstaculo[0]:

            
            colidiu = True
    return colidiu

def jogo():
    backgroud = pygame.display.set_mode((1366, 768))  # designa o tamanho do display
    fundo1 = fundo2 = pygame.image.load("fundo.jpg")
    fundo1 = fundo2 = pygame.image.load("fundo.jpg")
    
    
    fundo_obstaculo = pygame.image.load("rocha.png")
    fundo_obstaculo1 = pygame.image.load("bird.png")
    personagem = pygame.image.load("Kang.png")
    posicaoFundo1 = [0, 0]  # posicao da imagem de fundo
    posicaoFundo2 = [1366, 0]  # reposicao da imagem de fundo
    posicao_personagem = [683, 568, 50, 50]  # posição imagem x, y, largura, altura(produndidade)
    passaro = [650, 515, 50, 50]  # passaro
    pedra = [350, 615, 50, 50]  # rocha
    pular = 0

    gameOver = False
    clock = pygame.time.Clock() # FPS do jogo
    while not gameOver:  #enqanto nao acabar o jogo
        for event in pygame.event.get(): #funcao de fechar a tela
            if event.type == QUIT: #fechar
                gameOver = True

            if event.type == pygame.KEYDOWN: 
                if event.key == K_ESCAPE:
                    gameOver = True

        backgroud.blit(fundo1, posicaoFundo1) #funcao de printar o fundo
        backgroud.blit(fundo2, posicaoFundo2) #printa o segundo fundo
        fundoContinuo(posicaoFundo1)  #faz a posicao das imagens se encaixar
        fundoContinuo(posicaoFundo2) #posiciona a imagem
        backgroud.blit(personagem, posicao_personagem)
        backgroud.blit(fundo_obstaculo, [pedra[0], pedra[1]])
        backgroud.blit(fundo_obstaculo1, [passaro[0], passaro[1]])
        obstaculo_passaro(passaro)
        obstaculu_pedra (pedra) 

            


        if pular == 0:

            if event.type == pygame.MOUSEBUTTONDOWN :# faz leitura do mouse prescionado
                posicao_personagem[1] =  posicao_personagem[1] -100 # instrução para pular
                pygame.time.set_timer(pygame.USEREVENT+1, 800) # tempo que personagem fica no ar
                pular = pular + 1

        if pular == 1:

            if event.type == pygame.USEREVENT+1:# desbilita o evento temporizado
                pygame.time.set_timer(pygame.USEREVENT+1,  0)
                posicao_personagem[1] =  posicao_personagem[1] +100
                pular = pular - 1
                
        if colide_obstaculo_esquerda(posicao_personagem, pedra) or colide_obstaculo_esquerda(posicao_personagem, passaro):
            gameOver = True
            


        if not gameOver:
            pygame.display.flip() #configura o display
            clock.tick(500) #designa a velocidade da tela

        else:
            pygame.display.quit()




# -------------------------
""" main -> menu """
def main(): 
     
    tela = pygame.display.set_mode((1366, 750))
    pygame.display.set_caption("MENU")
    relogio = pygame.time.Clock() # capturar com Tempo de atualização da tela
    Fundo = pygame.image.load("Menu.png")
    pygame.mixer.music.load("tokmenu.mp3")
    pygame.mixer.music.play(50,10)

    sair = False
   
    while sair != True: #enquanto diferente de verdadeiro
        for event in pygame.event.get(): #enquanto receber evento, capturar

            if event.type == pygame.QUIT: # se evento receber pygame.quit
               sair = True # Sair vira verdade e executa pygame.quit
          
        if event.type == pygame.KEYDOWN:#VERIFICA SE ALGUMA TECLA FOI PRESCIONADA
            if event.key == pygame.K_KP_ENTER:
                jogo()
                tela = pygame.display.set_mode((1366, 750))
        
                
        relogio.tick(27) # atualiza while 27 frames por segundo
        tela.blit(Fundo,[0, 0])
        pygame.display.update() # fica atualizando display
    pygame.quit() # fecha tela
main() # Chama função main

