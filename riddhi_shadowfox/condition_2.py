# Program to determine which country a city belongs to

# Step 1: Define the lists of cities for each country
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

# Step 2: Take user input
city = input("Enter a city name: ")

# Step 3: Check which country the city belongs to
if city in Australia:
    print(f"{city} is in Australia")
elif city in UAE:
    print(f"{city} is in UAE")
elif city in India:
    print(f"{city} is in India")
else:
    print(f"Sorry, {city} is not in our list.")
