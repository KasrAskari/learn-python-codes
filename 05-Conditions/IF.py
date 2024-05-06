

name = "Kasra"
language = "Python"
Online = True
x = 337
condition = False


#%%
#? AND / OR

if name == "Kasra" and language == "Python":
    print("That's right baby!")
else:
    print("hell naaah")
    

if name == "Kasra" or language == "Java":
    print("That's right baby!")
else:
    print("hell naaah")
   
    
#%%
######* ELIF ######

if x < 200:
    print("Increase")
elif 200 <= x < 250:
    print("it's OK")
elif 250 <= x < 350:
    print("hmmm it's OK")
else:
    print("Decrease")
    
    
#################################    
    
#%%
###! None / 0 / [] / {} / () ###

condition = None

if condition:
    print("That's right baby!")
else:
    print("hell naaah")
    
    
condition = 0

if condition:
    print("That's right baby!")
else:
    print("hell naaah")
    

condition = []

if condition:
    print("That's right baby!")
else:
    print("hell naaah")
    
    
print("--------------------")


#%%
###* ? / ?>0 / [?] / {?} / (?) ###

condition = [1]

if condition:
    print("That's right baby!")
else:
    print("hell naaah")    