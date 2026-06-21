for _ in range(int(input())):
    n = int(input())
    lis = list(map(int, input().split()))

    x = 0

    if len(lis) <= 1:
        print(len(lis))
        continue


    while True:
        lis2 = []
        wrong = 0

        for i in range(len(lis)-1):
            if lis[i] > lis[i+1]:
                wrong += 1
                lis2.append(lis[i])

        lis = lis2.copy()

        if not wrong:
            if not x:
                print(n)
            else:
                print(x)
            break
        else:
            x = wrong
        
            