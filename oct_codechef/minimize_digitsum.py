def dig_sum(n):
    c = 0
    sum = n
    while(sum > 9):
        n = sum
        sum = 0
        c += 1
        while (n > 0):
            sum = sum+(n % 10)
            n = n//10
    return [sum, c]


def main():
    k = int(input())
    for i in range(k):
        n, d = map(int, input().split())
        a = n
        c = 0
        dict = {}

        while (True):
            t = dig_sum(n)
            key = t[0]
            if t[0] in dict:
                break
            else:
                dict[key] = c+t[1]
            c += 1
            n = n+d
        temp = dig_sum(a)
        m = temp[0]
        dict[m] = temp[1]
        k = min(dict)
        v = dict[k]
        print (k, end=" ")
        print (v)


main()
