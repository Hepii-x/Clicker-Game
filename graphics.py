import pygame as pyg
from settings import Settings
from upgrades import Upgrades
import settings, upgrades
import upgradesettings as settupg

class Graphics:
    def __init__(self, game):
        self.settings = Settings()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.rect = (0,0, 1280, 550)
        self.font = pyg.font.SysFont('Arial', 72)
        self.upgrades = Upgrades()

    def draw_text(self):
        text_score = str(int(round(settupg.score, 1)))
        text_upgrade_click_cost = str(int(round(settupg.upgrade_cost_click, 1)))
        text_passive_cost = str(int(round(settupg.upgrade_passive_cost, 1)))
        self.score = self.font.render(text_score, True, (255,255,255))
        self.clickme = self.font.render('Click me', True, (255,255,255))
        self.upgrade_cost = self.font.render(text_upgrade_click_cost, True, (255,255,255))
        self.passive_cost = self.font.render(text_passive_cost, True, (255,255,255))

        # self.multiplier = self.font.render(str(self.settings.multiplier), True, (255,255,255))
        self.screen.blit(self.score, (575, 197))
        self.screen.blit(self.clickme, (559,599))
        self.screen.blit(self.upgrade_cost, (360,594))
        self.screen.blit(self.passive_cost, (120,594))

        # self.screen.blit(self.multiplier, (400, 197))

    def draw(self):
        self.terminal = pyg.draw.rect(self.screen, color=(0,0,0), rect=self.rect)

    def draw_button1(self):
        self.b1 = pyg.draw.rect(self.screen, color=(4,0,128), rect=(539,599, 275,90))

    def draw_button2(self):
        self.b2 = pyg.draw.rect(self.screen, color=self.settings.upgrade_button_color, rect=(300,599, 162,74))

    def draw_button3(self):
        self.b3 = pyg.draw.rect(self.screen, color=self.settings.upgrade_passive_button_color, rect=(100,599, 162,74))

    def test_func(self):
        print(settupg.score)



    def run(self):
        self.draw()
        self.draw_button1()
        self.draw_button2()
        self.draw_button3()
        self.draw_text()
        self._check_upgrade()
        self.increase_time()



    def _check_upgrade(self):
        if settupg.score < settupg.upgrade_cost_click:
            self.settings.upgrade_button_color = (255,0,0)
        else:
            self.settings.upgrade_button_color = (0,255,0)
        if settupg.score < settupg.upgrade_passive_cost:
            self.settings.upgrade_passive_button_color = (255,0,0)
        else:
            self.settings.upgrade_passive_button_color = (0,255,0)

    def increase_time(self): # Absolutnie nie mam pojęcia jak to działa ale działa XD
        current_time = pyg.time.get_ticks()
        if current_time > self.settings.time_shit:
            self.settings.time_shit = current_time + 1000
            settupg.score += settupg.passive_income
            settupg.score = round(settupg.score, 1)



