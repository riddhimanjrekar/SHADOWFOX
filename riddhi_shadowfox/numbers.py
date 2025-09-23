# -----------------------------------------------
# 1. Using format() function
# -----------------------------------------------
def format_number(num, rep):
    # 'o' is used to convert the number into octal representation
    result = format(num, rep)
    return result

formatted_value = format_number(145, 'o')
print("1. Formatted Result:", formatted_value)
print("Representation used: Octal (Base 8)")
print("-" * 40)


# -----------------------------------------------
# 2. Area of Circular Pond and Total Water
# -----------------------------------------------
# Given values
radius = 84  # in meters
pi = 3.14

# Formula: Area = π * r^2
pond_area = pi * (radius ** 2)
print("2. Area of the Pond:", pond_area)

# Bonus: Total water
water_per_sq_meter = 1.4  # liters
total_water = pond_area * water_per_sq_meter

# Print without decimal point
print("Total Water in Pond (Liters):", int(total_water))
print("-" * 40)


# -----------------------------------------------
# 3. Speed Calculation
# -----------------------------------------------
distance = 490  # in meters
time_minutes = 7  # in minutes

# Convert time to seconds
time_seconds = time_minutes * 60  # 7 minutes = 420 seconds

# Formula: Speed = Distance / Time
speed = distance / time_seconds

# Print speed without decimal point
print("3. Speed in meters/second:", int(speed))
