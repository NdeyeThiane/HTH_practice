import abc
from types import ClassMethodDescriptorType


dict_name = {'Chicken':1.59, 'Beef':1.99, 'Cheese':1.00, 'Milk':2.50}
#print(dict_name['Chicken'])
chicken = dict_name['Chicken']
beef = dict_name['Beef']
cheese = dict_name['Cheese']
milk = dict_name['Milk']

del dict_name['Chicken']
del dict_name['Milk']
#print(dict_name)

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
#print(fav_food)

dict_shoes ={'Jordan13': 1, 'Yeezy': 8, 'Foamposite': 10, 'Air Max': 5,'SB Dunk':20 }

dict_shoes['SB Dunk'] = 22
dict_shoes['Yeezy'] = 13
dict_shoes['Jordan13'] = 5
dict_shoes['Air Max'] = 9
dict_shoes['Foamposite'] = 14
dict_shoes['Nike Air force'] = 8
dict_shoes['Valentino Rockstud'] = 4
del dict_shoes['Air Max']
del dict_shoes['Foamposite']
#print(dict_shoes)


def t_price(a,b):
    total= dict_name[a] + dict_name[b]
    return total
print(t_price('Cheese','Beef'))

def t_differ(c,d):
    differ = dict_name[c] - dict_name[d]
    return abs(differ)
print(t_differ('Cheese', 'Beef'))

def restock(x,y):
    restock = dict_shoes[x] + y  
    return restock
print(restock('Yeezy', 3))


def clearance(s,n):
    clearnce = dict_shoes[s]//n
    return clearnce
print(clearance('SB Dunk', 2))


