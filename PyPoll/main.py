# imports 
import os
import csv


# declare global variables 


# import the data
file_to_read = os.path.join("Resources\\", "election_data.csv")
file_to_write =  os.path.join("output\\", "election_results.txt")


with open(file_to_read) as election_data:
    csv_reader = csv.reader(election_data)

    # read the first row and store it in the variable 'header'
    header = next(csv_reader)
    #print(header)
    #first = next(csv_reader)
    #print(first[1])

    # for loop