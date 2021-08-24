from typing import Text
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
        text_score = self.format_text(settupg.score)
        text_font = pyg.font.Font('ui/etc/m6x11.ttf',64)
        stroke_font = pyg.font.Font('ui/etc/m6x11.ttf',65)

        # Score
        self.score = text_font.render(text_score, True, (255,255,255))
        self.score_stroke = stroke_font.render(text_score, True, (0,0,0))

    def draw_ore_amount(self):
        font = pyg.font.Font('ui/etc/m6x11.ttf',25)
        stroke_font = pyg.font.Font('ui/etc/m6x11.ttf',27)

        self.iron_ore_amount = font.render(f'x{str(settupg.iron_ore)}', True, (255,255,255))
        self.iron_ore_amount_stroke = stroke_font.render(f'x{str(settupg.iron_ore)}', True, (0,0,0))

        self.copper_ore_amount = font.render(f'x{str(settupg.copper_ore)}', True, (255,255,255))
        self.copper_ore_amount_stroke = stroke_font.render(f'x{str(settupg.copper_ore)}', True, (0,0,0))
        
        self.silver_ore_amount = font.render(f'x{str(settupg.silver_ore)}', True, (255,255,255))
        self.silver_ore_amount_stroke = stroke_font.render(f'x{str(settupg.silver_ore)}', True, (0,0,0))
        
        self.gold_ore_amount = font.render(f'x{str(settupg.gold_ore)}', True, (255,255,255))
        self.gold_ore_amount_stroke = stroke_font.render(f'x{str(settupg.gold_ore)}', True, (0,0,0))
        
        self.diamond_ore_amount = font.render(f'x{str(settupg.diamond_ore)}', True, (255,255,255))
        self.diamond_ore_amount_stroke = stroke_font.render(f'x{str(settupg.diamond_ore)}', True, (0,0,0))
        
        self.emerald_ore_amount = font.render(f'x{str(settupg.emerald_ore)}', True, (255,255,255))
        self.emerald_ore_amount_stroke = stroke_font.render(f'x{str(settupg.emerald_ore)}', True, (0,0,0))
        
        self.rubin_ore_amount = font.render(f'x{str(settupg.rubin_ore)}', True, (255,255,255))
        self.rubin_ore_amount_stroke = stroke_font.render(f'x{str(settupg.rubin_ore)}', True, (0,0,0))
        
        self.jadeit_ore_amount = font.render(f'x{str(settupg.jadeit_ore)}', True, (255,255,255))
        self.jadeit_ore_amount_stroke = stroke_font.render(f'x{str(settupg.jadeit_ore)}', True, (0,0,0))
        
        self.amethyst_ore_amount = font.render(f'x{str(settupg.amethyst_ore)}', True, (255,255,255))
        self.amethyst_ore_amount_stroke = stroke_font.render(f'x{str(settupg.amethyst_ore)}', True, (0,0,0))

    def draw_pickaxe_amount(self):

        font = pyg.font.Font('ui/etc/m6x11.ttf',25)
        stroke_font = pyg.font.Font('ui/etc/m6x11.ttf',27)

        self.iron_pickaxe_amount = font.render(f'x{str(settupg.iron_pickaxe)}', True, (255,255,255))
        self.iron_pickaxe_amount_stroke = stroke_font.render(f'x{str(settupg.iron_pickaxe)}', True, (0,0,0))

        self.copper_pickaxe_amount = font.render(f'x{str(settupg.copper_pickaxe)}', True, (255,255,255))
        self.copper_pickaxe_amount_stroke = stroke_font.render(f'x{str(settupg.copper_pickaxe)}', True, (0,0,0))
        
        self.silver_pickaxe_amount = font.render(f'x{str(settupg.silver_pickaxe)}', True, (255,255,255))
        self.silver_pickaxe_amount_stroke = stroke_font.render(f'x{str(settupg.silver_pickaxe)}', True, (0,0,0))
        
        self.gold_pickaxe_amount = font.render(f'x{str(settupg.gold_pickaxe)}', True, (255,255,255))
        self.gold_pickaxe_amount_stroke = stroke_font.render(f'x{str(settupg.gold_pickaxe)}', True, (0,0,0))
        
        self.diamond_pickaxe_amount = font.render(f'x{str(settupg.diamond_pickaxe)}', True, (255,255,255))
        self.diamond_pickaxe_amount_stroke = stroke_font.render(f'x{str(settupg.diamond_pickaxe)}', True, (0,0,0))
        
        self.emerald_pickaxe_amount = font.render(f'x{str(settupg.emerald_pickaxe)}', True, (255,255,255))
        self.emerald_pickaxe_amount_stroke = stroke_font.render(f'x{str(settupg.emerald_pickaxe)}', True, (0,0,0))
        
        self.rubin_pickaxe_amount = font.render(f'x{str(settupg.rubin_pickaxe)}', True, (255,255,255))
        self.rubin_pickaxe_amount_stroke = stroke_font.render(f'x{str(settupg.rubin_pickaxe)}', True, (0,0,0))
        
        self.jadeit_pickaxe_amount = font.render(f'x{str(settupg.jadeit_pickaxe)}', True, (255,255,255))
        self.jadeit_pickaxe_amount_stroke = stroke_font.render(f'x{str(settupg.jadeit_pickaxe)}', True, (0,0,0))
        
        self.amethyst_pickaxe_amount = font.render(f'x{str(settupg.amethyst_pickaxe)}', True, (255,255,255))
        self.amethyst_pickaxe_amount_stroke = stroke_font.render(f'x{str(settupg.amethyst_pickaxe)}', True, (0,0,0))


    def draw_ore_cost(self):
        font = pyg.font.Font('ui/etc/m6x11.ttf',38)
        stroke_font = pyg.font.Font('ui/etc/m6x11.ttf',39)

        iron_ore_text = self.format_text(settupg.iron_ore_cost)
        copper_ore_text = self.format_text(settupg.copper_ore_cost)
        silver_ore_text = self.format_text(settupg.silver_ore_cost)
        gold_ore_text = self.format_text(settupg.gold_ore_cost)
        diamond_ore_text = self.format_text(settupg.diamond_ore_cost)
        emerald_ore_text = self.format_text(settupg.emerald_ore_cost)
        rubin_ore_text = self.format_text(settupg.rubin_ore_cost)
        jadeit_ore_text = self.format_text(settupg.jadeit_ore_cost)
        amethyst_ore_text = self.format_text(settupg.amethyst_ore_cost)


        self.iron_ore_cost = font.render(f'{iron_ore_text}', True, (255,255,255))
        self.iron_ore_cost_stroke = stroke_font.render(f'{iron_ore_text}', True, (0,0,0))

        self.copper_ore_cost = font.render(f'{copper_ore_text}', True, (255,255,255))
        self.copper_ore_cost_stroke = stroke_font.render(f'{copper_ore_text}', True, (0,0,0))

        self.silver_ore_cost = font.render(f'{silver_ore_text}', True, (255,255,255))
        self.silver_ore_cost_stroke = stroke_font.render(f'{silver_ore_text}', True, (0,0,0))

        self.gold_ore_cost = font.render(f'{gold_ore_text}', True, (255,255,255))
        self.gold_ore_cost_stroke = stroke_font.render(f'{gold_ore_text}', True, (0,0,0))

        self.diamond_ore_cost = font.render(f'{diamond_ore_text}', True, (255,255,255))
        self.diamond_ore_cost_stroke = stroke_font.render(f'{diamond_ore_text}', True, (0,0,0))

        self.emerald_ore_cost = font.render(f'{emerald_ore_text}', True, (255,255,255))
        self.emerald_ore_cost_stroke = stroke_font.render(f'{emerald_ore_text}', True, (0,0,0))

        self.rubin_ore_cost = font.render(f'{rubin_ore_text}', True, (255,255,255))
        self.rubin_ore_cost_stroke = stroke_font.render(f'{rubin_ore_text}', True, (0,0,0))

        self.jadeit_ore_cost = font.render(f'{jadeit_ore_text}', True, (255,255,255))
        self.jadeit_ore_cost_stroke = stroke_font.render(f'{jadeit_ore_text}', True, (0,0,0))

        self.amethyst_ore_cost = font.render(f'{amethyst_ore_text}', True, (255,255,255))
        self.amethyst_ore_cost_stroke = stroke_font.render(f'{amethyst_ore_text}', True, (0,0,0))

    def draw_pickaxe_cost(self):
        font = pyg.font.Font('ui/etc/m6x11.ttf',38)
        stroke_font = pyg.font.Font('ui/etc/m6x11.ttf',39)

        iron_pickaxe_text = self.format_text(settupg.iron_pickaxe_cost)
        copper_pickaxe_text = self.format_text(settupg.copper_pickaxe_cost)
        silver_pickaxe_text = self.format_text(settupg.silver_pickaxe_cost)
        gold_pickaxe_text = self.format_text(settupg.gold_pickaxe_cost)
        diamond_pickaxe_text = self.format_text(settupg.diamond_pickaxe_cost)
        emerald_pickaxe_text = self.format_text(settupg.emerald_pickaxe_cost)
        rubin_pickaxe_text = self.format_text(settupg.rubin_pickaxe_cost)
        jadeit_pickaxe_text = self.format_text(settupg.jadeit_pickaxe_cost)
        amethyst_pickaxe_text = self.format_text(settupg.amethyst_pickaxe_cost)


        self.iron_pickaxe_cost = font.render(f'{iron_pickaxe_text}', True, (255,255,255))
        self.iron_pickaxe_cost_stroke = stroke_font.render(f'{iron_pickaxe_text}', True, (0,0,0))

        self.copper_pickaxe_cost = font.render(f'{copper_pickaxe_text}', True, (255,255,255))
        self.copper_pickaxe_cost_stroke = stroke_font.render(f'{copper_pickaxe_text}', True, (0,0,0))

        self.silver_pickaxe_cost = font.render(f'{silver_pickaxe_text}', True, (255,255,255))
        self.silver_pickaxe_cost_stroke = stroke_font.render(f'{silver_pickaxe_text}', True, (0,0,0))

        self.gold_pickaxe_cost = font.render(f'{gold_pickaxe_text}', True, (255,255,255))
        self.gold_pickaxe_cost_stroke = stroke_font.render(f'{gold_pickaxe_text}', True, (0,0,0))

        self.diamond_pickaxe_cost = font.render(f'{diamond_pickaxe_text}', True, (255,255,255))
        self.diamond_pickaxe_cost_stroke = stroke_font.render(f'{diamond_pickaxe_text}', True, (0,0,0))

        self.emerald_pickaxe_cost = font.render(f'{emerald_pickaxe_text}', True, (255,255,255))
        self.emerald_pickaxe_cost_stroke = stroke_font.render(f'{emerald_pickaxe_text}', True, (0,0,0))

        self.rubin_pickaxe_cost = font.render(f'{rubin_pickaxe_text}', True, (255,255,255))
        self.rubin_pickaxe_cost_stroke = stroke_font.render(f'{rubin_pickaxe_text}', True, (0,0,0))

        self.jadeit_pickaxe_cost = font.render(f'{jadeit_pickaxe_text}', True, (255,255,255))
        self.jadeit_pickaxe_cost_stroke = stroke_font.render(f'{jadeit_pickaxe_text}', True, (0,0,0))

        self.amethyst_pickaxe_cost = font.render(f'{amethyst_pickaxe_text}', True, (255,255,255))
        self.amethyst_pickaxe_cost_stroke = stroke_font.render(f'{amethyst_pickaxe_text}', True, (0,0,0))





    

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


    def get_ore_rect(self):

        self.iron_ore_rect = self.button_available.get_rect()
        self.iron_ore_rect = self.iron_ore_rect.move(70,10)

        self.copper_ore_rect = self.button_available.get_rect()
        self.copper_ore_rect = self.copper_ore_rect.move(70,90)

        self.silver_ore_rect = self.button_available.get_rect() 
        self.silver_ore_rect = self.silver_ore_rect.move(70,170)

        self.gold_ore_rect = self.button_available.get_rect()
        self.gold_ore_rect = self.gold_ore_rect.move(70,250)

        self.diamond_ore_rect = self.button_available.get_rect() 
        self.diamond_ore_rect = self.diamond_ore_rect.move(70,330) 

        self.emerald_ore_rect = self.button_available.get_rect() 
        self.emerald_ore_rect = self.emerald_ore_rect.move(70,410) 

        self.rubin_ore_rect = self.button_available.get_rect() 
        self.rubin_ore_rect = self.rubin_ore_rect.move(70,490) 

        self.jadeit_ore_rect = self.button_available.get_rect() 
        self.jadeit_ore_rect = self.jadeit_ore_rect.move(70,570) 

        self.amethyst_ore_rect = self.button_available.get_rect() 
        self.amethyst_ore_rect = self.amethyst_ore_rect.move(70,650) 

    def get_pickaxe_rect(self):
        self.iron_pickaxe_rect = self.button_available.get_rect()
        self.iron_pickaxe_rect = self.iron_pickaxe_rect.move(1100,10)

        self.copper_pickaxe_rect = self.button_available.get_rect()
        self.copper_pickaxe_rect = self.copper_pickaxe_rect.move(1100,90)

        self.silver_pickaxe_rect = self.button_available.get_rect()
        self.silver_pickaxe_rect = self.silver_pickaxe_rect.move(1100,170)

        self.gold_pickaxe_rect = self.button_available.get_rect()
        self.gold_pickaxe_rect = self.gold_pickaxe_rect.move(1100,250)

        self.diamond_pickaxe_rect = self.button_available.get_rect()
        self.diamond_pickaxe_rect = self.diamond_pickaxe_rect.move(1100,330)

        self.emerald_pickaxe_rect = self.button_available.get_rect()
        self.emerald_pickaxe_rect = self.emerald_pickaxe_rect.move(1100,410)

        self.rubin_pickaxe_rect = self.button_available.get_rect()
        self.rubin_pickaxe_rect = self.rubin_pickaxe_rect.move(1100,490)

        self.jadeit_pickaxe_rect = self.button_available.get_rect()
        self.jadeit_pickaxe_rect = self.jadeit_pickaxe_rect.move(1100,570)

        self.amethyst_pickaxe_rect = self.button_available.get_rect()
        self.amethyst_pickaxe_rect = self.amethyst_pickaxe_rect.move(1100,650)













        
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
        if settupg.iron_pickaxe > 24:
            self.screen.blit(self.copper_ore, (0,80))
        if settupg.copper_pickaxe > 24:
            self.screen.blit(self.silver_ore,(0,160))
        if settupg.silver_pickaxe > 24:
            self.screen.blit(self.gold_ore,(0,240))
        if settupg.gold_pickaxe > 24:
            self.screen.blit(self.diamond_ore,(0,320))
        if settupg.diamond_pickaxe > 24:
            self.screen.blit(self.emerald_ore,(0,400))
        if settupg.emerald_pickaxe > 24:
            self.screen.blit(self.rubin_ore,(0,480))    
        if settupg.rubin_pickaxe > 24:
            self.screen.blit(self.jadeit_ore,(0,560))
        if settupg.jadeit_pickaxe > 24:
            self.screen.blit(self.amethyst_ore,(0,640))
    
    def blit_buttons_ores(self):
        if settupg.score < settupg.iron_ore_cost:
            self.b1_ore = self.screen.blit(self.button_unavailable, (70,10))
        else:
            self.b1_ore = self.screen.blit(self.button_available, (70,10))
        if settupg.iron_pickaxe > 24:
            if settupg.score < settupg.copper_ore_cost:
                self.b2_ore = self.screen.blit(self.button_unavailable, (70,90))
            else:
                self.b2_ore = self.screen.blit(self.button_available, (70,90))
        if settupg.copper_pickaxe > 24:
            if settupg.score < settupg.silver_ore_cost:
                self.b3_ore = self.screen.blit(self.button_unavailable, (70,170)) 
            else:
                self.b3_ore = self.screen.blit(self.button_available, (70,170)) 
        if settupg.silver_pickaxe > 24:
            if settupg.score < settupg.gold_ore_cost:
                self.b4_ore = self.screen.blit(self.button_unavailable, (70,250))
            else:
                self.b4_ore = self.screen.blit(self.button_available, (70,250))
        if settupg.gold_pickaxe > 24:
            if settupg.score < settupg.diamond_ore_cost:
                self.b5_ore = self.screen.blit(self.button_unavailable, (70,330))
            else:
                self.b5_ore = self.screen.blit(self.button_available, (70,330))
        if settupg.diamond_pickaxe > 24:
            if settupg.score < settupg.emerald_ore_cost:
                self.b6_ore = self.screen.blit(self.button_unavailable, (70,410))
            else:
                self.b6_ore = self.screen.blit(self.button_available, (70,410))
        if settupg.emerald_pickaxe > 24:
            if settupg.score < settupg.rubin_ore_cost:
                self.b7_ore = self.screen.blit(self.button_unavailable, (70,490))
            else:
                self.b7_ore = self.screen.blit(self.button_available, (70,490))
        if settupg.rubin_pickaxe > 24:
            if settupg.score < settupg.jadeit_ore_cost:
                self.b8_ore = self.screen.blit(self.button_unavailable, (70,570))
            else:
                self.b8_ore = self.screen.blit(self.button_available, (70,570))
        if settupg.jadeit_pickaxe > 24:
            if settupg.score < settupg.amethyst_ore_cost:
                self.b9_ore = self.screen.blit(self.button_unavailable, (70,650))
            else:
                self.b9_ore = self.screen.blit(self.button_available, (70,650))

    def blit_buttons_pickaxes(self):
        if settupg.iron_ore > 24:
            if settupg.score < settupg.iron_pickaxe_cost:
                self.b1_pickaxe = self.screen.blit(self.button_unavailable, (1100,10))
            else:
                self.b1_pickaxe = self.screen.blit(self.button_available, (1100,10))
        
        if settupg.copper_ore > 24:
            if settupg.score < settupg.copper_pickaxe_cost:
                self.b2_pickaxe = self.screen.blit(self.button_unavailable, (1100,90))
            else:
                self.b2_pickaxe = self.screen.blit(self.button_available, (1100,90))
        
        if settupg.silver_ore > 24:
            if settupg.score < settupg.silver_pickaxe_cost:
                self.b3_pickaxe = self.screen.blit(self.button_unavailable, (1100,170)) 
            else:
                self.b3_pickaxe = self.screen.blit(self.button_available, (1100,170)) 
        
        if settupg.gold_ore > 24:
            if settupg.score < settupg.gold_pickaxe_cost:
                self.b4_pickaxe = self.screen.blit(self.button_unavailable, (1100,250))
            else:
                self.b4_pickaxe = self.screen.blit(self.button_available, (1100,250))

        if settupg.diamond_ore > 24:
            if settupg.score < settupg.diamond_pickaxe_cost:
                self.b5_pickaxe = self.screen.blit(self.button_unavailable, (1100,330))
            else:
                self.b5_pickaxe = self.screen.blit(self.button_available, (1100,330))
        if settupg.emerald_ore > 24:
            if settupg.score < settupg.emerald_pickaxe_cost:
                self.b6_pickaxe = self.screen.blit(self.button_unavailable, (1100,410))
            else:
                self.b6_pickaxe = self.screen.blit(self.button_available, (1100,410))
        if settupg.rubin_ore > 24:
            if settupg.score < settupg.rubin_pickaxe_cost:
                self.b7_pickaxe = self.screen.blit(self.button_unavailable, (1100,490))
            else:
                self.b7_pickaxe = self.screen.blit(self.button_available, (1100,490))

        if settupg.jadeit_ore > 24:
            if settupg.score < settupg.jadeit_pickaxe_cost:
                self.b8_pickaxe = self.screen.blit(self.button_unavailable, (1100,570))
            else:
                self.b8_pickaxe = self.screen.blit(self.button_available, (1100,570))
        if settupg.amethyst_ore > 24:
            if settupg.score < settupg.amethyst_pickaxe_cost:
                self.b9_pickaxe = self.screen.blit(self.button_unavailable, (1100,650))
            else:
                self.b9_pickaxe = self.screen.blit(self.button_available, (1100,650))





        
    def blit_pickaxes(self):    
            # Pickaxes
        if settupg.iron_ore > 24:
            self.screen.blit(self.iron_pickaxe, (1210,0))
        if settupg.copper_ore > 24:
            self.screen.blit(self.copper_pickaxe, (1210,80))
        if settupg.silver_ore > 24:
            self.screen.blit(self.silver_pickaxe,(1210,160))
        if settupg.gold_ore > 24:
            self.screen.blit(self.gold_pickaxe,(1210,240))
        if settupg.diamond_ore > 24:
            self.screen.blit(self.diamond_pickaxe,(1210,320))
        if settupg.emerald_ore > 24:
            self.screen.blit(self.emerald_pickaxe,(1210,400))
        if settupg.rubin_ore > 24:
            self.screen.blit(self.rubin_pickaxe,(1210,480))    
        if settupg.jadeit_ore > 24:
            self.screen.blit(self.jadeit_pickaxe,(1210,560))
        if settupg.amethyst_ore > 24:
            self.screen.blit(self.amethyst_pickaxe,(1210,640))
    
    def blit_text(self):
        # Score
        
        self.screen.blit(self.score_stroke,(621,12))
        self.screen.blit(self.score, (620, 12))
        
        # Ores
        
        self.screen.blit(self.iron_ore_amount_stroke, (10,53))
        self.screen.blit(self.iron_ore_amount, (10,53))
        self.screen.blit(self.iron_ore_cost_stroke, (78,18))
        self.screen.blit(self.iron_ore_cost, (79,17))

        if settupg.iron_pickaxe > 24:
            self.screen.blit(self.copper_ore_amount_stroke, (10,133))
            self.screen.blit(self.copper_ore_amount, (10,133))
            self.screen.blit(self.copper_ore_cost_stroke, (78, 98))
            self.screen.blit(self.copper_ore_cost, (79,98))
        if settupg.copper_pickaxe > 24:
            self.screen.blit(self.silver_ore_amount_stroke, (10,213))
            self.screen.blit(self.silver_ore_amount, (10,213))
            self.screen.blit(self.silver_ore_cost_stroke, (78, 178))
            self.screen.blit(self.silver_ore_cost, (79,178))
        if settupg.silver_pickaxe > 24:
            self.screen.blit(self.gold_ore_amount_stroke, (10,293))
            self.screen.blit(self.gold_ore_amount, (10,293))
            self.screen.blit(self.gold_ore_cost_stroke, (78, 258))
            self.screen.blit(self.gold_ore_cost, (79,258))
        if settupg.gold_pickaxe > 24:
            self.screen.blit(self.diamond_ore_amount_stroke, (10,373))
            self.screen.blit(self.diamond_ore_amount, (10,373))
            self.screen.blit(self.diamond_ore_cost_stroke, (78, 338))
            self.screen.blit(self.diamond_ore_cost, (79,338))
        if settupg.diamond_pickaxe > 24:
            self.screen.blit(self.emerald_ore_amount_stroke, (10,453))
            self.screen.blit(self.emerald_ore_amount, (10,453))
            self.screen.blit(self.emerald_ore_cost_stroke, (78, 418))
            self.screen.blit(self.emerald_ore_cost, (79,418))
        if settupg.emerald_pickaxe > 24:
            self.screen.blit(self.rubin_ore_amount_stroke, (10,533))
            self.screen.blit(self.rubin_ore_amount, (10,533))
            self.screen.blit(self.rubin_ore_cost_stroke, (78, 498))
            self.screen.blit(self.rubin_ore_cost, (79,498))
        if settupg.rubin_pickaxe > 24:
            self.screen.blit(self.jadeit_ore_amount_stroke, (10,613))
            self.screen.blit(self.jadeit_ore_amount, (10,613))
            self.screen.blit(self.jadeit_ore_cost_stroke, (78, 578))
            self.screen.blit(self.jadeit_ore_cost, (79,578))
        if settupg.jadeit_pickaxe > 24:
            self.screen.blit(self.amethyst_ore_amount_stroke, (10,693))
            self.screen.blit(self.amethyst_ore_amount, (10,693))
            self.screen.blit(self.amethyst_ore_cost_stroke, (78, 658))
            self.screen.blit(self.amethyst_ore_cost, (79,658))
        
            # Pickaxes
        if settupg.iron_ore > 24:
            self.screen.blit(self.iron_pickaxe_amount_stroke, (1210,53))
            self.screen.blit(self.iron_pickaxe_amount, (1210,53))
            self.screen.blit(self.iron_pickaxe_cost_stroke, (1108,18))
            self.screen.blit(self.iron_pickaxe_cost, (1109,17))

        if settupg.copper_ore > 24:
            self.screen.blit(self.copper_pickaxe_amount_stroke, (1210,133))
            self.screen.blit(self.copper_pickaxe_amount, (1210,133))
            self.screen.blit(self.copper_pickaxe_cost_stroke, (1108, 98))
            self.screen.blit(self.copper_pickaxe_cost, (1109,98))
        if settupg.silver_ore > 24:
            self.screen.blit(self.silver_pickaxe_amount_stroke, (1210,213))
            self.screen.blit(self.silver_pickaxe_amount, (1210,213))
            self.screen.blit(self.silver_pickaxe_cost_stroke, (1108, 178))
            self.screen.blit(self.silver_pickaxe_cost, (1109, 178))
        if settupg.gold_ore > 24:
            self.screen.blit(self.gold_pickaxe_amount_stroke, (1210,293))
            self.screen.blit(self.gold_pickaxe_amount, (1210,293))
            self.screen.blit(self.gold_pickaxe_cost_stroke, (1108, 258))
            self.screen.blit(self.gold_pickaxe_cost, (1109,258))
        if settupg.diamond_ore > 24:
            self.screen.blit(self.diamond_pickaxe_amount_stroke, (1210,373))
            self.screen.blit(self.diamond_pickaxe_amount, (1210,373))
            self.screen.blit(self.diamond_pickaxe_cost_stroke, (1108, 338))
            self.screen.blit(self.diamond_pickaxe_cost, (1109,338))
        if settupg.emerald_ore > 24:
            self.screen.blit(self.emerald_pickaxe_amount_stroke, (1210,453))
            self.screen.blit(self.emerald_pickaxe_amount, (1210,453))
            self.screen.blit(self.emerald_pickaxe_cost_stroke, (1108, 418))
            self.screen.blit(self.emerald_pickaxe_cost, (1109,418))
        if settupg.rubin_ore > 24:
            self.screen.blit(self.rubin_pickaxe_amount_stroke, (1210,533))
            self.screen.blit(self.rubin_pickaxe_amount, (1210,533))
            self.screen.blit(self.rubin_pickaxe_cost_stroke, (1108, 498))
            self.screen.blit(self.rubin_pickaxe_cost, (1109,498))
        if settupg.jadeit_ore > 24:
            self.screen.blit(self.jadeit_pickaxe_amount_stroke, (1210,613))
            self.screen.blit(self.jadeit_pickaxe_amount, (1210,613))
            self.screen.blit(self.jadeit_pickaxe_cost_stroke, (1108, 578))
            self.screen.blit(self.jadeit_pickaxe_cost, (1109, 578))
        if settupg.amethyst_ore > 24:
            self.screen.blit(self.amethyst_pickaxe_amount_stroke, (1210,693))
            self.screen.blit(self.amethyst_pickaxe_amount, (1210,693))
            self.screen.blit(self.amethyst_pickaxe_cost_stroke, (1108, 658))
            self.screen.blit(self.amethyst_pickaxe_cost, (1109,658))

        # Ore COSTS






















        # Pickaxe COSTS
























    def run(self):
        self.load_etc()
        self.load_ores()
        self.load_pickaxes()
        self.blit_etc()
        self.blit_ores()
        self.blit_pickaxes()
        self.blit_buttons_ores()
        self.blit_buttons_pickaxes()
        self.get_ore_rect()
        self.get_pickaxe_rect()
        self.draw_text()
        self.draw_ore_amount()
        self.draw_ore_cost()
        self.draw_pickaxe_amount()
        self.draw_pickaxe_cost()
        self.blit_text()
        # self._check_upgrade()
        self.increase_time()



    # def _check_upgrade(self):
    #     if settupg.score < settupg.upgrade_cost_click:
    #         self.settings.upgrade_button_color = (255,0,0)
    #     else:
    #         self.settings.upgrade_button_color = (0,255,0)
    #     if settupg.score < settupg.upgrade_passive_cost:
    #         self.settings.upgrade_passive_button_color = (255,0,0)
    #     else:
    #         self.settings.upgrade_passive_button_color = (0,255,0)

    def increase_time(self): # Absolutnie nie mam pojęcia jak to działa ale działa XD
        current_time = pyg.time.get_ticks()
        if current_time > self.settings.time_shit:
            self.settings.time_shit = current_time + 1000
            all_passive = (settupg.iron_passive_income + settupg.copper_passive_income +
                            settupg.silver_passive_income + settupg.gold_passive_income +
                            settupg.diamond_passive_income + settupg.emerald_passive_income + 
                            settupg.rubin_passive_income + settupg.jadeit_passive_income +
                            settupg.amethyst_passive_income)
            settupg.all_passive = all_passive
            settupg.score += all_passive
            settupg.score = round(settupg.score, 1)


    def format_text(self,score):
        score_str = str(score)
        signs = []
        signs[:] = score_str
        if score >= 1000 and score < 10000:
            score_formated = f'{signs[0]},{signs[1]}{signs[2]}K'
            return score_formated


        elif score >= 10000 and score < 100000:
            score_formated = f'{signs[0]}{signs[1]},{signs[2]}K'
            return score_formated

        elif score >= 100000 and score < 1000000:
            score_formated = f'{signs[0]}{signs[1]}{signs[2]}K'
            return score_formated

        elif score >= 1000000 and score < 10000000:
            score_formated = f'{signs[0]},{signs[1]}{signs[2]}M'
            return score_formated

        elif score >= 10000000 and score < 100000000:
            score_formated = f'{signs[0]}{signs[1]},{signs[2]}M'
            return score_formated

        elif score >= 100000000 and score < 1000000000:
            score_formated = f'{signs[0]}{signs[1]}{signs[2]}M'
            return score_formated

        elif score >= 1000000000 and score < 10000000000:
            score_formated = f'{signs[0]},{signs[1]}{signs[2]}B'
            return score_formated

        elif score >= 10000000000 and score < 100000000000:
            score_formated = f'{signs[0]}{signs[1]},{signs[2]}B'
            return score_formated

        elif score >= 100000000000 and score < 1000000000000:
            score_formated = f'{signs[0]}{signs[1]}{signs[2]}B'
            return score_formated


        elif score >= 1000000000000 and score < 10000000000000:
            score_formated = f'{signs[0]},{signs[1]}{signs[2]}T'
            return score_formated

        elif score >= 10000000000000 and score < 100000000000000:
            score_formated = f'{signs[0]}{signs[1]},{signs[2]}T'
            return score_formated

        elif score >= 100000000000000 and score < 1000000000000000:
            score_formated = f'{signs[0]}{signs[1]}{signs[2]}T'
            return score_formated

        elif score >= 1000000000000000 and score < 10000000000000000:
            score_formated = f'{signs[0]},{signs[1]}{signs[2]}Q'
            return score_formated

        elif score >= 10000000000000000 and score < 100000000000000000:
            score_formated = f'{signs[0]}{signs[2]},{signs[3]}Q'
            return score_formated

        elif score >= 100000000000000000 and score < 1000000000000000000:
            score_formated = f'{signs[0]}{signs[2]}{signs[3]}Q'
            return score_formated

        elif score >= 1000000000000000000 and score < 10000000000000000000:
            score_formated = f'{signs[0]},{signs[2]}{signs[3]}S'
            return score_formated

        elif score >= 10000000000000000000 and score < 100000000000000000000:
            score_formated = f'{signs[0]}{signs[2]},{signs[3]}S'
            return score_formated

        elif score >= 100000000000000000000 and score < 1000000000000000000000:
            score_formated = f'{signs[0]}{signs[2]}{signs[3]}S'
            return score_formated

        elif score >= 1000000000000000000000 and score < 10000000000000000000000:
            score_formated = f'{signs[0]},{signs[2]}{signs[3]}X'
            return score_formated

        elif score >= 10000000000000000000000 and score < 100000000000000000000000:
            score_formated = f'{signs[0]}{signs[2]},{signs[3]}X'
            return score_formated

        elif score >= 100000000000000000000000 and score < 1000000000000000000000000:
            score_formated = f'{signs[0]}{signs[2]}{signs[3]}X'
            return score_formated

        elif score >= 1000000000000000000000000:
            score_formated = f'STOP IT, Get some help'
            return score_formated

        else:
            score = str(score)
            signs = []
            signs[:] = score
            score_formated = ''

            for value in signs[0:3]:
                score_formated += value

            return score_formated

