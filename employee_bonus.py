import csv

customers = open('EmployeePay.csv', 'r') #

csv_file = csv.reader(customers) 

next(csv_file)  

for rec in csv_file:
    salary = int(rec[3])
    bonus = float(rec[4])*salary

    print(f"first_name: {rec[1]}")
    print(f"last_name: {rec[2]}")
    print(f"salary: ${salary:10,.2f}")
    print(f"bonus: ${bonus:10,.2f}")
    input()
    