'''code snippets in python to perform the following:-
    i)-accessing element to different list
    ii)-accessing element from a tuple
    iii)-deleting different dictionary elements 
    '''
# To access element from the list 
my_list = ['p', 'r', 'o', 'b', 'e']
# For Output: o
print(my_list[2])

# To access elements from a tuple
my_tuple = ('pet','ear','rose','mouse','int','turbo')
# For Output: 'rose
print(my_tuple[0])    

# to delete different dictionary elements
# Create a  dictionary
sixMonths = {'January':31, 'February':28, 'March':31, 'April':30, 'May':31, 'June':30}
#TO delete a specific element from the dictonary i.e. 31
del sixMonths['May']
print(sixMonths)
#To delete all elements from the dictionary
sixMonths.clear()
print(sixMonths)
#To eliminate the dictionary object
del sixMonths
print(sixMonths)
