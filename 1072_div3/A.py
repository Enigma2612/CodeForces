for _ in range(int(input())):
    n = int(input())
    if n <= 3:
        print(n)
    elif not n%2:
        print(0)
    else:
        print(1)
