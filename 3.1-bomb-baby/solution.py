def solution(M, F):
	m, f = map(int, (M, F))
	generations = 0
	while not (m == f == 1):
		if m <= 0 or f <= 0:
			return "impossible"
		elif f == 1:
			# skip m - 1 repetitive steps once we get a 1
			return str(generations + m - 1)
		else:
			generations += m // f
			# Euclid's GCD algorithm! We need the GCD to be 1
			m, f = f, m % f
	return str(generations)

if __name__ == '__main__':
    m = input("M: ")
    f = input("F: ")
    print("Solution: " + solution(m, f))
