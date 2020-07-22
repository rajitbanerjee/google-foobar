def solution(pegs):
    n, denom = len(pegs), 1

    # first gear radius = 2 * last gear radius
    R = 2 * sum([(-1)**(i-1) * (pegs[i] - pegs[i-1]) for i in range(1, n)])

    # n is even
    if not n & 1:
        if R % 3 == 0:
            R //= 3
        else:
            denom = 3
    
    # check if all gears fit and touch each other
    def allFit(pegs, R):
        for i in range(1, n):
            diff = pegs[i] - pegs[i-1]
            if not (1 <= R <= diff - 1):
                return False
            R = diff - R
        return True
    
    if allFit(pegs, R // denom):
        return [R, denom]
    else:
        return [-1, -1]


if __name__ == '__main__':
    print(solution([4, 30, 50]))
    print(solution([4, 17, 50]))