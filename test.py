name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("\nHello", name)
print("You are", age, "years old.")

# Calculate age after 5 years
future_age = age + 5
print("After 5 years, you will be", future_age, "years old.")

# Check age category
if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# Check if the person can vote
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")

# Calculate birth year
birth_year = 2026 - age
print("Your approximate birth year is", birth_year)

# Final message
print("Have a great day,", name + "!")

plz pull this file
