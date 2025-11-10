counter = 100          # Creates an integer variable
miles   = 1000.0       # Creates a floating point variable
name    = "Zara Ali"
print(counter)
print(miles)
print(name)

# del counter  #Deleting a variable
# print(counter)

print(type(counter))
print(type(miles))

#casting the variable
x = str(10.000)  
y = int(10.989)   
z = float(10)
print(x)
print(y)
print(z)

# multiple assignment
a=b=c= 10
print(b)
print(c)

a, b, c, d, e = 1, 10.0, "rama", 20, 'p'
print(b)
print(c)
print(d)

#Local variable
def sum(a,b):
 res = a+b
 return res
 print(res)
#print(res)

#Global variable
def sum(a,b):
 res = a+b
 return res
print(a)