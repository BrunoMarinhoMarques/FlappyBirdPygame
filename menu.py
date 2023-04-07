import pygame.sprite

from obj import Obj, Text
import pygame


class Menu:

    def __init__(self):

        self.all_sprites = pygame.sprite.Group()

        self.background = Obj("assets/sky.png", 0, 0, self.all_sprites)
        self.background2 = Obj("assets/sky.png", 360, 0, self.all_sprites)
        self.ground = Obj("assets/ground.png", 0, 480, self.all_sprites)
        self.ground2 = Obj("assets/ground.png", 360, 480, self.all_sprites)

        self.get_ready = Obj("assets/getready.png", 60, 100, self.all_sprites)
        self.table_score = Obj("assets/score.png", 25, 200, self.all_sprites)
        self.button_go = Obj("assets/go.png", 100, 420, self.all_sprites)

        self.change_scene = False

        self.text_score = Text(100, "0")


    def draw(self, window):
        self.all_sprites.draw(window)
        self.text_score.draw(window, 160, 250)

    def update(self, pts):
        self.all_sprites.update()
        self.move_background()
        self.move_ground()
        self.text_score.text_update(pts)


    def events(self, event):

        #se caso o evento o tipo do evento for o de clicar com o mouse
        if event.type == pygame.MOUSEBUTTONUP:

            #se a posicao do mouse estiver dentro da imagem button_go entao
            if self.button_go.rect.collidepoint(pygame.mouse.get_pos()):
                #varivael change_scene se torna verdadeira
                self.change_scene = True
                print("Mouse")

        #se o tipo do evento for apertar uma tecla
        if event.type == pygame.KEYDOWN:
            #e a tecla apertada for a barra de espaço
            if event.key == pygame.K_SPACE:
                #entao variavel change_scene se torna verdadeira
                self.change_scene = True
                print("Teclado")




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
