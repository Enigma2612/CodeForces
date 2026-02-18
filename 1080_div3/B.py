import math
for _ in range(int(input())):
    n = int(input())
    lis = list(map(int, input().split()))

    for i in range(n):
        el = lis[i]
        a = min(el, i+1)
        b = max(el, i+1)

        if math.log(b/a, 2)%1:
            print("NO")
            break
    else:
        print("YES")