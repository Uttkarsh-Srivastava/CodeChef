def serves(p1, p2, k):
    total_points = p1+p2
    if (((total_points//k) % 2) == 0):
        return 0
    return 1


def main():
    t = int(input())
    for i in range(t):
        p1, p2, k = map(int, input().split())
        if (serves(p1, p2, k) == 0):
            print("CHEF")
        else:
            print("COOK")


main()
