def calculate_salary(work_hours, hourly_rate):
    if work_hours <= 40:
        return work_hours * hourly_rate
    else:
        overtime = work_hours - 40
        return 40 * hourly_rate + overtime * (1.4 * hourly_rate)

try:
    hours = float(input('Enter your hours: '))
    rate = float(input('Enter your hourly rate: '))

    gross_pay = calculate_salary(hours, rate)

    print('Salary:', gross_pay)

except ValueError:
    print('Error, please enter a number')
