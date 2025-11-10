def sumOfArrayItems(a):
  sum = 0
  for x in a:
    sum = sum + x
  return(sum)

if __name__ == "__main__":
    arr= [1,2,3,4,5]
    ans = sumOfArrayItems(arr)
    print(ans)


