# 1.
def format_number(num, rep):
    
    result = format(num, rep)
    return result

formatted_value = format_number(145, 'o')
print("1. Formatted Result:", formatted_value)
print("Representation used: Octal (Base 8)")
print("-" * 40)


# 2.
radius = 84  
pi = 3.14

# Formula (Area = π * r^2)
pond_area = pi * (radius ** 2)
print("2. Area of the Pond:", pond_area)


water_per_sq_meter = 1.4 
total_water = pond_area * water_per_sq_meter


print("Total Water in Pond (Liters):", int(total_water))
print("-" * 40)


# 3.
distance = 490  
time_minutes = 7  


time_seconds = time_minutes * 60  

# Formula (Speed = Distance / Time)
speed = distance / time_seconds

# Print
print("3. Speed in meters/second:", int(speed))


