import os
import csv


# set path for file
pollcsv = os.path.join("raw_data", "election_data_1.csv")

voter_id = []
candidate = []
winner = []


# Open the CSV
with open(pollcsv,newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print('Election Results:')
    print('---------------------------------------')

# Count Total number of Votes
    for row in csvreader:
        rowcount = len(list(csvreader))

        print('Total Votes: ' + str(rowcount))
        print('-------------------------------------')





    

        









    