list_cities = [ 'Oakland', 'Atlanta', 'New York City', 'Seattle', 'Memphis', 'Miami', 'Boston', "L'os Angeles", 'Denver', 'New Orleans' ]

list_cities[0] = 'San Francisco'
list_cities[2] = 'Brooklyn'
list_cities[7] = 'Hollywood'
list_cities[5] = 'Tampa'

del list_cities[8]
list_cities.pop(4)
list_cities.remove('Boston')
print(list_cities)



fav_cities = list_cities[2:5]
fav_cities.append('Las Vegas')
print(fav_cities)

fav_food = ['Pizza', 'Burger', 'French fried', 'Mac cheese']
top_food = fav_food[1:4]
top_food.append('Rice')
print(top_food)