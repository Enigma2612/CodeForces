for _ in range(int(input())):
    n,k = list(map(int, input().split()))
    time = 0
    if n == k:
        print(0)
    else:
        while n > k:
            if not n%2:
                n = n//2
                time += 1
                if k == n:
                    print(time)
                    break
            else:
                time += 1
                a,b = (n+1)//2, (n-1)//2
                n = a if a%2 else b

                if k in [a,b]:
                    print(time)
                    break
        else:
            print(-1)


            