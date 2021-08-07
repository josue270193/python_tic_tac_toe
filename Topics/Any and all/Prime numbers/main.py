prime_numbers = [n for n in range(1000) if n > 1 and all(n % divisor != 0 for divisor in range(2, n))]

