weight=int(input("Enter your weight"))
height=int(input("Enter your height"))
height=height/100
bmi=weight/(height*height)
print("Your BMI is {:.2f}".format(bmi))