if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list1 = list(arr)
    set1 = set(list1)
    list2 = list(set1)
    list2.sort(reverse=True)
    rp = list2[1]
    print(rp)
