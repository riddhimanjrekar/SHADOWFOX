# Program to check if two cities belong to the same country

# Step 1: Define lists of cities for each country
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

# Step 2: Take user input for two cities
city1 = input("Enter the first city: ").strip()
city2 = input("Enter the second city: ").strip()

# Step 3: Check if both cities are in the same country's list
if city1 in Australia and city2 in Australia:
    print(f"Both cities are in Australia")
elif city1 in UAE and city2 in UAE:
    print(f"Both cities are in UAE")
elif city1 in India and city2 in India:
    print(f"Both cities are in India")
else:
    print("They don't belong to the same country")
