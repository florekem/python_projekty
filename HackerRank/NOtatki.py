N = int(input())



for i in range(N):
    line = input()
    first = ""
    second = ""
    
    for n, l in enumerate(line):
        if n % 2 == 0:
            first += l
        else:
            second += l
    print(first, second)
    