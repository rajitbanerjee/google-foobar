def solution(n):

    # Recursive approach (too slow)
    def rec(n):
        if n == 1:
            return 0
        elif n % 2 == 1:
            # Odd numbers have two steps: +1,/2 or -1,/2
            return min(rec((n - 1) // 2) + 2, rec((n + 1) // 2) + 2)
        else:
            # Even numbers have one step: /2
            return rec(n // 2) + 1

    # Iterative/Bit manipulation approach
    def bit_man(n, count=0):
        while n > 1:
            if n & 1:
                # if odd, subtract 1 if n just passed 2 or a multiple of 4
                n += 1 * -1 if (n == 3 or n % 4 == 1) else 1
            else:
                # if even, always /2
                n = n >> 1
            count += 1
        return count

    return bit_man(int(n))


if __name__ == '__main__':
    print(solution('3'))
    print(solution('15'))
