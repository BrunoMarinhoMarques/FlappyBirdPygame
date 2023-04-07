import pygame
from game import Game
from menu import Menu

class Main:
    def __init__(self):

        pygame.init()

        self.window = pygame.display.set_mode([360, 640])
        self.title = pygame.display.set_caption("Flappy Bird")



 

        self.loop = True
        self.fps = pygame.time.Clock()

        self.game = Game()
        self.menu = Menu()


    def events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.loop = False

            if not self.menu.change_scene:
                self.menu.events(event)


            #vai dentro de menu na funcao events e passas o parametro event que verifica todos os eventos
            self.menu.events(event)


    def draw(self):

        #dentro do objeto Game() pegue a funcao draw e dessenhe na self.window que recebe a tela
       # self.game.draw(self.window)
        #self.game.update()

        #se a variavel change_scene dentro de menu for falsa entao desenhamos ela
        if not self.menu.change_scene:
            self.menu.draw(self.window)
            self.menu.update(str(self.game.max_score))
        #senao se a variavel change_scene for falsa entao desenhamos ela
        elif not self.game.change_scene:
            self.game.draw(self.window)
            self.game.update()
        else:
            self.loop = False




    def update(self):
        while self.loop:
            self.fps.tick(30)
            self.events()
            self.draw()
            pygame.display.update()


loop = True

#aqui é para o jogo continuar sendo executado e voltar do inicio caso vc perca
while loop:
    Main().update()





