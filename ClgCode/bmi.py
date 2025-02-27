weight=int(input("Enter your weight in kg:"))
height=int(input("Enter your height in cm:"))
height=height/100
bmi=weight/(height*height)
print("Your BMI is {:.2f}".format(bmi))
