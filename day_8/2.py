## List of Prime Numbers
# Write a function called prime_numbers. This function asks a user to enter a number (integer) as an argument and returns a list of all the prime numbers within its range. For example, if user enters 10, your code should return [2, 3, 5, 7] as prime numbers.

def prime_numbers(n):
  
  primes = []
  for num in range(2, n + 1):
    # Check if the number is divisible by any prime number already found.
    is_prime = True
    for prime in primes:
      if num % prime == 0:
        is_prime = False
        break
    if is_prime:
      primes.append(num)
  return primes

# Example usage
primes = prime_numbers(10)
print(f"Prime numbers within the range (1, 10): {primes}")

'''
output : Prime numbers within the range (1, 10): [2, 3, 5, 7]

'''
