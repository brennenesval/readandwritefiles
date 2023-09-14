import csv

sales = open('sales.csv', 'r')

csv_file = csv.reader(sales) 

next(csv_file)  

outfile = open("salesreport.csv", 'w')
outfile.write("Customer ID, Total \n")

cust_id = '250' #fine to initialize hard coded variables
total = 0

for rec in csv_file:
    sub_total = float(rec[3])
    tax_amt = float(rec[4])
    freight = float(rec[5])
    



    if cust_id == rec[0]:
        total += sub_total + tax_amt + freight

    else:
        outfile.write(f"{cust_id}, {total:10,.2f}\n")
        total = sub_total + tax_amt + freight
        cust_id = rec[0]


outfile.write(f"{cust_id}, {total:10,.2f}\n")

outfile.close()




