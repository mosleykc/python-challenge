# Unit 3 Assignment - Py Me Up Charlie
# The purpose of main.py is to analyze financial records based on the dataset in budget_data.csv.
# Analysis to include the calculation of the folowing:
# 1. Total Number of months included in the dataset 
# 2. Net total amount of "profit/loss" over the entire period
# 3. Average of changes in "Profit/Loss" over the entire period
# 4. Greatest increase in profits (date and amt) over entire period
# 5. Greatest decrease in losses (date and amt) over entire period
# 6. Print the analysis to the terminal and export a text file with results

import os 
import csv

#Variables/Empty Lists
total_months = [] # create empty list to hold total months data
net_total = 0
avg_chg = 0
revenue = [] # create empty list to hold revenue data
date = []

# set path for input data file
pybank_input_path=os.path.join('Resources','budget_data.csv')

# set path for output file named pybank_analysis.csv
pybank_analysis_path=os.path.join('Analysis','pybank_analysis.csv')

# open data input file
with open(pybank_input_path,newline="") as datafile:
    read_data=csv.reader(datafile,delimiter=",")
    next(read_data, None)
    
     # Create loop to count number of rows to use as Total Months starting at 0
    total_months=0
        
    date, revenue = ([] for i in range(2))

    # create loop to read through read_data
    # calculate total months by adding number of rows
    # calculate Revenue by adding values in each row, index 1
    # use append method to associate date list with the first column and revenue with second column
    for row in read_data: 
        total_months+=1 
        net_total += int(row[1]) 
        date.append(row[0])
        revenue.append(row[1])
        

 #  loop through total_months subtract current from next month 
 # #then divide by total_months - 1 to get average change  
net_change = []
next = 0
current = 0

for next in range(0, total_months):
    if next == 0:
        net_change.append(0)
    else:
        net_change.append(int(revenue[next])-int(revenue[current]))
        current += 1

sum_monthly_chg = 0
m = 0
for m in range(total_months):
    sum_monthly_chg = sum_monthly_chg + int(net_change[m])
avg_chg= round(int(sum_monthly_chg)/int(total_months - 1),2)

# Create function to calculate greatest increase in profits (date & amt)
# use the max method to look at output in net_change list to find the highest number
# find index for greatest increase value to find associated date
# assign the date associated with the greatest increase value by using the index in greatest_incr_index
# create variable to hold date and amount for output
greatest_increase = max(net_change)
greatest_incr_index = net_change.index(greatest_increase)
greatest_increase_date = date[greatest_incr_index]
greatest_increase_output = str(greatest_increase_date) + " " + "($" + str(greatest_increase) + ")"

# Create function to calculate the greatest decrease in losses (date & amt)
# use the min method to look at output in net_change list to find the lowest number
# find index for greatest decrease value to find associated date
# assing the date associated with greatest decrease value
# create variable to hold date and amount for output
greatest_decrease =min(net_change)
greatest_decr_index = net_change.index(greatest_decrease)
greatest_decrease_date = date[greatest_decr_index] 
greatest_decrease_output = str(greatest_decrease_date) + " " + "($" + str(greatest_decrease) + ")"
 
# setup output format
Pybank_Analysis_Output = (
    f"Financial Analysis\n"
    f"--------------------\n"
    f"Total Number of Months: {total_months}\n"
    f"Total Revenue: ${net_total}\n"
    f"Average Change: ${avg_chg}\n"
    f"Greatest Increase in Profits: {greatest_increase_output}\n"
    f"Greatest Decrease in Profits: {greatest_decrease_output}\n") 

# Print analysis to terminal
print(Pybank_Analysis_Output)

# Print analysis to file pybank_analysis.csv
# open Pybank_Analysis_Output.csv and append results
with open(pybank_analysis_path,'a') as csvfile:
   csvfile.write(Pybank_Analysis_Output)

# End of Pybank homework assignment