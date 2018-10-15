def population(N):
    b = 1
    n = B = t = 0
    while (True):
        if N > 2:
            N -= 2
            n = b
            b = 0
        if N > 8:
            N -= 8
            B = n
            n = 0
        if N > 16:
            N -= 16
            b = 2*B
            B = 0
        else:
            break
    return [b, n, B]


def main():
    t = int(input())
    while(t > 0):
        N = int(input())
        a = population(N)
        for x in a:
            print(x, end=" ")
        print()
        t = t-1


main()
