for _ in range(int(input())):
    n = int(input())
    lis = list(map(int, input().split()))
    print(max(lis)*len(lis))