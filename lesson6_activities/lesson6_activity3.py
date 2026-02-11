height=float(input("enter your height in cm"))
weight=float(input("enter your weight in kg"))
bmi=weight/(height/100)**2
print("bmi is", bmi)
if bmi <=18.4:
    print("you are under weight")
elif bmi<=24.9:
    print("you are healthy")
elif bmi<= 34.9:
    print("you are over weight")
else:
    print("you are severely over weight")