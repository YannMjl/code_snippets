# Python 3.6 Tutorial for Beginners
# Working with Lists, Tuples, and Sets

#---------------------------------------------------------------------------------------------#
# basic list slicing operation                                                                #
#---------------------------------------------------------------------------------------------#
# initialize an empty List
empty_list = []
empty_list = list()

# let's create a list of fruits
fruits = ['bananas', 'mango', 'berry', 'apple', 'cherry', 'strawberry', 'melon']
print(fruits)

#get the number of item in the list
print('The number of items in the list is:', len(fruits))

# print an item in the list using index
print('the first item in the list is:', fruits[0])
# print the last item on the list 
# the last item can be find by pass index -1 
# this is a good way to find the last item when the lenght of the list is unknown
print('the last item on the list is:', fruits[-1])

# print a range of items in the list
print('these the first 3 items on the list:', fruits[0:3])
# or
print('these the first 3 items on the list:', fruits[:3])
# print item from index 3 to last item on the list, not including item on index 3 
print('these the first 3 items on the list:', fruits[3:])

#---------------------------------------------------------------------------------------------#
# basic list operation                                                                        #
#---------------------------------------------------------------------------------------------#
# add an item on the list at the end of the list
fruits.append('piche')
print('Items on list are:', fruits)

# add item to a specific location in the list
fruits.insert(4, 'durian')
print('Items on list are now:', fruits)

# add multiple items on the list
fruits_2 = ['apricot','pineapple', 'plum', 'orange', 'avocado']
# let's add fruit_2 list to fruits list
fruits.extend(fruits_2)
print('Items on fruits list are now:', fruits)

# remove item from list
fruits.remove('plum')
print('after remove, items on list are now:', fruits)

# pop remove the last item on the list by default and return the item removed
popeditem = fruits.pop()
print('item removed from the list is:', popeditem)

#---------------------------------------------------------------------------------------------#
# list sorting                                                                                #
#---------------------------------------------------------------------------------------------#
# sorted function, return a sorted version of the list
fruit_sorted = sorted(fruits)
print('the sorted version of the list is:', fruit_sorted)

# reverse items on the list
fruits.reverse()
print('after reverse, items on list are now:', fruits)

# sort the list, ascending order by default
fruits.sort()
print('after sorting, items on list are now:', fruits)
# to sort the list in descending order, pass reverse into sort
fruits.sort(reverse=True)
print('after sorting and reversing, items on list are now:', fruits)

#---------------------------------------------------------------------------------------------#
# list of integers
number_list = [3, 5, 6, 2, 7, 4, 9, 1, 8]

# the minimum value in the list
print('The minimum value in the list is:', min(number_list))

# the maximum value in the list
print('The minimum value in the list is:', max(number_list))

# the sum value of number in the list
print('The sum value of number in the list is:', sum(number_list))

# find the index of item in the list
print('The index of 7 in number_list is:', number_list.index(7))
print('The index of "berry" in fruits list is:', fruits.index('berry'))

# check if item exist in the list
print('is 10 in number_list?', 10 in number_list)
print('is mango in fruits list?', 'mango' in fruits)

# read item in the list with a loop
# enumerate return the item and its index
# a start value can be passed in enumerate
for index, item in enumerate(fruits, start=1):
    print(index, item)

#---------------------------------------------------------------------------------------------#
# turn list into a string with join string method
fruit_str1 = ', '.join(fruits)
print('strings of fruits are:', fruit_str1)
# or
fruit_str2 = ' - '.join(fruits)
print('strings of fruits are:', fruit_str2)

# turn string values into a list with split function
new_fruits1 = fruit_str1.split(', ')
print('list made out of fruit_str1 is:', new_fruits1)
# or
new_fruits2 = fruit_str1.split(' - ')
print('list made out of fruit_str2 is:', new_fruits2)

#---------------------------------------------------------------------------------------------#
# Tuples                                                                                      # 
# tuples are similar except list are mutable and tuples are immutable (can't not be modified) #
#---------------------------------------------------------------------------------------------#
# Initialize Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# let's demonstarte the immutability
tuple_1 = ('bananas', 'mango', 'berry', 'apple', 'cherry', 'strawberry', 'melon')
tuple_2 = tuple_1
print('tuple_1 is:', tuple_1)
print('tuple_2 is:', tuple_2)

# now let's try to change item of tuple
# tuple_1[0] = 'peach' 
# the above line gives an error: does not support item assignment 

#---------------------------------------------------------------------------------------------#
# Sets                                                                                        #
# set is a list of unordered values and no duplicate                                          #
#---------------------------------------------------------------------------------------------#
# Initialize Empty Sets
# This isn't right! It's a dict
empty_set = {}  # this is going to create an empty dictionary

# this is the right way to create an empty set
empty_set = set()

set_fruits = {'bananas', 'mango', 'berry', 'apple', 'cherry', 'strawberry', 'apple', 'melon'}
# the order of item in the set will chnage for each excution of print 
# and will eliminate duplicate automaticly
print('items in set of fruits are:', set_fruits)
# sets are optimized for checking items
print('is mango in set of fruits?', 'mango' in set_fruits)

# sets also determine what values sets share or don't share with other sets
# let's create another set
set_fruits_2 = {'peach', 'mango', 'grape', 'apple','cherry', 'apple', 'plum'}
print('The following items exist in both sets:', set_fruits.intersection(set_fruits_2))
print('The following items are in set_fruits but not in set_fruits_2:', 
        set_fruits.difference(set_fruits_2))

# union will combine items of both sets
print('Union of set_fruits and set_fruits_2 is:', set_fruits.union(set_fruits_2))

#---------------------------------------------------------------------------------------------#
