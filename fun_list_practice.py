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
#print(fav_cities)

fav_food = ['Pizza', 'Burger', 'French fried', 'Mac cheese']
top_food = fav_food[1:4]
top_food.append('Rice')
print(top_food)



def name_cities(city):
    for c in city:
        print(c)
    return "US cities"

def cities(x):

    print(x)
    counter = 0 
    while counter < len(x):
        city = x[counter]
        city2 = x[counter + 1]
        if len(city) >= len(city2):
            counter += 1
            continue
        elif counter + 1 == len(x) - 1:
            break
        else:
            x.remove(city)
            x.append(city2)

    return x
    
print(name_cities(list_cities))
print(cities(list_cities))



def food(f):
    f.append('Meat')
    return f
print(food(fav_food))
