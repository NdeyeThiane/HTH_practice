dict_name = {'Chicken':'$1.59', 'Beef':'$1.99', 'Cheese':'$1.00', 'Milk':'$2.50'}
print(dict_name['Chicken'])
chicken = dict_name['Chicken']
beef = dict_name['Beef']
cheese = dict_name['Cheese']
milk = dict_name['Milk']

del dict_name['Cheese']
del dict_name['Milk']
print(dict_name)

fav_food = {'Food1':'Pizza', 'Food2': 'Burger', 'Food3': 'French fried', 'Food4': 'Mac cheese'}
food1 = fav_food['Food1']
food2 = fav_food['Food2']
food3 = fav_food['Food3']
food4 = fav_food['Food4']
# print(food1)
# print(food2)
# print(food3)
# print(food4)

fav_food['Food1'] = 'Veggie Pizza'
fav_food['Food5'] = 'Rice'

del fav_food['Food3']
del fav_food['Food1']
print(fav_food)

dict_shoes ={'Jordan13': 1, 'Yeezy': 8, 'Foamposite': 10, 'Air Max': 5,'SB Dunk':20 }

dict_shoes['SB Dunk'] = 22
dict_shoes['Yeezy'] = 13
dict_shoes['Jordan13'] = 5
dict_shoes['Air Max'] = 9
dict_shoes['Foamposite'] = 14
dict_shoes['Nike Air force'] = 8
dict_shoes['Valentino Rockstud'] = 4
del dict_shoes['Yeezy']
del dict_shoes['Foamposite']
print(dict_shoes)
