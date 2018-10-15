def semi_primes():
    semi_prime = []
    prime = []
    l = []
    for i in range(1, 100):
        c = 0
        for j in range(1, i+1):
            if (i % j == 0):
                c += 1
        if c == 2:
            prime.append(i)
    for i in range(len(prime)):
        for j in range(i+1, len(prime)):
            s = prime[i]*prime[j]
            if s <= 200:
                semi_prime.append(s)
    semi_prime = list(set(semi_prime))
    for i in range(len(semi_prime)):
        for j in range(len(semi_prime)):
            s = semi_prime[i]+semi_prime[j]
            if s <= 200:
                l.append(s)
    l = list(set(l))
    return l


def main():
    t = int(input())
    list = semi_primes()
    for i in range(t):
        n = int(input())
        if n in list:
            print("YES")
        else:
            print("NO")


main()
