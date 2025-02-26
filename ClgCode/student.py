maths=float(input("Enter the marks of maths: "))
science=float(input("Enter the marks of science: "))
english=float(input("Enter the marks of english: "))
total=maths+science+english
average=total/3
print(f"Total marks: {total}") 
print(f"Average marks: {average:.2f}")