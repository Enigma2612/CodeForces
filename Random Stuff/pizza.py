cases = []
for _ in range(int(input())):
    cases.append(int(input()))

for num in cases:
    if not num % 2:
        print(num//2 - 1)
    else:
        print((num+1)//2 - 1)