for _ in range(int(input())):
    n = int(input())
    lis = list(map(int, input().split()))

    lis = sorted(set(lis))

    current = 1
    mex = 1

    for i in range(1, len(lis)):
        if lis[i] == lis[i-1] + 1:
            current += 1
        else:
            current = 1
        mex = max(current, mex)


    print(lis)
    print("ANS:", mex)