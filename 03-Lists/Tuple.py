colors = ['red', 'green', 'blue']
numbers = [4, 8, 23, 56, 2]



colors_tup = ('red', 'green', 'blue')
print(type(colors_tup))
print(len(colors_tup))

print(colors_tup.count('blue'))
print(colors_tup.index('blue'))

print(dir(colors_tup))

colors_tup[1] = 'sabz'
colors[1] = 'sabz'
print(colors)


###! Lists are mutable ###
###? Tuples are immutable ###



###########* EMPTY ###########

#List
numbs_list = []
numbs_list = list()

#tuple
numbs_tup = ()
nums_tup = tuple()

#set
numbs_set = {} #dictionary
numbs_set = set()