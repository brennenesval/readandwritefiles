import csv

customers = open('customers.csv', 'r')

csv_file = csv.reader(customers) #add delimiter= if the separation in not ",

next(csv_file)  #skip a row




outfile = open("customer_country.csv", 'w')

outfile.write(f"Full Name, Country \n")

counter = 0

for rec in csv_file:
    f_name = rec[1]
    l_name = rec[2]
    country = rec[4]

    outfile.write(f"{f_name} {l_name}, {country}\n")
    counter += 1

outfile.close()

print(f"total number of customers: {counter}")
