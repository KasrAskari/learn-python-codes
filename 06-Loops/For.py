

numbers = [1, 2, 3, 4, 5, 6, 7, 8,]
items = ["ball", "car", "bird"]


#* Break
""" for num in numbers:
    if num == 6:
        break
    print(num) """
    
#* Continue  
""" for num in numbers:
    if num == 6:
        continue
    print(num) """    


##########################


""" for num in numbers:
    for item in "salam":
        print(num, item) """
        
        
""" for num in numbers:
    for item in items:
        print(num, item) """
        
 
#########################
 
#^ range: amounts 0 to 9
""" for i in range(1, 11):
    print(i) """
    
x = 2    
for i in range(3):
    x = x*x
    print(x)