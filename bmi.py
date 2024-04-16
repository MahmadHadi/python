weight = 0
heightFoot = 0
heightInch = 0
heightMeter = 0
bmi = 0


weight = int(input("Enter your weight : "))
heightFoot = int(input("Enter your height foot : "))
heightInch = int(input("Enter your height inch : "))

heightMeter = (heightFoot / 3.281) + (heightInch / 39.37)

bmi = weight / (heightMeter * heightMeter)

print(f"BMI = {bmi} ")
