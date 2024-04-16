amount = 0
rate = 0
time = 0
simpleInterest = 0

amount = int(input("Enter amount : "))
rate = int(input("Enter rate : "))
time = int(input("Enter duration : "))

simpleInterest = (amount * rate * time) / 100

print(f"Simple interest = {simpleInterest}%")