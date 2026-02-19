import math
for _ in range(int(input())):
    n,k = list(map(int, input().split()))
    lis = list(map(int, input().split()))

    last_found = 0
    for i in range(n):
        if lis[i] == last_found + 1:
            last_found += 1
    
    counter = n - last_found
    print(math.ceil(counter/k))
