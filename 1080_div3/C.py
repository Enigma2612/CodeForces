for _ in range(int(input())):
    n = int(input())
    lis = list(map(int, input().split()))

    problem_index = [0] * n

    ans = 0

    for p in range(n):
        if p < n-1:
            if lis[p] in {7 - lis[p+1], lis[p+1]}:
                problem_index[p] += 1
        if p > 0:
            if lis[p] in {7 - lis[p-1], lis[p-1]}:
                problem_index[p] += 1
    
    for i in range(n):
        if problem_index[i] == 2:
            ans += 1
            problem_index[i-1] -= 1
            problem_index[i+1] -= 1
    
    ans += problem_index.count(1)//2
    print(ans)