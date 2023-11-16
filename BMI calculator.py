#BMI index calculator
print("Welcome to BMI calculator!")
weight=float(input("Enter your weight in kgs:"))
height=float(input("Enter your height in metres:"))
BMI=weight/(height**2)
print("Your BMI is:",round(BMI,3))
if(BMI<=18.5):
    print("You are underweight as your BMI is less than 18.5")
elif(BMI>18.5 and BMI<=24.9):
    print("You are of normal weight.")
elif(BMI > 24.9 and  BMI<=29.9):
    print("You are overweight as your BMI is between 24.9 and 29.9")
else:
    print("You are obese as your BMI is above 30")
    



