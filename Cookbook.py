# This is a little interactive cookbook written from scratch by myself.

print('Please choose a recipe you want to cook (type in number): ')
print('(1) Pancakes')
print('(2) Cheesecake')
print('(3) Waffles')

# Choose your recipe:
recipe = input('Please type in your number: ')
portions = input('Please type in the number of portions you want to cook: ')

# Pancake recipe:
pe = (int(portions) * 2) / 7  # Eggs
pm = (int(portions) * 200) / 7  # Milk
ps = (int(portions) * 1) / 7  # Sugar
pslt = (int(portions) * 1) / 7  # Salt
pf = (int(portions) * 200) / 7  # Flour
psw = (int(portions) * 60) / 7  # Soda

# Cheesecake recipe:
# Cake ingredients
cpf = int(portions) * 200  # Flour
cps = int(portions) * 100  # Sugar
cpb = int(portions) * 100  # Butter
cpvs = int(portions) * 1  # Vanillasugar
cbs = int(portions) * 1  # Backingsoda
cpe = int(portions) * 1  # Egg
# Topping ingredients
tpq = int(portions) * 500  # Quark
tpvp = int(portions) * 1  # Vanillapudding
tpe = int(portions) * 1  # Egg
tpo = int(portions) * 2  # Oil
tpm = int(portions) * 250  # Milk
tps = int(portions) * 160  # Sugar
tplj = int(portions) * 1  # Lemonjuice

# Waffle recipe
wpb = (int(portions) * 125) / 10  # Butter
wps = (int(portions) * 100) / 10  # Sugar
wpvs = (int(portions) * 1) / 10  # Vanillasugar
wpe = (int(portions) * 3) / 10  # Eggs
wpf = (int(portions) * 250) / 10  # Flour
wpslt = (int(portions) * 1) / 10  # Salt
wpbs = (int(portions) * 1) / 10  # Backingsoda
wpm = (int(portions) * 200) / 10  # Milk

# Very clever portions calculator:
if recipe == '1':
    for x in ['Pancake-recipe for ' + str(portions) + ' pancake(s): ', str(pe) + ' Eggs', str(pm) + 'ml Milk', str(ps) +
              ' dash(es) of Sugar', str(pslt) + ' dash(es) of Salt', str(pf) + 'g of Flour',
              str(psw) + 'ml of Soda-water']:
        print(x)
    print('Instructions: Mix that shit together and slap it in a pan gurl.')
elif recipe == '2':
    for y in ['Cheesecake-recipe for ' + str(portions) + ' cake(s): ', 'Ingredients for cake: ',
              str(cpf) + 'g Flour', str(cps) + 'g Sugar', str(cpb) + 'g Butter', str(cpvs) + 'pkg(s) Vanillasugar',
              str(cbs) + 'dash(es) of Backingsoda', str(cpe) + 'Egg(s)', 'Ingredients for topping: ',
              str(tpq) + 'g Quark', str(tpvp) + 'pkg(s) Vanillapudding', str(tpe) + 'Egg(s)', str(tpo) + 'tbs of Oil',
              str(tpm) + 'ml Milk', str(tps) + 'g Sugar', str(tplj) + 'dash(es) Lemonjuice']:
        print(y)
    print('Instructions: Steer all that shit together, slap it together and throw it into the oven, '
          'better a furnace, until ready.')
elif recipe == '3':
    for z in ['Waffles-recipe for ' + str(portions) + ' waffle(s): ', str(wpb) + 'g Butter', str(wps) + 'g Sugar',
              str(wpvs) + 'pkg(s) Vanillasugar', str(wpe) + ' Egg(s)', str(wpf) + 'g Flour',
              str(wpslt) + ' dash(es) of Salt', str(wpbs) + ' tsp(s) of Backingsoda', str(wpm) + 'ml Milk']:
        print(z)
    print('Instructions: Mix that shyte togetha brotha and slappp it onto the waffleiron laddy.')
else:
    print('There is no recipe with that number.')

input('To end this program, please push any button.')
