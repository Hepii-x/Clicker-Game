import pygame as pyg
import settings
import upgradesettings as settupg





class Upgrades():

    def increase_score(self):
        settupg.score += settupg.multiplier_click
        settupg.score = round(settupg.score, 1)
        print(settupg.score)

    def increase_passive(self):
        if settupg.score < settupg.upgrade_passive_cost:
            pass
        else:
            settupg.score -= settupg.upgrade_passive_cost
            settupg.passive_income += 2
            settupg.upgrade_passive_cost *= 1.5

    def increase_multiplier(self):
        if settupg.score < settupg.upgrade_cost_click:
            pass
        else:
            settupg.score -= settupg.upgrade_cost_click
            settupg.multiplier_click += 2
            settupg.upgrade_cost_click *= 1.5