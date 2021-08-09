import pygame as pyg
from settings import Settings
from graphics import Graphics
from sys import exit
from threading import Thread
from time import sleep

class Main:
    def __init__(self):
        pyg.init()
        self.settings = Settings()


        self.screen = pyg.display.set_mode((self.settings.screen_height, self.settings.screen_width))
        pyg.display.set_caption('Clicker')


        self.graphics = Graphics(self)

    def run_game(self):
        while True:
            self._event_loop()
            self._update_screen()




    def _event_loop(self):
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                exit()
            elif event.type == pyg.MOUSEBUTTONDOWN:
                x, y = event.pos
                if self.graphics.b1.collidepoint(x,y):
                    self.graphics.increase_score()
                elif self.graphics.b2.collidepoint(x,y):
                    self.graphics.increase_multiplier()
                elif self.graphics.b3.collidepoint(x,y):
                    self.graphics.increase_passive()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.graphics.run()
        pyg.display.flip()

if __name__ == '__main__':
    game = Main()
    game.run_game()


