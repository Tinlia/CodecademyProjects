def semi_prime_count(n):
  # Find a list of primes
  primes = []
  semiprimes = []
  for i in range(2,n):
    prime = True
    for k in range(2,i):
      if i%k==0 and i!=k: prime=False
      k += 1
    if prime: primes.append(i)
  print(primes)

  # Multiply primes against eachother until >n then iterate
  for i in primes:
    for k in primes:
      if i*k < n: 
        semiprimes.append(i*k)
  return len(list(set(semiprimes)))

semi_prime_count(10)
