import pygame as pyg
from settings import Settings
from graphics import Graphics
from sys import exit
from upgrades import Upgrades
import upgradesettings as settupg


class Main:
    def __init__(self):
        pyg.init()
        self.settings = Settings()
        self.upgrades = Upgrades()

        self.screen = pyg.display.set_mode((self.settings.screen_height, self.settings.screen_width))
        pyg.display.set_caption('Clicker')

        self.graphics = Graphics(self)

    def run_game(self):
        while True:
            self._event_loop()
            # self.upgrades.run()
            self._update_screen()

    def _event_loop(self):
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                print(settupg.save)
                settupg.save_save(settupg.save)
                exit()
            elif event.type == pyg.MOUSEBUTTONDOWN:
                x, y = event.pos
                if self.graphics.rock_rect.collidepoint(x, y):
                    self.upgrades.increase_score()

                elif self.graphics.iron_ore_rect.collidepoint(x, y):
                    self.upgrades.buy_iron_ore()

                elif self.graphics.copper_ore_rect.collidepoint(x, y):
                    print('Copper ore')
                    if settupg.iron_pickaxe > 24:
                        self.upgrades.buy_copper_ore()
                
                elif self.graphics.silver_ore_rect.collidepoint(x, y):
                    print('Silver ore')
                    if settupg.copper_pickaxe > 24:
                        self.upgrades.buy_silver_ore()

                elif self.graphics.gold_ore_rect.collidepoint(x, y):
                    print('Gold ore')
                    if settupg.silver_pickaxe > 24:
                        self.upgrades.buy_gold_ore()

                elif self.graphics.diamond_ore_rect.collidepoint(x, y):
                    print('Diamond ore')
                    if settupg.gold_pickaxe > 24:
                        self.upgrades.buy_diamond_ore()

                elif self.graphics.emerald_ore_rect.collidepoint(x, y):
                    print('Emerald ore')
                    if settupg.diamond_pickaxe > 24:
                        self.upgrades.buy_emerald_ore()

                elif self.graphics.rubin_ore_rect.collidepoint(x, y):
                    print('Rubin ore')
                    if settupg.emerald_pickaxe > 24:
                        self.upgrades.buy_rubin_ore()

                elif self.graphics.jadeit_ore_rect.collidepoint(x, y):
                    print('Jadeit ore')
                    if settupg.rubin_pickaxe > 24:
                        self.upgrades.buy_jadeit_ore()

                elif self.graphics.amethyst_ore_rect.collidepoint(x, y):
                    print('Amethyst ore')
                    if settupg.jadeit_pickaxe > 24:
                        self.upgrades.buy_amethyst_ore()

                elif self.graphics.iron_pickaxe_rect.collidepoint(x, y):
                    print('Iron pickaxe')
                    if settupg.iron_ore > 24:
                        self.upgrades.buy_iron_pickaxe()

                elif self.graphics.copper_pickaxe_rect.collidepoint(x, y):
                    print('Copper pickaxe')
                    if settupg.copper_ore > 24:
                        self.upgrades.buy_copper_pickaxe()

                elif self.graphics.silver_pickaxe_rect.collidepoint(x, y):
                    print('Silver pickaxe')
                    if settupg.silver_ore > 24:
                        self.upgrades.buy_silver_pickaxe()

                elif self.graphics.gold_pickaxe_rect.collidepoint(x, y):
                    print('Gold pickaxe')
                    if settupg.gold_ore > 24:
                        self.upgrades.buy_gold_pickaxe()

                elif self.graphics.diamond_pickaxe_rect.collidepoint(x, y):
                    print('Diamond pickaxe')
                    if settupg.diamond_ore > 24:
                        self.upgrades.buy_diamond_pickaxe()

                elif self.graphics.emerald_pickaxe_rect.collidepoint(x, y):
                    print('Emerald pickaxe')
                    if settupg.emerald_ore > 24:
                        self.upgrades.buy_emerald_pickaxe()

                elif self.graphics.rubin_pickaxe_rect.collidepoint(x, y):
                    print('Rubin pickaxe')
                    if settupg.rubin_ore > 24:
                        self.upgrades.buy_rubin_pickaxe()

                elif self.graphics.jadeit_pickaxe_rect.collidepoint(x, y):
                    print('Jadeit pickaxe')
                    if settupg.jadeit_ore > 24:
                        self.upgrades.buy_jadeit_pickaxe()
                    
                elif self.graphics.amethyst_pickaxe_rect.collidepoint(x, y):
                    print('Amethyst pickaxe')
                    if settupg.amethyst_ore > 24:
                        self.upgrades.buy_amethyst_pickaxe()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.graphics.run()
        pyg.display.flip()


if __name__ == '__main__':
    game = Main()
    game.run_game()
