# for loop

fruits = ['apple', 'Banana', 'mango']
for f in fruits:
    print(f)
    
for i in range(5):
    print(i)
for i in range(2,5):
    print(i)
for i in range(1,5,2):
    print(i)
for i in "print":
    print(i)

#loops with dictonaries
x = {10:"Ten", 20:"Twenty", 30:"Thirty"}
for n in x:
    print(n, ":", x[n])
for n in x:
    print(n)
for n in x:
    print(x[n])

#loops with tuples
numbers = (1,2,3,4,5,6)
total = 0
for num in numbers:
    total+=num
print(total)

#loops with lists
numberss = [10,20,30,40,50,23,24,25,]
tot = 0
for num in numberss:
    if(num%2==0):
        print(num)

#for-else loops
for count in range(6):
    print(count)
else:
    print("numbers")
print("numbers in series")

#while loops
count = 0
while(count<5):
    count += 1
    print(count)
else:
    print("c")
print("count")

#break statement
for letter in 'Python':    
   if letter == 'h':
      break
   print (letter)
print ("Good bye!")

#Continue statement
for letter in 'Python':
   if letter == 'h':
      continue
   print (letter)
print ("Good bye!")