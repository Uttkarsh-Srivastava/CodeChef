def operations(a, b):
    c = 0
    while (c < len(a)-2):
        if (a[c] < b[c]):
            k = b[c]-a[c]
            a[c] += k*1
            a[c+1] += k * 2
            a[c+2] += k*3
        else:
            c += 1
    if a == b:
        return 0


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        A = input().split()[:n]
        B = input().split()[:n]
        a = [int(x) for x in A]
        b = [int(x) for x in B]
        if operations(a, b) == 0:
            print("TAK")
        else:
            print("NIE")


main()
