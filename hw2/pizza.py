flour = float(input("Please type the total weight of the flour in terms of grams: "))
water_per = float(input("Please type the total percentage of water you wish for: "))

water = (water_per/100) * flour
salt = flour * 0.02
olive_oil = flour * 0.02
yeast = flour * 0.012

print("Flour (grams):", flour)
print('Hydration (%):', water_per)

print('\nRecipe\n-----')
print('Flour: {:.1f} g'.format(flour))
print('Water: {:.1f} g'.format(water))
print('Salt: {:.1f} g'.format(salt))
print('Olive Oil: {:.1f} g'.format(olive_oil))
print('Yeast: {:.1f} g'.format(yeast))