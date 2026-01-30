for _ in range(int(input())):
    n = int(input())
    lis = list(map(int, input().split()))
    l, r = 0,0
    for i in range(n):
        if lis[i] == (n-i):
            continue
        else:
            l = i
            r = lis.index((n-i))
            break

    lis2 = lis[:l] + lis[l:r+1][::-1] + lis[r+1:]
    print(*lis2)        