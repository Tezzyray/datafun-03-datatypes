import statistics  
import math


# TASK 3 NUMERIC LISTS AND LIST STATISTICS
list1=[2,10,30,5,7,9,12,13,54,68,76,62,32,21,33,44,60,78,98,77]
mean_list1=statistics.mean(list1)
median_list1=statistics.median(list1)
mode_list1=statistics.mode(list1)

print('the mean of list1 is:', mean_list1)
print('The median is :', median_list1)
print('The mode is :', mode_list1)

stdev_list1=statistics.stdev(list1)
variance_list1=statistics.variance(list1)

print('The standard deviation is :', stdev_list1)
print('The variance is :', variance_list1)

#CORRELATION AND PREDICTION
listx= list(range(10, 101,10))
listy= [10.5,12.3,14.6,16.5,17.9,19.5,21.3,22.5,23.4,24.6]
x_y_correlation=statistics.correlation(listx,listy)

print('correlation between listx and listy:', x_y_correlation)


slope, intercept=statistics.linear_regression(listx, listy)
futurex=101
futurey=slope*futurex+intercept
print('The future y at futurex=15 is: ', int(futurey))

#USING BUILT IN PYTHON FUNCTION
max_y=max(listy)
print('maximum value in listy is:', max_y)
min_y=min(listy)
print('minimum value in listy is:', min_y)
len_y=len(listy)
print('the lenght of listy is:', len_y)
sum_y=sum(listy)
print('the sum of values in listy is: ',  sum_y)
avg_y=sum_y/len_y
print('the average value for listy is: ' ,avg_y)

#sorting the list in ascending order

ascend_listy=sorted(listy)

#sorting in descending order.
descend_listy= sorted(listy, reverse=True)

print('This is listy in descending order: ' , descend_listy)

#LIST METHODS
lst=[40,89,93,90,34]
lst_new=lst.append(300)
print('this is a new list with another value:', {lst_new})

lst2=[9,8,7]
ext_list=lst2.extend({lst_new})
print('this is the extended list: ', {ext_list})

lst.insert(2,100)
print (f'list after inserting a new value:' , lst)

lst.remove(100)
print(f'this is the list after removing a value:', lst)

lst.append(89)

lst.count(89)
print('89 appears on the list', lst.count,'times')

lst.sort()
print('This is the list in ascending order:', lst)

lst.sort(reverse=True)
print('This is the list in descending order:', lst)

#copying the list to a new list

lst_new= lst.copy()
print('This is the copied list:', lst_new)

first_pop=lst_new.pop(0)

print('This is the list after removing first value from lst_new:', first_pop)

last_pop=lst_new.pop(-1)
print('This is the list after removing the last value:', last_pop)

#LIST TRANSFORMATIONS
LIST_5 = [1,2,3,4,5,6,7,8]
List_5_filtered=list(filter(lambda x : x < 4, LIST_5))
print('This is the list filtered for any value less than 4', List_5_filtered)

LIST_5_MAP= list(map(lambda x : x **3, LIST_5))
print('The cube root for all values in the list are:', LIST_5_MAP)

#Volume of a cube with same sides
side=4
Volume_Cube=list(map(lambda side:side**3, {side}))
print('The volume of the cube is :', Volume_Cube)


#LIST COMPREHENSION
list1_new=[x for x in list1 if x< 8]
print('New list after filtering using comprehension is :', list1_new)

#Getting triple value
list1_triple= [x *3 for x in list1]
print('This is the triple value if list1:', list1_triple)

# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    print("your code here")


# Why? Why only print if this the module called?
# Because when you write good functions, you may want to
# import this module into another script - just like you did
# math or statistics.
# Build a library of resuable functions to support your domain.

# For example, if your domain:
# Is sports, create functions to provide a list of teams.
# Is pets, create functions to calculate adoption prices.
# Is music, create functions to return a list of your favorite artists.


# When you write reusable functions for your domain, you can
# import the module with your utility functions into other modules
# and use them there.  This is a very common practice.
# Anything you write can be imported into later projects.

