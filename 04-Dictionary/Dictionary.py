
#& Key: Value
car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1965,
    'colors':['red','blue']
    }


#print(len(car))
#print(car.values())
#print(car.items())


""" for key in car.keys():
    print(key) """

for key, value in car.items():
    print(key, '_______' , value)

        
#print(car)

#print(car['brand'])



###? Change the values ###

#car['brand'] = 'Chevrolet'
#car['model'] = 'Corvette'
#car['year'] = 1963
#car['city'] = 'Tehran'


######? Update ######

#car.update({'brand': 'Chevrolet', 'model': 'Corvette', 'year': 1963, 'colors':['red','blue'], 'city': 'Tehran'})
#print(car)



######! unknown ######
#print(car.get('city', 'be khoda nadaram'))



######? Delete ######

#^ Method 1:
#del car['model']

#^ Method 2:
#brand = car.pop('brand')
#print(car)