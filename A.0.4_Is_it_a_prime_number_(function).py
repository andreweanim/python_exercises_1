# Checks if input is prime.
def is_prime(x):

  if x <= 1: 
    return False  # Numbers less than or equal to 1 are not prime

  for i in range(2, int(x**0.5) + 1):
    if x % i == 0: 
      return False  # If x is divisible by a number from 2, it's not prime

  return True  # If the loop completes without divisors, x is prime

if __name__ == "__main__":
  num = int(input("Enter an integer: "))
  if is_prime(num):
    print("{} is a prime number.".format(num))
  else:
    print("{} is not a prime number.".format(num))