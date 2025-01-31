# Checks if input is prime.

def is_prime(x):

  if x <= 1:
    return False
  for i in range(2, int(x**0.5) + 1):
    if x % i == 0:
      return False
  return True

# Finding the next prime number greater than n.

def next_prime(x):

  x += 1  # Start checking from the next integer
  while not is_prime(x):
    x += 1
  return x

if __name__ == "__main__":
  num = int(input("Enter an integer: "))
  next_prime_num = next_prime(num)
  print(f"The next prime number after {num} is: {next_prime_num}")