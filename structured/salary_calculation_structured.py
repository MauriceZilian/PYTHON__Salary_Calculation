def calculate_salary(work_hours, hourly_wage):
    
    # Calculates the salary based on working hours and hourly wage.
    # Overtime (over 40 hours) is paid with a 40% bonus.
    
    if work_hours <= 40:
        return work_hours * hourly_wage
    else:
        overtime = work_hours - 40
        return 40 * hourly_wage + overtime * (1.4 * hourly_wage)

def main():
    try:
        hours = float(input('Enter your working hours: '))
        wage = float(input('Enter your hourly wage: '))
        
        gross_pay = calculate_salary(hours, wage)
        print('Salary:', round(gross_pay, 2))
    except ValueError:
        print('Error, please enter a valid number')

if __name__ == "__main__":
    main()
