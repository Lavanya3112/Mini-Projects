print("BMI calculator")

print('''     
________________________
|                       |
|   BMI CALCULATOR      |
|_______________________|
|  Height (m): _______  |
|  Weight (kg): _______ |
|                       |
|  [ CALCULATE BMI ]    |
|_______________________|
|  Your BMI: _________  |
|_______________________|

''')

height = float(input("Enter your height in metres: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight / (height ** 2)

print(f"Your BMI is {round(bmi, 2)}")

if bmi < 18.5:
    print("Category: Malnourished")

elif 18.5 <= bmi < 25:
    print("Category: Healthy")

elif 25 <= bmi < 30:
    print("Category: Overweight")

else:
    print("Category: Obesity")
