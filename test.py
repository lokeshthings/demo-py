name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Hello", name)
print("You are", age, "years old")

# Calculate age next year
next_age = age + 1
print("Next year, you will be", next_age)

# Check whether the person is an adult
if age >= 18:
    print("You are an adult.")
else:
    print("You are under 18.")

# Greeting based on age
if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")