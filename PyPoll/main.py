# Create a Python script that analyzes the votes and calculates each of the following:
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

import os 
import csv

# Define variables & dictionary for capturing data needed for output
total_votes = 0
election_data = {} # Using dictionary to store data - one to many relationship
candidates = [] # create empty list to hold candidate names
percent_votes = []  #create empty list to hold percentage of votes each candidate won
votes = [] #create empty list to hold vote numbers
winner = [] 
max_count = 0
winner_list = []

# set path for input data file election_data.csv
pypoll_input_path=os.path.join('Resources','election_data.csv')

# set path for output file named pypoll_analysis.csv
pypoll_analysis_path=os.path.join('Analysis','pypoll_analysis.csv')

# open data input file and store header data (not to be used in this assignment)
with open(pypoll_input_path,newline="") as datafile:
    read_data=csv.reader(datafile,delimiter=",")
    next(read_data, None)

# Create loop to count number of rows 
    # Dictionary to capture data and assign to candidate name as key and other election data as values
    # 3rd column is the dictionary key and begin condition to tally votes by candidate
    for row in read_data:
       # Total number of votes 
        total_votes+=1  
        if row[2] in election_data.keys(): 
            election_data[row[2]] = election_data[row[2]] + 1 
        else:
            election_data[row[2]] = 1
    
    # create a dictionary loop that will append the returned candidate names & votes into strings
    # utlize the .items method to create tuples for candidate names (key) votes(value)
    for key, value in election_data.items():
        candidates.append(key)
        votes.append(value)
    

    # calculate the percentage of votes
    # set votes to 0
    winning_votes = votes[0]
        
    for vote_cntr in range(len(candidates)):
        percentage = votes[vote_cntr]/total_votes*100
        percent_votes.append(percentage)
        if votes[vote_cntr] > winning_votes:
                winning_votes = votes[vote_cntr]
                max_count = vote_cntr
    winner = candidates[max_count]

# setup output format
pypoll_Analysis_Output = (
    f"Election Results\n"
    f"--------------------\n"
    f"Total Votes: {total_votes}\n"
    f"--------------------\n"
    f"{candidates}\n" 
    f"{percent_votes}\n"
    f"{votes}\n"
    f"--------------------\n"
    f"Winner: {winner} \n" 
    f"--------------------\n" 
    
)

# print results to terminal
print(pypoll_Analysis_Output)

# Print analysis to file  pypoll_analysis.csv
# open Pybank_Analysis_Output.csv and append results
with open(pypoll_analysis_path,'a') as csvfile:
   csvfile.write(pypoll_Analysis_Output)






# End Pypoll homework assignment