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
        self.upgrades = Upgrades()

    def draw_text(self):
        text_score = str(int(round(settupg.score, 1)))
        text_upgrade_click_cost = str(int(round(settupg.upgrade_cost_click, 1)))
        text_passive_cost = str(int(round(settupg.upgrade_passive_cost, 1)))
        text_font = pyg.font.Font('ui/etc/m6x11.ttf',64)
        stroke_font = pyg.font.Font('ui/etc/m6x11.ttf',65)

        # Score
        self.score = text_font.render(text_score, True, (255,255,255))
        self.score_stroke = stroke_font.render(text_score, True, (0,0,0))

    def draw_ore_amount(self):
        font = pyg.font.Font('ui/etc/m6x11.ttf',25)
        stroke_font = pyg.font.Font('ui/etc/m6x11.ttf',26)
        self.iron_ore_amount = font.render(f'x{str(settupg.iron_ore)}', True, (255,255,255))
        self.iron_ore_amount_stroke = stroke_font.render(f'{str(settupg.iron_ore)}', True, (0,0,0))

        



    def load_etc(self):
        # ETC
        self.bg = pyg.image.load('ui/etc/bg.png')
        self.shadow = pyg.image.load('ui/etc/shadow.png')
        self.rock = pyg.image.load('ui/etc/rock.png')
        self.rock_rect = self.rock.get_rect()
        self.rock_rect = self.rock_rect.move(432,112)
        self.coin = pyg.image.load('ui/etc/gold coin.png')
        self.coin = pyg.transform.scale(self.coin, (50,50))
        self.button_available = pyg.image.load('ui/etc/button available.png')
        self.button_unavailable = pyg.image.load('ui/etc/button unavailable.png')

    def load_ores(self):
        # Ores
        self.iron_ore = pyg.image.load('ui/ores/iron ore.png')
        self.iron_ore = pyg.transform.scale(self.iron_ore, (67,67))
        self.copper_ore = pyg.image.load('ui/ores/copper ore.png')
        self.copper_ore = pyg.transform.scale(self.copper_ore, (67,67))
        self.silver_ore = pyg.image.load('ui/ores/silver ore.png')
        self.silver_ore = pyg.transform.scale(self.silver_ore, (67,67))
        self.gold_ore = pyg.image.load('ui/ores/gold ore.png')
        self.gold_ore = pyg.transform.scale(self.gold_ore, (67,67))
        self.diamond_ore = pyg.image.load('ui/ores/diamond ore.png')
        self.diamond_ore = pyg.transform.scale(self.diamond_ore, (67,67))
        self.emerald_ore = pyg.image.load('ui/ores/emerald ore.png')
        self.emerald_ore = pyg.transform.scale(self.emerald_ore, (67,67))
        self.rubin_ore = pyg.image.load('ui/ores/rubin ore.png')
        self.rubin_ore = pyg.transform.scale(self.rubin_ore, (67,67))
        self.jadeit_ore = pyg.image.load('ui/ores/jadeit ore.png')
        self.jadeit_ore = pyg.transform.scale(self.jadeit_ore, (67,67))
        self.amethyst_ore = pyg.image.load('ui/ores/amethyst ore.png')
        self.amethyst_ore = pyg.transform.scale(self.amethyst_ore, (67,67))

    def load_pickaxes(self):
        # Pickaxes
        self.iron_pickaxe = pyg.image.load('ui/pickaxe/iron pickaxe.png')
        self.iron_pickaxe = pyg.transform.scale(self.iron_pickaxe, (67,67))
        self.copper_pickaxe = pyg.image.load('ui/pickaxe/copper pickaxe.png')
        self.copper_pickaxe = pyg.transform.scale(self.copper_pickaxe, (67,67))
        self.silver_pickaxe = pyg.image.load('ui/pickaxe/silver pickaxe.png')
        self.silver_pickaxe = pyg.transform.scale(self.silver_pickaxe, (67,67))
        self.gold_pickaxe = pyg.image.load('ui/pickaxe/gold pickaxe.png')
        self.gold_pickaxe = pyg.transform.scale(self.gold_pickaxe, (67,67))
        self.diamond_pickaxe = pyg.image.load('ui/pickaxe/diamond pickaxe.png')
        self.diamond_pickaxe = pyg.transform.scale(self.diamond_pickaxe, (67,67))
        self.emerald_pickaxe = pyg.image.load('ui/pickaxe/emerald pickaxe.png')
        self.emerald_pickaxe = pyg.transform.scale(self.emerald_pickaxe, (67,67))
        self.rubin_pickaxe = pyg.image.load('ui/pickaxe/rubin pickaxe.png')
        self.rubin_pickaxe = pyg.transform.scale(self.rubin_pickaxe, (67,67))
        self.jadeit_pickaxe = pyg.image.load('ui/pickaxe/jadeit pickaxe.png')
        self.jadeit_pickaxe = pyg.transform.scale(self.jadeit_pickaxe, (67,67))
        self.amethyst_pickaxe = pyg.image.load('ui/pickaxe/amethyst pickaxe.png')
        self.amethyst_pickaxe = pyg.transform.scale(self.amethyst_pickaxe, (67,67))

    def blit_etc(self):
            # ETC
        self.screen.blit(self.bg, (0,0))
        self.screen.blit(self.shadow, (417,398))
        self.screen.blit(self.rock, (432,112))
        self.screen.blit(self.coin, (560,10))

    def blit_ores(self):
            # Ores
        self.screen.blit(self.iron_ore, (0,0))
        self.screen.blit(self.copper_ore, (0,80))
        self.screen.blit(self.silver_ore,(0,160))
        self.screen.blit(self.gold_ore,(0,240))
        self.screen.blit(self.diamond_ore,(0,320))
        self.screen.blit(self.emerald_ore,(0,400))
        self.screen.blit(self.rubin_ore,(0,480))    
        self.screen.blit(self.jadeit_ore,(0,560))
        self.screen.blit(self.amethyst_ore,(0,640))
    
    def blit_buttons_ores(self):
        self.b1_ore = self.screen.blit(self.button_available, (70,90))
        self.b2_ore = self.screen.blit(self.button_available, (70,170))
        self.b3_ore = self.screen.blit(self.button_available, (70,250))
        self.b4_ore = self.screen.blit(self.button_available, (70,330))
        self.b5_ore = self.screen.blit(self.button_available, (70,410))
        self.b6_ore = self.screen.blit(self.button_available, (70,490))
        self.b7_ore = self.screen.blit(self.button_available, (70,10))
        self.b8_ore = self.screen.blit(self.button_available, (70,570))
        self.b9_ore = self.screen.blit(self.button_available, (70,650))

    def blit_buttons_pickaxes(self):
        self.b1_pickaxe = self.screen.blit(self.button_available, (1100,10))
        self.b2_pickaxe = self.screen.blit(self.button_available, (1100,90))
        self.b3_pickaxe = self.screen.blit(self.button_available, (1100,170))
        self.b4_pickaxe = self.screen.blit(self.button_available, (1100,250))
        self.b5_pickaxe = self.screen.blit(self.button_available, (1100,330))
        self.b6_pickaxe = self.screen.blit(self.button_available, (1100,410))
        self.b7_pickaxe = self.screen.blit(self.button_available, (1100,490))
        self.b8_pickaxe = self.screen.blit(self.button_available, (1100,570))
        self.b9_pickaxe = self.screen.blit(self.button_available, (1100,650))





        
    def blit_pickaxes(self):    
            # Pickaxes
        self.screen.blit(self.iron_pickaxe, (1210,0))
        self.screen.blit(self.copper_pickaxe, (1210,80))
        self.screen.blit(self.silver_pickaxe,(1210,160))
        self.screen.blit(self.gold_pickaxe,(1210,240))
        self.screen.blit(self.diamond_pickaxe,(1210,320))
        self.screen.blit(self.emerald_pickaxe,(1210,400))
        self.screen.blit(self.rubin_pickaxe,(1210,480))    
        self.screen.blit(self.jadeit_pickaxe,(1210,560))
        self.screen.blit(self.amethyst_pickaxe,(1210,640))
    
    def blit_text(self):
        # Score
        self.screen.blit(self.score_stroke,(621,12))
        self.screen.blit(self.score, (620, 12))
        self.screen.blit(self.iron_ore_amount_stroke, (46,53))
        self.screen.blit(self.iron_ore_amount, (46,53))
    
    def run(self):
        self.load_etc()
        self.load_ores()
        self.load_pickaxes()
        self.blit_etc()
        self.blit_ores()
        self.blit_pickaxes()
        self.blit_buttons_ores()
        self.blit_buttons_pickaxes()
        self.draw_text()
        self.draw_ore_amount()
        self.blit_text()
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



