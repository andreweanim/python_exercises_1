import random

# Simulation of coin
def flip_coin():

  if random.random() < 0.5:
    return "H"  # Heads
  else:
    return "T"  # Tails

def simulate_flips():
 
  flips = ""  # storing the sequence of flips
  count = 0
  consecutive_count = 0

  while True:
    flip = flip_coin()
    flips += flip
    count += 1

    if flip == flips[count - 2]:  # Check for two consecutive flips
      consecutive_count += 1
    else:
      consecutive_count = 1

    if consecutive_count == 3:
      break

  print(f"Flips: {flips}")
  print(f"Number of flips: {count}")

if __name__ == "__main__":
  simulate_flips()