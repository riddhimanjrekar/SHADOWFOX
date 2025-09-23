# Program to determine BMI Category

# Step 1: Take user input
height = float(input("Enter height in meters: "))  # Example: 1.75
weight = float(input("Enter weight in kilograms: "))  # Example: 70

# Step 2: Calculate BMI
bmi = weight / (height ** 2)  # BMI formula

# Step 3: Determine the BMI category
print("\nYour BMI is:", round(bmi, 2))  # Display BMI rounded to 2 decimal places

if bmi >= 30:
    print("Category: Obesity")
elif 25 <= bmi < 30:
    print("Category: Overweight")
elif 18.5 <= bmi < 25:
    print("Category: Normal")
else:
    print("Category: Underweight")
