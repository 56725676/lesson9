numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for j in numbers:
  is_prime = True
  for i in range(2, j):
    if j % i == 0:
      is_prime = False
  if j != 1:
    if is_prime:
      primes.append(j)
    else:
      not_primes.append(j)
print(f"Primes: {primes}")
print(f"Not Primes: {not_primes}")