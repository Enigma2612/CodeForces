for _ in range(int(input())):
    s,k,m = list(map(int, input().split()))

    if not m:
        print(0)
        continue

    if s <= k:
        print(max(s - m%k, 0))
    else:
        if m%k:
            print(max(k - m%k, 0))
        else:
            print([s,k][(m//k)%2])


#WRONG ANS