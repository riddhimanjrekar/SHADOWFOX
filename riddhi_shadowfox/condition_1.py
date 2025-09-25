# if condition Q1

#Take user input
height = float(input("Enter height in meters: "))  
weight = float(input("Enter weight in kilograms: "))  

#calcalate bmi (formula)
bmi = weight / (height ** 2)  

# deciding bmi category
print("\nYour BMI is:", round(bmi, 2))

if bmi >= 30:
    print("Category: Obesity")
elif 25 <= bmi < 30:
    print("Category: Overweight")
elif 18.5 <= bmi < 25:
    print("Category: Normal")
else:
    print("Category: Underweight")

