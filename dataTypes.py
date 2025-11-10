var1 = 1       # int data type
var2 = True    # bool data type
var3 = 10.023  # float data type
var4 = 10+3j   # complex data type

#String datatype
str = 'Hello World!'
print (str)          # complete string
print (str[0])       # first character of the string
print (str[2:5])     # characters starting from 3rd to 5th
print (str[2:])      # tring starting from 3rd character
print (str * 2)      # string two times
print (str + "TEST") # concatenated string

#list datatype
list1 = ['abcd', 's', 2.222, 3]
list2 = [['abcd', 's', 2.222, 3], [1, 'sushma', 2.2]]
print(list1)            # complete list
print(list1[0])         # first element of the list
print(list1[1:3])       # elements starting from 2nd till 3rd 
print(list1[2:])        # elements starting from 3rd element
print(list1 * 2)        # list two times
print(list2[1])         #first element of 2nd sublist
print(list2[1][2])      #second element of second sublist of list2

#Tuple dataType
t1 = ( 'abcd', 786 , 2.23, 'john', 70.2  )
t2 = (123, 'john')
print (t1[0])            # Prints first element of the tuple
print (t1[1:3])          # Prints elements of the tuple starting from 2nd till 3rd 
print (t1[2:])           # Prints elements of the tuple starting from 3rd element
print (t2 * 2)       # Prints the contents of the tuple twice
print (t1 + t2)   # Prints concatenated tuples

#Range Datatype
#Syntax: range(start, stop, step)
for i in range(5):
 print(i)

for i in range(1, 5):
 print(i)

for i in range(1, 5, 2):
 print(i)

#Boolean datatype
a = 2
b = 4
print(bool(a==b))
print(a==b)
a = None
print(bool(a))
a = ()
print(bool(a))
a = 0.0
print(bool(a))
a = 10
print(bool(a))

#DataType conversion
a = 1
print(int(a))
print(float(a))
a = 45
print(str(a))
a="4+5"
print(eval(a))
a=[1,2,3]
print(tuple(a))