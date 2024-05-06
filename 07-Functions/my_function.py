

def my_function(fname):
    print(fname + " Askari")

my_function("Alireza")
my_function("Masi")
my_function("Kasra")


##########################


def my_function2(fname, lname):
    print(fname + " " + lname) 

my_function2("Kasra", "Askari")


###########################


# def my_function3(*persons):
#     print("The youngest person is " +persons[1])

# my_function3("Alireza", "Kasra", "Masi")    


def my_function3(person3, person2, person1):
    print("The youngest person is " + person3)
    
my_function3(person1 = "Masi", person2 = "Alireza", person3 = "Kasra")


##########################


def my_function4(**person):
    print("His last name is " + person["lname"])

my_function4(fname = "Kasra", lname = "Askari")


##########################


def my_function5(country = "Iran"):
    print("I am from " + country)
    
my_function5("Sweden")
my_function5("Brazil")
my_function5("Canada")
my_function5()
my_function5("Brazil")


#########################

#%%
def return_function(x):
    return 5 * x

print(return_function(3))
print(return_function(5))
print(return_function(9))
# %%
