# 1. Create a variable named pi and store the value 22/7 in it. Check its data type.
pi = 22 / 7
print("Value of pi:", pi)
print("Data type of pi:", type(pi))  # This will show the data type

print("-" * 30)

# 2. Create a variable called 'for' and assign it a value 4
# for = 4  # ❌ This will give a SyntaxError because 'for' is a reserved keyword in Python
# print(for)
print("You cannot use 'for' as a variable name because it's a reserved keyword in Python.")

print("-" * 30)

# 3. Calculate Simple Interest (SI = P x R x T / 100)
P = 10000  # Principal amount
R = 5      # Rate of interest
T = 3      # Time in years

SI = (P * R * T) / 100
print("Principal:", P)
print("Rate of Interest:", R)
print("Time (Years):", T)
print("Simple Interest:", SI)
