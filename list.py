# Declaration of list
list1 = [1,2,3,4,5]
print(list1)

#Accessing list values
print(list1[0])
print(list1[0:3])

#Updating list values
list1[2]=7
print(list1)

#delete list value
del list1[3]
print(list1)

#Change consecutive list items:
list2 = ['x', 'y']
list1[1:3]= list2
print(list1)

#Change range of list items
list3 = ['A', 'B', 'C']
list1[1:3] = list3
print(list1)

#Adding items to list
list1.append('p')
list1.insert(1, 'q')
list1.extend(list2)
print(list1)

#Remove items from list
list1.remove('x')
list1.pop(3)
list2.clear()
del list1[2]
del list1[1:4]
print(list1)

#Loops in list
for x in list1:
    print(x, end=' ')

#list methods:
# list1.append(obj)
# list1.clear()
# list1.copy()
# list1.extend(seq)
# list1.count(obj)
# list1.insert(index, obj)
# list1.index(obj)
# list1.pop(obj=list1[-1])
# list1.remove(obj)
# list1.reverse()
# list1.sort()
# comp(list1, list2)
# len(list1)
# max(list1)
# min(list1)
# list(seq)