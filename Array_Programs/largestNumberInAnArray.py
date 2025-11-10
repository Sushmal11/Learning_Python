def largest():
    max = 0
    for x in arr:
        if x>max:
            max = x
    return(max)

if __name__=="__main__":
    arr = [1,2,3,4,5]
    ans = largest()
    print(ans)

