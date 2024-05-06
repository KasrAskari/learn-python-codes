colors = ['red', 'green', 'blue']
colors_2 = ['white', 'black',]
numbers = [4, 8, 23, 56, 2]



colors_set1 = {'red', 'green', 'blue', 'white'}
colors_set2 = {'green', 'blue', 'white', 'black'}
numbers_2 = [4, 8, 8, 23, 56, 2, 2, 44, 44] #list
numbers_set = set(numbers_2)

#print(set(numbers_2))
#print(len(set(numbers_2)))

#print(4 in numbers_set)

print(colors_set1.union(colors_set2))
print(colors_set1.intersection(colors_set2))
print(colors_set1.difference(colors_set2))
print(colors_set2.difference(colors_set1))



########### EMPTY ###########

#List
numbs_list = []
numbs_list = list()

#tuple
numbs_tup = ()
nums_tup = tuple()

#set
numbs_set = {} #dictionary
numbs_set = set()