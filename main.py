import pygame as pyg
from settings import Settings
from terminal import Terminal
from sys import exit
from threading import Thread
from time import sleep

class DeathlyMind:
    def __init__(self):
        pyg.init()
        self.settings = Settings()


        self.screen = pyg.display.set_mode((self.settings.screen_height, self.settings.screen_width))
        pyg.display.set_caption('Deathly Mind')


        self.terminal = Terminal(self)

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
                if self.terminal.b1.collidepoint(x,y):
                    self.terminal.increase_score()
                elif self.terminal.b2.collidepoint(x,y):
                    self.terminal.increase_multiplier()
                elif self.terminal.b3.collidepoint(x,y):
                    self.terminal.increase_passive()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.terminal.terminal_run()
        pyg.display.flip()

if __name__ == '__main__':
    game = DeathlyMind()
    game.run_game()


