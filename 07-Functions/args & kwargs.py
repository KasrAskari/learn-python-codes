

car_colors = {1: 'blue', 2: "red", 3: "green", 4: "white", 5: "black"}


def car_info(*args , **kwargs):
    print(args) #?() List
    print(kwargs) #?{} Dictionary 
    
    
cities = ["Tehran", "Paris"]    
specs = {"brand": "Ford", "model": "Mustang"}
    
car_info(*cities, **specs)    
#car_info("Tehran", "Paris", brand="Ford", model="Mustang")