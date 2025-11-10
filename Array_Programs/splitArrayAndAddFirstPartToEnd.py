arr = [1,2,3,4,5,6,7]
#print(arr[2:])
b=arr[2:]
print(b)
for x in range(0, 2):
    b.append(arr[x])
print(b)