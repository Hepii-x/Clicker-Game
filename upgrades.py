from sys import settrace
import pygame as pyg
import settings
import upgradesettings as settupg





class Upgrades():

    def increase_score(self):
        all_click = (settupg.iron_click + settupg.copper_click + settupg.silver_click +
                    settupg.gold_click + settupg.diamond_click + settupg.emerald_click + 
                    settupg.rubin_click + settupg.jadeit_click + settupg.amethyst_click + settupg.base_click)

        settupg.score += all_click
        settupg.score = round(settupg.score, 1)
        print(f'Click {all_click}\n Passive {settupg.all_passive}')


            
            



    def buy_iron_pickaxe(self):
        if settupg.score < settupg.iron_pickaxe_cost:
            pass
        else:
            if settupg.iron_pickaxe == 0:
                settupg.iron_pickaxe += 1
                settupg.iron_click = (settupg.iron_pickaxe_multiplier * settupg.iron_pickaxe) * 1
                settupg.score -= settupg.iron_pickaxe_cost
                settupg.iron_pickaxe_cost = 17 * (1.06)**settupg.iron_pickaxe
            
            elif settupg.iron_pickaxe >= 1 and settupg.iron_pickaxe < 25:
                settupg.iron_pickaxe += 1
                settupg.iron_click = (settupg.iron_pickaxe_multiplier * settupg.iron_pickaxe) * 1
                settupg.score -= settupg.iron_pickaxe_cost
                settupg.iron_pickaxe_cost = 17 * (1.06)**settupg.iron_pickaxe

            elif settupg.iron_pickaxe >= 25 and settupg.iron_pickaxe < 50:
                settupg.iron_pickaxe += 1
                settupg.iron_click = (settupg.iron_pickaxe_multiplier * settupg.iron_pickaxe) * 1.5
                settupg.score -= settupg.iron_pickaxe_cost
                settupg.iron_pickaxe_cost = 17 * (1.06)**settupg.iron_pickaxe

            elif settupg.iron_pickaxe >= 50 and settupg.iron_pickaxe < 100:
                settupg.iron_pickaxe += 1
                settupg.iron_click = (settupg.iron_pickaxe_multiplier * settupg.iron_pickaxe) * 2.25
                settupg.score -= settupg.iron_pickaxe_cost
                settupg.iron_pickaxe_cost = 17 * (1.06)**settupg.iron_pickaxe

            else:
                settupg.iron_pickaxe += 1
                settupg.iron_click = (settupg.iron_pickaxe_multiplier * settupg.iron_pickaxe) * 3
                settupg.score -= settupg.iron_pickaxe_cost
                settupg.iron_pickaxe_cost = 17 * (1.06)**settupg.iron_pickaxe


    def buy_copper_pickaxe(self):

        if settupg.score < settupg.copper_pickaxe_cost:
            pass
        else:
            if settupg.copper_pickaxe == 0:
                settupg.copper_pickaxe += 1
                settupg.copper_click = (settupg.copper_pickaxe_multiplier * settupg.copper_pickaxe) * 1
                settupg.score -= settupg.copper_pickaxe_cost
                settupg.copper_pickaxe_cost = 148 * (1.08)**settupg.copper_pickaxe
            
            elif settupg.copper_pickaxe >= 1 and settupg.copper_pickaxe < 25:
                settupg.copper_pickaxe += 1
                settupg.copper_click = (settupg.copper_pickaxe_multiplier * settupg.copper_pickaxe) * 1
                settupg.score -= settupg.copper_pickaxe_cost
                settupg.copper_pickaxe_cost = 148 * (1.08)**settupg.copper_pickaxe

            elif settupg.copper_pickaxe >= 25 and settupg.copper_pickaxe < 50:
                settupg.copper_pickaxe += 1
                settupg.copper_click = (settupg.copper_pickaxe_multiplier * settupg.copper_pickaxe) * 1.5
                settupg.score -= settupg.copper_pickaxe_cost
                settupg.copper_pickaxe_cost = 148 * (1.08)**settupg.copper_pickaxe

            elif settupg.copper_pickaxe >= 50 and settupg.copper_pickaxe < 100:
                settupg.copper_pickaxe += 1
                settupg.copper_click = (settupg.copper_pickaxe_multiplier * settupg.copper_pickaxe) * 2.25
                settupg.score -= settupg.copper_pickaxe_cost
                settupg.copper_pickaxe_cost = 148 * (1.08)**settupg.copper_pickaxe

            else:
                settupg.copper_pickaxe += 1
                settupg.copper_click = (settupg.copper_pickaxe_multiplier * settupg.copper_pickaxe) * 3
                settupg.score -= settupg.copper_pickaxe_cost
                settupg.copper_pickaxe_cost = 148 * (1.08)**settupg.copper_pickaxe

    def buy_silver_pickaxe(self):

        if settupg.score < settupg.silver_pickaxe_cost:
            pass
        else:
            if settupg.silver_pickaxe == 0:
                settupg.silver_pickaxe += 1
                settupg.silver_click = (settupg.silver_pickaxe_multiplier * settupg.silver_pickaxe) * 1
                settupg.score -= settupg.silver_pickaxe_cost
                settupg.silver_pickaxe_cost = 831 * (1.1)**settupg.silver_pickaxe
            
            elif settupg.silver_pickaxe >= 1 and settupg.silver_pickaxe < 25:
                settupg.silver_pickaxe += 1
                settupg.silver_click = (settupg.silver_pickaxe_multiplier * settupg.silver_pickaxe) * 1
                settupg.score -= settupg.silver_pickaxe_cost
                settupg.silver_pickaxe_cost = 831 * (1.1)**settupg.silver_pickaxe

            elif settupg.silver_pickaxe >= 25 and settupg.silver_pickaxe < 50:
                settupg.silver_pickaxe += 1
                settupg.silver_click = (settupg.silver_pickaxe_multiplier * settupg.silver_pickaxe) * 1.5
                settupg.score -= settupg.silver_pickaxe_cost
                settupg.silver_pickaxe_cost = 831 * (1.1)**settupg.silver_pickaxe

            elif settupg.silver_pickaxe >= 50 and settupg.silver_pickaxe < 100:
                settupg.silver_pickaxe += 1
                settupg.silver_click = (settupg.silver_pickaxe_multiplier * settupg.silver_pickaxe) * 2.25
                settupg.score -= settupg.silver_pickaxe_cost
                settupg.silver_pickaxe_cost = 831 * (1.1)**settupg.silver_pickaxe

            else:
                settupg.silver_pickaxe += 1
                settupg.silver_click = (settupg.silver_pickaxe_multiplier * settupg.silver_pickaxe) * 3
                settupg.score -= settupg.silver_pickaxe_cost
                settupg.silver_pickaxe_cost = 831 * (1.1)**settupg.silver_pickaxe

    def buy_gold_pickaxe(self):

        if settupg.score < settupg.gold_pickaxe_cost:
            pass
        else:
            if settupg.gold_pickaxe == 0:
                settupg.gold_pickaxe += 1
                settupg.gold_click = (settupg.gold_pickaxe_multiplier * settupg.gold_pickaxe) * 1
                settupg.score -= settupg.gold_pickaxe_cost
                settupg.gold_pickaxe_cost = 4655 * (1.12)**settupg.gold_pickaxe
            
            elif settupg.gold_pickaxe >= 1 and settupg.gold_pickaxe < 25:
                settupg.gold_pickaxe += 1
                settupg.gold_click = (settupg.gold_pickaxe_multiplier * settupg.gold_pickaxe) * 1
                settupg.score -= settupg.gold_pickaxe_cost
                settupg.gold_pickaxe_cost = 4655 * (1.12)**settupg.gold_pickaxe

            elif settupg.gold_pickaxe >= 25 and settupg.gold_pickaxe < 50:
                settupg.gold_pickaxe += 1
                settupg.gold_click = (settupg.gold_pickaxe_multiplier * settupg.gold_pickaxe) * 1.5
                settupg.score -= settupg.gold_pickaxe_cost
                settupg.gold_pickaxe_cost = 4655 * (1.12)**settupg.gold_pickaxe

            elif settupg.gold_pickaxe >= 50 and settupg.gold_pickaxe < 100:
                settupg.gold_pickaxe += 1
                settupg.gold_click = (settupg.gold_pickaxe_multiplier * settupg.gold_pickaxe) * 2.25
                settupg.score -= settupg.gold_pickaxe_cost
                settupg.gold_pickaxe_cost = 4655 * (1.12)**settupg.gold_pickaxe

            else:
                settupg.gold_pickaxe += 1
                settupg.gold_click = (settupg.gold_pickaxe_multiplier * settupg.gold_pickaxe) * 3
                settupg.score -= settupg.gold_pickaxe_cost
                settupg.gold_pickaxe_cost = 4655 * (1.12)**settupg.gold_pickaxe

    def buy_diamond_pickaxe(self):

        if settupg.score < settupg.diamond_pickaxe_cost:
            pass
        else:
            if settupg.diamond_pickaxe == 0:
                settupg.diamond_pickaxe += 1
                settupg.diamond_click = (settupg.diamond_pickaxe_multiplier * settupg.diamond_pickaxe) * 1
                settupg.score -= settupg.diamond_pickaxe_cost
                settupg.diamond_pickaxe_cost = 26087 * (1.14)**settupg.diamond_pickaxe
            
            elif settupg.diamond_pickaxe >= 1 and settupg.diamond_pickaxe < 25:
                settupg.diamond_pickaxe += 1
                settupg.diamond_click = (settupg.diamond_pickaxe_multiplier * settupg.diamond_pickaxe) * 1
                settupg.score -= settupg.diamond_pickaxe_cost
                settupg.diamond_pickaxe_cost = 26087 * (1.14)**settupg.diamond_pickaxe

            elif settupg.diamond_pickaxe >= 25 and settupg.diamond_pickaxe < 50:
                settupg.diamond_pickaxe += 1
                settupg.diamond_click = (settupg.diamond_pickaxe_multiplier * settupg.diamond_pickaxe) * 1.5
                settupg.score -= settupg.diamond_pickaxe_cost
                settupg.diamond_pickaxe_cost = 26087 * (1.14)**settupg.diamond_pickaxe

            elif settupg.diamond_pickaxe >= 50 and settupg.diamond_pickaxe < 100:
                settupg.diamond_pickaxe += 1
                settupg.diamond_click = (settupg.diamond_pickaxe_multiplier * settupg.diamond_pickaxe) * 2.25
                settupg.score -= settupg.diamond_pickaxe_cost
                settupg.diamond_pickaxe_cost = 26087 * (1.14)**settupg.diamond_pickaxe

            else:
                settupg.diamond_pickaxe += 1
                settupg.diamond_click = (settupg.diamond_pickaxe_multiplier * settupg.diamond_pickaxe) * 3
                settupg.score -= settupg.diamond_pickaxe_cost
                settupg.diamond_pickaxe_cost = 26087 * (1.14)**settupg.diamond_pickaxe

    def buy_emerald_pickaxe(self):

        if settupg.score < settupg.emerald_pickaxe_cost:
            pass
        else:
            if settupg.emerald_pickaxe == 0:
                settupg.emerald_pickaxe += 1
                settupg.emerald_click = (settupg.emerald_pickaxe_multiplier * settupg.emerald_pickaxe) * 1
                settupg.score -= settupg.emerald_pickaxe_cost
                settupg.emerald_pickaxe_cost = 146202 * (1.16)**settupg.emerald_pickaxe
            
            elif settupg.emerald_pickaxe >= 1 and settupg.emerald_pickaxe < 25:
                settupg.emerald_pickaxe += 1
                settupg.emerald_click = (settupg.emerald_pickaxe_multiplier * settupg.emerald_pickaxe) * 1
                settupg.score -= settupg.emerald_pickaxe_cost
                settupg.emerald_pickaxe_cost = 146202 * (1.16)**settupg.emerald_pickaxe

            elif settupg.emerald_pickaxe >= 25 and settupg.emerald_pickaxe < 50:
                settupg.emerald_pickaxe += 1
                settupg.emerald_click = (settupg.emerald_pickaxe_multiplier * settupg.emerald_pickaxe) * 1.5
                settupg.score -= settupg.emerald_pickaxe_cost
                settupg.emerald_pickaxe_cost = 146202 * (1.16)**settupg.emerald_pickaxe

            elif settupg.emerald_pickaxe >= 50 and settupg.emerald_pickaxe < 100:
                settupg.emerald_pickaxe += 1
                settupg.emerald_click = (settupg.emerald_pickaxe_multiplier * settupg.emerald_pickaxe) * 2.25
                settupg.score -= settupg.emerald_pickaxe_cost
                settupg.emerald_pickaxe_cost = 146202 * (1.16)**settupg.emerald_pickaxe

            else:
                settupg.emerald_pickaxe += 1
                settupg.emerald_click = (settupg.emerald_pickaxe_multiplier * settupg.emerald_pickaxe) * 3
                settupg.score -= settupg.emerald_pickaxe_cost
                settupg.emerald_pickaxe_cost = 146202 * (1.16)**settupg.emerald_pickaxe


    def buy_rubin_pickaxe(self):

        if settupg.score < settupg.rubin_pickaxe_cost:
            pass
        else:
            if settupg.rubin_pickaxe == 0:
                settupg.rubin_pickaxe += 1
                settupg.rubin_click = (settupg.rubin_pickaxe_multiplier * settupg.rubin_pickaxe) * 1
                settupg.score -= settupg.rubin_pickaxe_cost
                settupg.rubin_pickaxe_cost = 819374 * (1.18)**settupg.rubin_pickaxe
            
            elif settupg.rubin_pickaxe >= 1 and settupg.rubin_pickaxe < 25:
                settupg.rubin_pickaxe += 1
                settupg.rubin_click = (settupg.rubin_pickaxe_multiplier * settupg.rubin_pickaxe) * 1
                settupg.score -= settupg.rubin_pickaxe_cost
                settupg.rubin_pickaxe_cost = 819374 * (1.18)**settupg.rubin_pickaxe

            elif settupg.rubin_pickaxe >= 25 and settupg.rubin_pickaxe < 50:
                settupg.rubin_pickaxe += 1
                settupg.rubin_click = (settupg.rubin_pickaxe_multiplier * settupg.rubin_pickaxe) * 1.5
                settupg.score -= settupg.rubin_pickaxe_cost
                settupg.rubin_pickaxe_cost = 819374 * (1.18)**settupg.rubin_pickaxe

            elif settupg.rubin_pickaxe >= 50 and settupg.rubin_pickaxe < 100:
                settupg.rubin_pickaxe += 1
                settupg.rubin_click = (settupg.rubin_pickaxe_multiplier * settupg.rubin_pickaxe) * 2.25
                settupg.score -= settupg.rubin_pickaxe_cost
                settupg.rubin_pickaxe_cost = 819374 * (1.18)**settupg.rubin_pickaxe

            else:
                settupg.rubin_pickaxe += 1
                settupg.rubin_click = (settupg.rubin_pickaxe_multiplier * settupg.rubin_pickaxe) * 3
                settupg.score -= settupg.rubin_pickaxe_cost
                settupg.rubin_pickaxe_cost = 819374 * (1.18)**settupg.rubin_pickaxe


    def buy_jadeit_pickaxe(self):

        if settupg.score < settupg.jadeit_pickaxe_cost:
            pass
        else:
            if settupg.jadeit_pickaxe == 0:
                settupg.jadeit_pickaxe += 1
                settupg.jadeit_click = (settupg.jadeit_pickaxe_multiplier * settupg.jadeit_pickaxe) * 1
                settupg.score -= settupg.jadeit_pickaxe_cost
                settupg.jadeit_pickaxe_cost = 4592106 * (1.2)**settupg.jadeit_pickaxe
            
            elif settupg.jadeit_pickaxe >= 1 and settupg.jadeit_pickaxe < 25:
                settupg.jadeit_pickaxe += 1
                settupg.jadeit_click = (settupg.jadeit_pickaxe_multiplier * settupg.jadeit_pickaxe) * 1
                settupg.score -= settupg.jadeit_pickaxe_cost
                settupg.jadeit_pickaxe_cost = 4592106 * (1.2)**settupg.jadeit_pickaxe

            elif settupg.jadeit_pickaxe >= 25 and settupg.jadeit_pickaxe < 50:
                settupg.jadeit_pickaxe += 1
                settupg.jadeit_click = (settupg.jadeit_pickaxe_multiplier * settupg.jadeit_pickaxe) * 1.5
                settupg.score -= settupg.jadeit_pickaxe_cost
                settupg.jadeit_pickaxe_cost = 4592106 * (1.2)**settupg.jadeit_pickaxe

            elif settupg.jadeit_pickaxe >= 50 and settupg.jadeit_pickaxe < 100:
                settupg.jadeit_pickaxe += 1
                settupg.jadeit_click = (settupg.jadeit_pickaxe_multiplier * settupg.jadeit_pickaxe) * 2.25
                settupg.score -= settupg.jadeit_pickaxe_cost
                settupg.jadeit_pickaxe_cost = 4592106 * (1.2)**settupg.jadeit_pickaxe

            else:
                settupg.jadeit_pickaxe += 1
                settupg.jadeit_click = (settupg.jadeit_pickaxe_multiplier * settupg.jadeit_pickaxe) * 3
                settupg.score -= settupg.jadeit_pickaxe_cost
                settupg.jadeit_pickaxe_cost = 4592106 * (1.2)**settupg.jadeit_pickaxe

    def buy_amethyst_pickaxe(self):

        if settupg.score < settupg.amethyst_pickaxe_cost:
            pass
        else:
            if settupg.amethyst_pickaxe == 0:
                settupg.amethyst_pickaxe += 1
                settupg.amethyst_click = (settupg.amethyst_pickaxe_multiplier * settupg.amethyst_pickaxe) * 1
                settupg.score -= settupg.amethyst_pickaxe_cost
                settupg.amethyst_pickaxe_cost = 25736049 * (1.22)**settupg.amethyst_pickaxe
            
            elif settupg.amethyst_pickaxe >= 1 and settupg.amethyst_pickaxe < 25:
                settupg.amethyst_pickaxe += 1
                settupg.amethyst_click = (settupg.amethyst_pickaxe_multiplier * settupg.amethyst_pickaxe) * 1
                settupg.score -= settupg.amethyst_pickaxe_cost
                settupg.amethyst_pickaxe_cost = 25736049 * (1.22)**settupg.amethyst_pickaxe

            elif settupg.amethyst_pickaxe >= 25 and settupg.amethyst_pickaxe < 50:
                settupg.amethyst_pickaxe += 1
                settupg.amethyst_click = (settupg.amethyst_pickaxe_multiplier * settupg.amethyst_pickaxe) * 1.5
                settupg.score -= settupg.amethyst_pickaxe_cost
                settupg.amethyst_pickaxe_cost = 25736049 * (1.22)**settupg.amethyst_pickaxe

            elif settupg.amethyst_pickaxe >= 50 and settupg.amethyst_pickaxe < 100:
                settupg.amethyst_pickaxe += 1
                settupg.amethyst_click = (settupg.amethyst_pickaxe_multiplier * settupg.amethyst_pickaxe) * 2.25
                settupg.score -= settupg.amethyst_pickaxe_cost
                settupg.amethyst_pickaxe_cost = 25736049 * (1.22)**settupg.amethyst_pickaxe

            else:
                settupg.amethyst_pickaxe += 1
                settupg.amethyst_click = (settupg.amethyst_pickaxe_multiplier * settupg.amethyst_pickaxe) * 3
                settupg.score -= settupg.amethyst_pickaxe_cost
                settupg.amethyst_pickaxe_cost = 25736049 * (1.22)**settupg.amethyst_pickaxe

    def buy_iron_ore(self):
        if settupg.score < settupg.iron_ore_cost:
            pass
        else:
            if settupg.iron_ore == 0:
                settupg.iron_ore += 1
                settupg.iron_passive_income = (1 * settupg.iron_ore) * 1
                settupg.score -= settupg.iron_ore_cost
                settupg.iron_ore_cost = 5 * (1.05)**settupg.iron_ore
            
            elif settupg.iron_ore >= 1 and settupg.iron_ore < 25:
                settupg.iron_ore += 1
                settupg.iron_passive_income = (1 * settupg.iron_ore) * 1
                settupg.score -= settupg.iron_ore_cost
                settupg.iron_ore_cost = 5 * (1.05)**settupg.iron_ore

            elif settupg.iron_ore >= 25 and settupg.iron_ore < 50:
                settupg.iron_ore += 1
                settupg.iron_passive_income = (1 * settupg.iron_ore) * 1.5
                settupg.score -= settupg.iron_ore_cost
                settupg.iron_ore_cost = 5 * (1.05)**settupg.iron_ore

            elif settupg.iron_ore >= 50 and settupg.iron_ore < 100:
                settupg.iron_ore += 1
                settupg.iron_passive_income = (1 * settupg.iron_ore) * 2.25
                settupg.score -= settupg.iron_ore_cost
                settupg.iron_ore_cost = 5 * (1.05)**settupg.iron_ore

            else:
                settupg.iron_ore += 1
                settupg.iron_passive_income = (1 * settupg.iron_ore) * 3
                settupg.score -= settupg.iron_ore_cost
                settupg.iron_ore_cost = 5 * (1.05)**settupg.iron_ore
            print(settupg.iron_ore_cost)
    def buy_copper_ore(self):
        if settupg.score < settupg.copper_ore_cost:
            pass
        else:
            if settupg.copper_ore == 0:
                settupg.copper_ore += 1
                settupg.copper_passive_income = (settupg.copper_ore_multiplier * settupg.copper_ore) * 1
                settupg.score -= settupg.copper_ore_cost
                settupg.copper_ore_cost = 63 * (1.07)**settupg.copper_ore
            
            elif settupg.copper_ore >= 1 and settupg.copper_ore < 25:
                settupg.copper_ore += 1
                settupg.copper_passive_income = (settupg.copper_ore_multiplier * settupg.copper_ore) * 1
                settupg.score -= settupg.copper_ore_cost
                settupg.copper_ore_cost = 63 * (1.07)**settupg.copper_ore

            elif settupg.copper_ore >= 25 and settupg.copper_ore < 50:
                settupg.copper_ore += 1
                settupg.copper_passive_income = (settupg.copper_ore_multiplier * settupg.copper_ore) * 1.5
                settupg.score -= settupg.copper_ore_cost
                settupg.copper_ore_cost = 63 * (1.07)**settupg.copper_ore

            elif settupg.copper_ore >= 50 and settupg.copper_ore < 100:
                settupg.copper_ore += 1
                settupg.copper_passive_income = (settupg.copper_ore_multiplier * settupg.copper_ore) * 2.25
                settupg.score -= settupg.copper_ore_cost
                settupg.copper_ore_cost = 63 * (1.07)**settupg.copper_ore

            else:
                settupg.copper_ore += 1
                settupg.copper_passive_income = (settupg.copper_ore_multiplier * settupg.copper_ore) * 3
                settupg.score -= settupg.copper_ore_cost
                settupg.copper_ore_cost = 63 * (1.07)**settupg.copper_ore

    def buy_silver_ore(self):
        if settupg.score < settupg.silver_ore_cost:
            pass
        else:
            if settupg.silver_ore == 0:
                settupg.silver_ore += 1
                settupg.silver_passive_income = (settupg.silver_ore_multiplier * settupg.silver_ore) * 1
                settupg.score -= settupg.silver_ore_cost
                settupg.silver_ore_cost = 351 * (1.09)**settupg.silver_ore
            
            elif settupg.silver_ore >= 1 and settupg.silver_ore < 25:
                settupg.silver_ore += 1
                settupg.silver_passive_income = (settupg.silver_ore_multiplier * settupg.silver_ore) * 1
                settupg.score -= settupg.silver_ore_cost
                settupg.silver_ore_cost = 351 * (1.09)**settupg.silver_ore

            elif settupg.silver_ore >= 25 and settupg.silver_ore < 50:
                settupg.silver_ore += 1
                settupg.silver_passive_income = (settupg.silver_ore_multiplier * settupg.silver_ore) * 1.5
                settupg.score -= settupg.silver_ore_cost
                settupg.silver_ore_cost = 351 * (1.09)**settupg.silver_ore

            elif settupg.silver_ore >= 50 and settupg.silver_ore < 100:
                settupg.silver_ore += 1
                settupg.silver_passive_income = (settupg.silver_ore_multiplier * settupg.silver_ore) * 2.25
                settupg.score -= settupg.silver_ore_cost
                settupg.silver_ore_cost = 351 * (1.09)**settupg.silver_ore

            else:
                settupg.silver_ore += 1
                settupg.silver_passive_income = (settupg.silver_ore_multiplier * settupg.silver_ore) * 3
                settupg.score -= settupg.silver_ore_cost
                settupg.silver_ore_cost = 351 * (1.09)**settupg.silver_ore

    def buy_gold_ore(self):
        if settupg.score < settupg.gold_ore_cost:
            pass
        else:
            if settupg.gold_ore == 0:
                settupg.gold_ore += 1
                settupg.gold_passive_income = (settupg.gold_ore_multiplier * settupg.gold_ore) * 1
                settupg.score -= settupg.gold_ore_cost
                settupg.gold_ore_cost = 1967 * (1.11)**settupg.gold_ore
            
            elif settupg.gold_ore >= 1 and settupg.gold_ore < 25:
                settupg.gold_ore += 1
                settupg.gold_passive_income = (settupg.gold_ore_multiplier * settupg.gold_ore) * 1
                settupg.score -= settupg.gold_ore_cost
                settupg.gold_ore_cost = 1967 * (1.11)**settupg.gold_ore

            elif settupg.gold_ore >= 25 and settupg.gold_ore < 50:
                settupg.gold_ore += 1
                settupg.gold_passive_income = (settupg.gold_ore_multiplier * settupg.gold_ore) * 1.5
                settupg.score -= settupg.gold_ore_cost
                settupg.gold_ore_cost = 1967 * (1.11)**settupg.gold_ore

            elif settupg.gold_ore >= 50 and settupg.gold_ore < 100:
                settupg.gold_ore += 1
                settupg.gold_passive_income = (settupg.gold_ore_multiplier * settupg.gold_ore) * 2.25
                settupg.score -= settupg.gold_ore_cost
                settupg.gold_ore_cost = 1967 * (1.11)**settupg.gold_ore

            else:
                settupg.gold_ore += 1
                settupg.gold_passive_income = (settupg.gold_ore_multiplier * settupg.gold_ore) * 3
                settupg.score -= settupg.gold_ore_cost
                settupg.gold_ore_cost = 1967 * (1.11)**settupg.gold_ore

    def buy_diamond_ore(self):
        if settupg.score < settupg.diamond_ore_cost:
            pass
        else:
            if settupg.diamond_ore == 0:
                settupg.diamond_ore += 1
                settupg.diamond_passive_income = (settupg.diamond_ore_multiplier * settupg.diamond_ore) * 1
                settupg.score -= settupg.diamond_ore_cost
                settupg.diamond_ore_cost = 11019 * (1.13)**settupg.diamond_ore
            
            elif settupg.diamond_ore >= 1 and settupg.diamond_ore < 25:
                settupg.diamond_ore += 1
                settupg.diamond_passive_income = (settupg.diamond_ore_multiplier * settupg.diamond_ore) * 1
                settupg.score -= settupg.diamond_ore_cost
                settupg.diamond_ore_cost = 11019 * (1.13)**settupg.diamond_ore

            elif settupg.diamond_ore >= 25 and settupg.diamond_ore < 50:
                settupg.diamond_ore += 1
                settupg.diamond_passive_income = (settupg.diamond_ore_multiplier * settupg.diamond_ore) * 1.5
                settupg.score -= settupg.diamond_ore_cost
                settupg.diamond_ore_cost = 11019 * (1.13)**settupg.diamond_ore

            elif settupg.diamond_ore >= 50 and settupg.diamond_ore < 100:
                settupg.diamond_ore += 1
                settupg.diamond_passive_income = (settupg.diamond_ore_multiplier * settupg.diamond_ore) * 2.25
                settupg.score -= settupg.diamond_ore_cost
                settupg.diamond_ore_cost = 11019 * (1.13)**settupg.diamond_ore

            else:
                settupg.diamond_ore += 1
                settupg.diamond_passive_income = (settupg.diamond_ore_multiplier * settupg.diamond_ore) * 3
                settupg.score -= settupg.diamond_ore_cost
                settupg.diamond_ore_cost = 11019 * (1.13)**settupg.diamond_ore

    def buy_emerald_ore(self):
        if settupg.score < settupg.emerald_ore_cost:
            pass
        else:
            if settupg.emerald_ore == 0:
                settupg.emerald_ore += 1
                settupg.emerald_passive_income = (settupg.emerald_ore_multiplier * settupg.emerald_ore) * 1
                settupg.score -= settupg.emerald_ore_cost
                settupg.emerald_ore_cost = 61757 * (1.15)**settupg.emerald_ore
            
            elif settupg.emerald_ore >= 1 and settupg.emerald_ore < 25:
                settupg.emerald_ore += 1
                settupg.emerald_passive_income = (settupg.emerald_ore_multiplier * settupg.emerald_ore) * 1
                settupg.score -= settupg.emerald_ore_cost
                settupg.emerald_ore_cost = 61757 * (1.15)**settupg.emerald_ore

            elif settupg.emerald_ore >= 25 and settupg.emerald_ore < 50:
                settupg.emerald_ore += 1
                settupg.emerald_passive_income = (settupg.emerald_ore_multiplier * settupg.emerald_ore) * 1.5
                settupg.score -= settupg.emerald_ore_cost
                settupg.emerald_ore_cost = 61757 * (1.15)**settupg.emerald_ore

            elif settupg.emerald_ore >= 50 and settupg.emerald_ore < 100:
                settupg.emerald_ore += 1
                settupg.emerald_passive_income = (settupg.emerald_ore_multiplier * settupg.emerald_ore) * 2.25
                settupg.score -= settupg.emerald_ore_cost
                settupg.emerald_ore_cost = 61757 * (1.15)**settupg.emerald_ore

            else:
                settupg.emerald_ore += 1
                settupg.emerald_passive_income = (settupg.emerald_ore_multiplier * settupg.emerald_ore) * 3
                settupg.score -= settupg.emerald_ore_cost
                settupg.emerald_ore_cost = 61757 * (1.15)**settupg.emerald_ore

    def buy_rubin_ore(self):
        if settupg.score < settupg.rubin_ore_cost:
            pass
        else:
            if settupg.rubin_ore == 0:
                settupg.rubin_ore += 1
                settupg.rubin_passive_income = (settupg.rubin_ore_multiplier * settupg.rubin_ore) * 1
                settupg.score -= settupg.rubin_ore_cost
                settupg.rubin_ore_cost = 346113 * (1.17)**settupg.rubin_ore
            
            elif settupg.rubin_ore >= 1 and settupg.rubin_ore < 25:
                settupg.rubin_ore += 1
                settupg.rubin_passive_income = (settupg.rubin_ore_multiplier * settupg.rubin_ore) * 1
                settupg.score -= settupg.rubin_ore_cost
                settupg.rubin_ore_cost = 346113 * (1.17)**settupg.rubin_ore

            elif settupg.rubin_ore >= 25 and settupg.rubin_ore < 50:
                settupg.rubin_ore += 1
                settupg.rubin_passive_income = (settupg.rubin_ore_multiplier * settupg.rubin_ore) * 1.5
                settupg.score -= settupg.rubin_ore_cost
                settupg.rubin_ore_cost = 346113 * (1.17)**settupg.rubin_ore

            elif settupg.rubin_ore >= 50 and settupg.rubin_ore < 100:
                settupg.rubin_ore += 1
                settupg.rubin_passive_income = (settupg.rubin_ore_multiplier * settupg.rubin_ore) * 2.25
                settupg.score -= settupg.rubin_ore_cost
                settupg.rubin_ore_cost = 346113 * (1.17)**settupg.rubin_ore

            else:
                settupg.rubin_ore += 1
                settupg.rubin_passive_income = (settupg.rubin_ore_multiplier * settupg.rubin_ore) * 3
                settupg.score -= settupg.rubin_ore_cost
                settupg.rubin_ore_cost = 346113 * (1.17)**settupg.rubin_ore

    def buy_jadeit_ore(self):
        if settupg.score < settupg.jadeit_ore_cost:
            pass
        else:
            if settupg.jadeit_ore == 0:
                settupg.jadeit_ore += 1
                settupg.jadeit_passive_income = (settupg.jadeit_ore_multiplier * settupg.jadeit_ore) * 1
                settupg.score -= settupg.jadeit_ore_cost
                settupg.jadeit_ore_cost = 1939756 * (1.19)**settupg.jadeit_ore
            
            elif settupg.jadeit_ore >= 1 and settupg.jadeit_ore < 25:
                settupg.jadeit_ore += 1
                settupg.jadeit_passive_income = (settupg.jadeit_ore_multiplier * settupg.jadeit_ore) * 1
                settupg.score -= settupg.jadeit_ore_cost
                settupg.jadeit_ore_cost = 1939756 * (1.19)**settupg.jadeit_ore

            elif settupg.jadeit_ore >= 25 and settupg.jadeit_ore < 50:
                settupg.jadeit_ore += 1
                settupg.jadeit_passive_income = (settupg.jadeit_ore_multiplier * settupg.jadeit_ore) * 1.5
                settupg.score -= settupg.jadeit_ore_cost
                settupg.jadeit_ore_cost = 1939756 * (1.19)**settupg.jadeit_ore

            elif settupg.jadeit_ore >= 50 and settupg.jadeit_ore < 100:
                settupg.jadeit_ore += 1
                settupg.jadeit_passive_income = (settupg.jadeit_ore_multiplier * settupg.jadeit_ore) * 2.25
                settupg.score -= settupg.jadeit_ore_cost
                settupg.jadeit_ore_cost = 1939756 * (1.19)**settupg.jadeit_ore

            else:
                settupg.jadeit_ore += 1
                settupg.jadeit_passive_income = (settupg.jadeit_ore_multiplier * settupg.jadeit_ore) * 3
                settupg.score -= settupg.jadeit_ore_cost
                settupg.jadeit_ore_cost = 1939756 * (1.19)**settupg.jadeit_ore

    def buy_amethyst_ore(self):
        if settupg.score < settupg.amethyst_ore_cost:
            pass
        else:
            if settupg.amethyst_ore == 0:
                settupg.amethyst_ore += 1
                settupg.amethyst_passive_income = (settupg.amethyst_ore_multiplier * settupg.amethyst_ore) * 1
                settupg.score -= settupg.amethyst_ore_cost
                settupg.amethyst_ore_cost = 10871185 * (1.21)**settupg.amethyst_ore
            
            elif settupg.amethyst_ore >= 1 and settupg.amethyst_ore < 25:
                settupg.amethyst_ore += 1
                settupg.amethyst_passive_income = (settupg.amethyst_ore_multiplier * settupg.amethyst_ore) * 1
                settupg.score -= settupg.amethyst_ore_cost
                settupg.amethyst_ore_cost = 10871185 * (1.21)**settupg.amethyst_ore

            elif settupg.amethyst_ore >= 25 and settupg.amethyst_ore < 50:
                settupg.amethyst_ore += 1
                settupg.amethyst_passive_income = (settupg.amethyst_ore_multiplier * settupg.amethyst_ore) * 1.5
                settupg.score -= settupg.amethyst_ore_cost
                settupg.amethyst_ore_cost = 10871185 * (1.21)**settupg.amethyst_ore

            elif settupg.amethyst_ore >= 50 and settupg.amethyst_ore < 100:
                settupg.amethyst_ore += 1
                settupg.amethyst_passive_income = (settupg.amethyst_ore_multiplier * settupg.amethyst_ore) * 2.25
                settupg.score -= settupg.amethyst_ore_cost
                settupg.amethyst_ore_cost = 10871185 * (1.21)**settupg.amethyst_ore

            else:
                settupg.amethyst_ore += 1
                settupg.amethyst_passive_income = (settupg.amethyst_ore_multiplier * settupg.amethyst_ore) * 3
                settupg.score -= settupg.amethyst_ore_cost
                settupg.amethyst_ore_cost = 10871185 * (1.21)**settupg.amethyst_ore