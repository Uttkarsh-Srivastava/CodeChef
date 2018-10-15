def days(n, l):
    i = d = s = 0
    f = 1
    n = n-1
    while (True):
        d += 1
        for x in range(i, f):
            s += l[x]
        n = n-s
        if n <= 0:
            break
        else:
            i = f
            f = f + s
    return d


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        x = input().split()[:n]
        l = [int(t) for t in x]
        d = days(n, l)
        print (d)


main()
