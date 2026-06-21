for _ in range(int(input())):
    n,k = list(map(int, input().split()))
    lis = list(map(int, list(input())))

    if lis.count(1) == 0:
        print("YES")
        continue
    elif lis.count(1)%2:
        print("NO")
        continue

    p = 0
    c = lis.count(1)
    while c%2 == 0 and p+k < len(lis):
        if lis[p] == 1:
            lis[p] = 0
            c -= 1
            if lis[p+k] == 1:
                c -= 1
            else:
                c += 1
            lis[p+k] = int(not lis[p+k])
            p += 1
        else:
            p += 1
    else:
        if lis.count(1) == 0:
            print("YES")
        else:
            print("NO")