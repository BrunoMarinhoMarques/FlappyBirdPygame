import pygame


# herdando a biblioteca do pygame.sprite.Sprite
class Obj(pygame.sprite.Sprite):

    def __init__(self, img, x, y, *groups):
        super().__init__(*groups)

        # recebe a imagem
        self.image = pygame.image.load(img)

        # recebe posicao
        self.rect = self.image.get_rect()
        self.rect[0] = x
        self.rect[1] = y




# criacao do cano com heranca do objeto Obj
class Pipe(Obj):

    def __init__(self, img, x, y, *groups):
        super().__init__(img, x, y, *groups)

    def update(self, *args):
        # chamando o movimento dos canos e atualizando
        self.move()

    def move(self):
        # movimento do cano
        self.rect[0] -= 3

        # se posicao x do cano for menor ou igual a -100 entao ele elimina o cano
        if self.rect[0] <= -100:
            self.kill()


class Coin(Obj):

    def __init__(self, img, x, y, *groups):
        super().__init__(img, x, y, *groups)

        self.ticks = 0

    # especifico do objeto
    def update(self, *args):
        self.move()
        self.anim()

    # especifico ao objeto Coin
    def move(self):
        self.rect[0] -= 3

        if self.rect[0] <= -100:
            self.kill()

    def anim(self):
        # esta falando para que a variavel self.ticks adicione o valor 1 seis vezes por conta do %6
        self.ticks = (self.ticks + 1) % 6
        self.image = pygame.image.load("assets/" + str(self.ticks) + ".png")


class Bird(Obj):
    def __init__(self, img, x, y, *groups):
        super().__init__(img, x, y, *groups)

        self.ticks = 0
        self.vel = 4
        self.grav = 1
        self.pts = 0

        self.play = True

    def update(self, *args):

        self.anim()
        self.move()

    def anim(self):

        # define que ticks ira somar +1 e ira fazer isso 4 vezes por conta do %
        self.ticks = (self.ticks + 1) % 4
        self.image = pygame.image.load("assets/bird" + str(self.ticks) + ".png")

    def move(self):

        # verifica toda vez que pressionar uma tecla do meu teclado
        key = pygame.key.get_pressed()

        self.vel += self.grav
        self.rect[1] += self.vel

        # limite de velocidade que ele desce e sobe
        if self.vel >= 13:
            self.vel = 13

        # se self.play for verdadeiro ele continua conseguindo apertar espaco
        if self.play:
            # se a tecla for espaco ele faz isso
            if key[pygame.K_SPACE]:
                self.vel -= 3.7

        # determina o limite do chao do jogo
        if self.rect[1] >= 440:
            self.rect[1] = 440

            print("PERDEU")

        # determina o limite do teto do jogo
        elif self.rect[1] <= 0:
            self.rect[1] = 0

            # a velocidade volta para 4 senao ele buga e fica preso no teto
            self.vel = 4

    def colision_pipe(self, group):

        # o que vai colidir que no caso sera o self que se refere ao proprio obj que no caso é passaro
        col = pygame.sprite.spritecollide(self, group, False)

        if col:
            self.play = False

    def colision_coin(self, group):

        col = pygame.sprite.spritecollide(self, group, True)

        if col:
            self.pts += 1


class Text:

    def __init__(self, size, text):
        #importando font dentro da pasta, quando for chamar passa os parametros de tamanho e o texto que vai colocar
        self.font = pygame.font.Font("assets/font/font.ttf", size)
        self.render = self.font.render(text, True, (255, 255, 255))

    def draw(self, window, x, y):
        #onde vai ser desenhado, o que vai ser desenhado, posicao x e y
        window.blit(self.render, (x, y))

    def text_update(self, text):
        #atualiza o proprio texto
        self.render = self.font.render(text, True, (255, 255, 255))
