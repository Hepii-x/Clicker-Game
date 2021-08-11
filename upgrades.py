import pygame as pyg
from settings import Settings


class Upgrades():
    def __init__(self):
        self.settings = Settings()

    # def run(self):


    def increase_score(self):
        self.settings.score += self.settings.multiplier
        self.settings.score = round(self.settings.score, 1)
        print(self.settings.score)

    def increase_passive(self):
        if self.settings.score < self.settings.upgrade_passive_cost:
            pass
        else:
            self.settings.score -= self.settings.upgrade_passive_cost
            self.settings.upgrade_passive_cost += 2
            self.settings.passive += 1

    def increase_multiplier(self):
        if self.settings.score < self.settings.upgrade_cost:
            pass
        else:
            self.settings.score -= self.settings.upgrade_cost
            self.settings.upgrade_cost *= 2
            self.settings.multiplier *= 1