principle=float(input("Enter the principle amount: "))
rate=float(input("Enter the rate of interest: "))
time=float(input("Enter the time: "))
si=(principle*rate*time)/100
print(f"The simple interest is: {si:.2f}")