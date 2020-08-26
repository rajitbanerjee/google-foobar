def solution(n):
    # zero matrix
    m = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    # base case
    m[0][0] = 1

    for i in range(1, n + 1):
        for j in range(0, n + 1):
            m[i][j] = m[i - 1][j]
            if j >= i:
                m[i][j] += m[i - 1][j - i]

    return m[n][n] - 1


if __name__ == '__main__':
    print(solution(3))
    print(solution(200))
