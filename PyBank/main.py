# Modules
import os
import csv

# set path for file
budgetcsv = os.path.join("raw_data", "budget_data_1.csv")

#open csv
with open(budgetcsv,encoding='utf-8') as csvfile1:
    csvreader1 = csv.reader(csvfile1, delimiter=",")

# Variables
    totalmonth = 0
# Loop through months
    for row in csvreader1: 
        totalmonth = totalmonth +1        

# Print Row (Month)
        
        print('Total Months: ' + str(totalmonth))



