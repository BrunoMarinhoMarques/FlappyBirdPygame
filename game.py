from obj import Obj, Pipe, Coin, Bird, Text
import pygame
import random
import pygame


class Game:

    def __init__(self):

        pygame.font.init()

        #responsavel por pegar todos os grupos e desenhar numa unica linha
        self.all_sprites = pygame.sprite.Group()
        self.coin_group = pygame.sprite.Group()
        self.pipe_group = pygame.sprite.Group()

        #o self.all_sprites é para que ele sempre seja desenhado na tela e sempre seja atualizado
        self.background = Obj("assets/sky.png", 0, 0, self.all_sprites)
        self.background2 = Obj("assets/sky.png", 360, 0, self.all_sprites)
        self.ground = Obj("assets/ground.png", 0, 480, self.all_sprites)
        self.ground2 = Obj("assets/ground.png", 360, 480, self.all_sprites)

        self.bird = Bird("assets/bird0.png", 50, 320, self.all_sprites)
        self.change_scene = False

        self.score = Text(100, "0")

        self.ticks = 0
        self.timer = 0

        self.max_score = 0

        self.check_score()


    def draw(self, window):

        #desenha todos os objetos na tela
        #funcao .draw existe em .sprite, passando parametro para quando chamar colocar onde vai ser desenhado
        self.all_sprites.draw(window)
        self.score.draw(window, 150, 50)

    # esse update é uma funcao que tem dentro de sprite
    def update(self):

        # chamando a funcao que da movimento a tela
        self.move_background()

        # chamando a funcao que da movimento ao chao
        self.move_ground()

        # atualiza todos os objetos na tela


        #se a variavel bird.play for igual a verdadeiro entao ele faz tudo e se colidir com o cano e se tornar False ele nao faz mais
        if self.bird.play:


            #chamando a funcao que adiciona canos a tela
            self.spaw_pipe()

            #aqui verifica a colisao, e estou passando o parametro de quando colidir com o grupo da moeda ou do cano
            self.bird.colision_coin(self.coin_group)
            self.bird.colision_pipe(self.pipe_group)
            self.score.text_update(str(self.bird.pts))
            self.all_sprites.update()

        else:
            #antes de acabar o jogo salva o valor da pontuacao
            self.save_score()

            self.gameover()





    def move_background(self):

        self.background.rect[0] -= 1
        self.background2.rect[0] -= 1

        #se background for menor que -360 entao a posicao x dele se tornara 0
        if self.background.rect[0] <= -360:
            self.background.rect[0] = 0

        if self.background2.rect[0] <= 0:
            self.background2.rect[0] = 360

    def move_ground(self):

        self.ground.rect[0] -= 3
        self.ground2.rect[0] -= 3

        if self.ground.rect[0] <= -360:
            self.ground.rect[0] = 0

        if self.ground2.rect[0] <= 0:
            self.ground2.rect[0] = 360

    def spaw_pipe(self):
        self.ticks += 1

        #entre 2.2 segundos e 3.3 segundos crie um cano
        #aleatoriedade dos canos
        if self.ticks >= random.randrange(80, 125):
            self.ticks = 0

            #o random.randrange esta aleatorizando a posicao Y entre 300 e 450 em Y
            #o self.pipe_group esta informando que o cano criado pertence tambem ao grupo pipe
            pipe = Pipe("assets/pipe1.png", 360, random.randrange(300, 450), self.all_sprites, self.pipe_group)
            pipe2 = Pipe("assets/pipe2.png", 360, random.randrange(-200, -100), self.all_sprites, self.pipe_group)

            coin = Coin("assets/0.png", 380, pipe2.rect[1] + 405, self.all_sprites, self.coin_group)

    #timer de delay para voltar para a tela de inicio
    def gameover(self):
        self.timer += 1
        print(self.timer)
        if self.timer >= 30:
            self.change_scene = True


    #funcao para o placar no inicio do jogo
    def save_score(self):
        #se o bird.pts for maior que max_score entao
        if self.bird.pts > self.max_score:
            #max_score sera igual a bird.pts
            self.max_score = self.bird.pts

            #serve para abrir arquivos, ira abrir o arquivo save.txt e depois da virgula
            #letra A = colocar mais conteudo
            #letra W = apaga tudo que esta dentro e reescreve/armazena
            #letra R = ler a informacao
            file = open("save.txt", "w")
            #.write esta falando que vai escrever algo dentro do arquivo, que sera o self.max_score
            file.write(str(self.max_score))

            #fecha o arquivo
            file.close()

    def check_score(self):

        #ler o que esta dentro do arquivo save.txt
        file = open("save.txt", "r")

        #variavel max_score sera igual ao valor que esta dentro do arquivo, porem tem que ser convertido em numero inteiro novamente
        self.max_score = int(file.read())

        #depois fecha o arquivo
        file.close()



