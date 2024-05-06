

#### AND ####

a = 200
b = 300
c = 500

if a > b and c > a:
    print("both conditionds are TRUE")

    
#### OR ####

a = 200
b = 300
c = 500

if a>b or a>c:
    print("at least one of the condition is TRUE")
    

#### NOT ####
#%%
a = 33
b = 200

if not a>b:
    print("a is NOT greater than b")
    
    
#### Nested if ####
#%%
x = 41

if x>10:
    print("Above ten,")
    if x>20:
        print("and also above 20!")
    else:
        print("but not above 20!")
        
        
#### PASS ####
#%%
a = 33
b = 200

if b>a:
    pass

# %%
