for _ in range(int(input())):
    n,k = list(map(int, input().split()))
    lis = list(map(int, input().split()))
    lis.sort()  #nlogn
    s = set(lis)

    for choice in s:
        ...