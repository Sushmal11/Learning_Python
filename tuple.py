tuple1 = ("Rohan", "Physics", 21, 69.75)
tuple2 = (1, 2, 3, 4, 5)

#Accessing the items with index
print (tuple1[0])
print (tuple2[2])

#Accessing elements with negative index
print(tuple1[-1])
print(tuple2[-3])

#Accessing rangle of tuple with negative index
print(tuple2[2:-1])

#Accessing elements using slice operator
print(tuple2[:2])

#Concattaion of tuple
tuple1 = tuple1+tuple2
print(tuple1)

#Unpacking the tuple
a, b, c, d, e = tuple2
print(a)

#Unpacking the tuple with '*' symbol as a prefix for a variable
a, *b = tuple2
print(b)
*a, b = tuple2
print(a)

# extend method
# We can join tuples using the extend() function by temporarily converting the tuples into lists, 
# performing the joining operation as if they were lists, and then converting the resulting list back into a tuple.
list1 = list(tuple1)
list2 = list(tuple2)
list1.extend(list2)
tuple1 = tuple(list1)
print(tuple1)

#sum method
tuple1 = sum((tuple1, tuple2), ())
print(tuple1)