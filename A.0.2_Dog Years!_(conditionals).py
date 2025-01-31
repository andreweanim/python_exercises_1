# Getting the human age from the user
human_age = float(input("Enter the human age: "))

# Check for invalid input
if human_age < 0:
  print("Age can't be a negative value.")
else:
  # Calculating dog years
  if human_age <= 2:
    dog_years = human_age * 10.5
  else:
    dog_years = 2 * 10.5 + (human_age - 2) * 4

  print(f"The equivalent dog age is: {dog_years:.2f} years")