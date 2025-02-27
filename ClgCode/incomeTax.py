# Function to calculate year-end bonus
def calculate_bonus(salary, holidays_worked, night_shifts, complaints):
    yearly_bonus = 0.1 * salary * 12  # 10% of salary per month for 12 months
    holiday_bonus = holidays_worked * 200  # ₹200 per holiday worked
    night_shift_bonus = night_shifts * 100  # ₹100 per night shift
    complaint_penalty = complaints * 100  # ₹100 deduction per complaint
    
    total_bonus = yearly_bonus + holiday_bonus + night_shift_bonus - complaint_penalty
    return total_bonus

# Taking user input (Ensuring proper data types)
name = input("Enter Employee Name: ")
salary = float(input("Enter Monthly Salary (₹): "))  # Convert to float
holidays_worked = int(input("Enter Number of Holidays Worked: "))  # Convert to int
night_shifts = int(input("Enter Number of Night Shifts: "))  # Convert to int
complaints = int(input("Enter Number of Complaints: "))  # Convert to int

# Calculate and display bonus
total_salary = calculate_bonus(salary, holidays_worked, night_shifts, complaints)
print(f"Bonus:",total_salary-salary)
print(f"Total Salary after 1 year for {name}: ₹{total_salary:.2f}")
