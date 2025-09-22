weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))



height_in_meters = height / 100  # Convert height from cm to meters if needed
bmi = weight / (height_in_meters ** 2)
print("Your BMI is:", bmi)

if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:    
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")

    if 30 <= bmi < 35:
            print("You are in Obesity Class I!")
    elif 35 <= bmi < 40:
            print("You are in Obesity Class II!")
    else:
            print("You are in Obesity Class III (Severely Obese)!")