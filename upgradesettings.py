import json



def load_save():
    with open('save.json') as file:
        save = json.load(file)
        return save
def save_save(save):
    with open('save.json', 'w') as file:
        save['score'] = score
        save['iron_ore'] = iron_ore
        save['iron_pickaxe'] = iron_pickaxe
        save['copper_ore'] = copper_ore
        save['copper_pickaxe'] = copper_pickaxe
        save['silver_ore'] = silver_ore
        save['silver_pickaxe'] = silver_pickaxe
        save['gold_ore'] = gold_ore
        save['gold_pickaxe'] = gold_pickaxe
        save['diamond_ore'] = diamond_ore
        save['diamond_pickaxe'] = diamond_pickaxe
        save['emerald_ore'] = emerald_ore
        save['emerald_pickaxe'] = emerald_pickaxe
        save['rubin_ore'] = rubin_ore
        save['rubin_pickaxe'] = rubin_pickaxe
        save['jadeit_ore'] = jadeit_ore
        save['jadeit_pickaxe'] = jadeit_pickaxe
        save['amethyst_ore'] = amethyst_ore
        save['amethyst_pickaxe'] = amethyst_pickaxe
        save['iron_ore_cost'] = iron_ore_cost
        save['iron_pickaxe_cost'] = iron_pickaxe_cost
        save['copper_ore_cost'] = copper_ore_cost
        save['copper_pickaxe_cost'] = copper_pickaxe_cost
        save['silver_ore_cost'] = silver_ore_cost
        save['silver_pickaxe_cost'] = silver_pickaxe_cost
        save['gold_ore_cost'] = gold_ore_cost
        save['gold_pickaxe_cost'] = gold_pickaxe_cost
        save['diamond_ore_cost'] = diamond_ore_cost
        save['diamond_pickaxe_cost'] = diamond_pickaxe_cost
        save['emerald_ore_cost'] = emerald_ore_cost
        save['emerald_pickaxe_cost'] = emerald_pickaxe_cost
        save['rubin_ore_cost'] = rubin_ore_cost
        save['rubin_pickaxe_cost'] = rubin_pickaxe_cost
        save['jadeit_ore_cost'] = jadeit_ore_cost
        save['jadeit_pickaxe_cost'] = jadeit_pickaxe_cost
        save['amethyst_ore_cost'] = amethyst_ore_cost
        save['amethyst_pickaxe_cost'] = amethyst_pickaxe_cost
        save['iron_ore_multiplier'] = iron_ore_multiplier
        save['iron_pickaxe_multiplier'] = iron_pickaxe_multiplier
        save['copper_ore_multiplier'] = copper_ore_multiplier
        save['copper_pickaxe_multiplier'] = copper_pickaxe_multiplier
        save['silver_ore_multiplier'] = silver_ore_multiplier
        save['silver_pickaxe_multiplier'] = silver_pickaxe_multiplier
        save['gold_ore_multiplier'] = gold_ore_multiplier
        save['gold_pickaxe_multiplier'] = gold_pickaxe_multiplier
        save['diamond_ore_multiplier'] = diamond_ore_multiplier
        save['diamond_pickaxe_multiplier'] = diamond_pickaxe_multiplier
        save['emerald_ore_multiplier'] = emerald_ore_multiplier
        save['emerald_pickaxe_multiplier'] = emerald_pickaxe_multiplier
        save['rubin_ore_multiplier'] = rubin_ore_multiplier
        save['rubin_pickaxe_multiplier'] = rubin_pickaxe_multiplier
        save['jadeit_ore_multiplier'] = jadeit_ore_multiplier
        save['jadeit_pickaxe_multiplier'] = jadeit_pickaxe_multiplier
        save['amethyst_ore_multiplier'] = amethyst_ore_multiplier
        save['amethyst_pickaxe_multiplier'] = amethyst_pickaxe_multiplier
        save['all_passive'] = all_passive
        save['iron_passive_income'] = iron_passive_income
        save['copper_passive_income'] = copper_passive_income
        save['silver_passive_income'] = silver_passive_income
        save['gold_passive_income'] = gold_passive_income
        save['diamond_passive_income'] = diamond_passive_income
        save['emerald_passive_income'] = emerald_passive_income
        save['rubin_passive_income'] = rubin_passive_income
        save['jadeit_passive_income'] = jadeit_passive_income
        save['amethyst_passive_income']   = amethyst_passive_income
        save['base_click'] = base_click
        save['iron_click'] = iron_click
        save['copper_click'] = copper_click
        save['silver_click'] = silver_click
        save['gold_click'] = gold_click
        save['diamond_click'] = diamond_click
        save['emerald_click'] = emerald_click
        save['rubin_click'] = rubin_click
        save['jadeit_click'] = jadeit_click
        save['amethyst_click'] = amethyst_click
        json.dump(save, file, indent=4)

save = load_save()
score = save['score']




iron_ore = save['iron_ore']
iron_pickaxe = save['iron_pickaxe']

copper_ore = save['copper_ore']
copper_pickaxe = save['copper_pickaxe']

silver_ore = save['silver_ore']
silver_pickaxe = save['silver_pickaxe']

gold_ore = save['gold_ore']
gold_pickaxe = save['gold_pickaxe']

diamond_ore = save['diamond_ore']
diamond_pickaxe = save['diamond_pickaxe']

emerald_ore = save['emerald_ore']
emerald_pickaxe = save['emerald_pickaxe']

rubin_ore = save['rubin_ore']
rubin_pickaxe = save['rubin_pickaxe']

jadeit_ore = save['jadeit_ore']
jadeit_pickaxe = save['jadeit_pickaxe']

amethyst_ore = save['amethyst_ore']
amethyst_pickaxe = save['amethyst_pickaxe']



iron_ore_cost = save['iron_ore_cost']
iron_pickaxe_cost = save['iron_pickaxe_cost']

copper_ore_cost = save['copper_ore_cost']
copper_pickaxe_cost = save['copper_pickaxe_cost']

silver_ore_cost = save['silver_ore_cost']
silver_pickaxe_cost = save['silver_pickaxe_cost']

gold_ore_cost = save['gold_ore_cost']
gold_pickaxe_cost = save['gold_pickaxe_cost']

diamond_ore_cost = save['diamond_ore_cost']
diamond_pickaxe_cost = save['diamond_pickaxe_cost']

emerald_ore_cost = save['emerald_ore_cost']
emerald_pickaxe_cost = save['emerald_pickaxe_cost']

rubin_ore_cost = save['rubin_ore_cost']
rubin_pickaxe_cost = save['rubin_pickaxe_cost']

jadeit_ore_cost = save['jadeit_ore_cost']
jadeit_pickaxe_cost = save['jadeit_pickaxe_cost']

amethyst_ore_cost = save['amethyst_ore_cost']
amethyst_pickaxe_cost = save['amethyst_pickaxe_cost']




iron_ore_multiplier = save['iron_ore_multiplier']
iron_pickaxe_multiplier = save['iron_pickaxe_multiplier']

copper_ore_multiplier = save['copper_ore_multiplier']
copper_pickaxe_multiplier = save['copper_pickaxe_multiplier']

silver_ore_multiplier = save['silver_ore_multiplier']
silver_pickaxe_multiplier = save['silver_pickaxe_multiplier']

gold_ore_multiplier = save['gold_ore_multiplier']
gold_pickaxe_multiplier = save['gold_pickaxe_multiplier']

diamond_ore_multiplier = save['diamond_ore_multiplier']
diamond_pickaxe_multiplier = save['diamond_pickaxe_multiplier']

emerald_ore_multiplier = save['emerald_ore_multiplier']
emerald_pickaxe_multiplier = save['emerald_pickaxe_multiplier']

rubin_ore_multiplier = save['rubin_ore_multiplier']
rubin_pickaxe_multiplier = save['rubin_pickaxe_multiplier']

jadeit_ore_multiplier = save['jadeit_ore_multiplier']
jadeit_pickaxe_multiplier = save['jadeit_pickaxe_multiplier']

amethyst_ore_multiplier = save['amethyst_ore_multiplier']
amethyst_pickaxe_multiplier = save['amethyst_pickaxe_multiplier']



all_passive = save['all_passive']



iron_passive_income = save['iron_passive_income']
copper_passive_income = save['copper_passive_income']
silver_passive_income = save['silver_passive_income']
gold_passive_income = save['gold_passive_income']
diamond_passive_income = save['diamond_passive_income']
emerald_passive_income = save['emerald_passive_income']
rubin_passive_income = save['rubin_passive_income']
jadeit_passive_income = save['jadeit_passive_income']
amethyst_passive_income = save['amethyst_passive_income']


base_click = save['base_click']
iron_click = save['iron_click']
copper_click = save['copper_click']
silver_click = save['silver_click']
gold_click = save['gold_click']
diamond_click = save['diamond_click']
emerald_click = save['emerald_click']
rubin_click = save['rubin_click']
jadeit_click = save['jadeit_click']
amethyst_click = save['amethyst_click']












