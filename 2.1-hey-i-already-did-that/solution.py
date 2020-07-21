def solution(n, b):
    # Convert an int base 10 to a given base b
    def numberToBase(n, b):
        digits = []
        while n:
            digits.insert(0, str(n % b))
            n = n // b
        return "".join(digits)

    # Algorithm's key iteration step
    def iterate(n, b, k):
        s = sorted(str(n))
        x = "".join(s[::-1])
        y = "".join(s)
        return numberToBase(int(x, b) - int(y, b), b).zfill(k)

    seen, k = [], len(str(n))

    # Find the entry point to the ending cycle
    while n not in seen:
        seen.append(n)
        n = iterate(n, b, k)

    # Compute the length of the ending cycle
    return len(seen) - seen.index(n)


if __name__ == '__main__':
    print(solution(1211, 10))
    print(solution(210022, 3))
