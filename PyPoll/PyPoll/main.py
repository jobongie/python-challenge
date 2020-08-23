#Summary
# This code could not print the candidates as list while pulling in 
#their corresponding values. I tried using Dicts as several other things.
# THe candidates name list somewhere was changing the names of 
#the candidates to the individual letters of o'tooley and printing his %
#my troubleshooting caused me to run out of time after changing too many things
#not being able to revert

#The print to text file code literally works in PYBANK but not In PYPOLL




#Dependencies
import os 
import csv
import collections

# Lists to store data
Percentage = 0
TopTally = 0
Votes = 0
Total = 0
Tally = []
VotePercentage = []
Candidates = []
CandidateVotes = {}

#Created csv reader file path
csvpath = os.path.join("..", "Resources", "election_data.csv")

# Open csv import data and close csv
with open(csvpath,'r') as csvfile:
    
    # CSV reader with delimiter csvreader holds content
    csvreader = csv.reader(csvfile,delimiter = ",")
    
     # Read header row first
    csv_header = next(csvreader)

    for row in csvreader:        
        
        # Total number of votes cast
        Total +=1

        # Name of candidate by row index
        CandidatesName = row[2] 

        # Create list of candidates and in vote tally
        if CandidatesName not in Candidates:
            Candidates.append(CandidatesName)            
            CandidateVotes[CandidatesName] = 0
        CandidateVotes[CandidatesName] += 1
           

# Outputs Header and Total
print("Election Results")
print("------------------------")
print(f"Total Votes: {Total}")
print("------------------------")

# Find the vote count and percentage for each candidate
for Candidate in CandidateVotes:
    Tally = CandidateVotes.get(Candidate)
    VotePercentage = (Tally/Total)*100
    
     
    # Find the winner
    if Tally == max(CandidateVotes):
        Winner = Candidates.index(Tally)
   

# Print the Candidates vote Percent and vote Count
#for x in Candidates:
    #print(f"{Candidates[x]}: {VotePercentage[x]}%, {Tally[x]}")




# Create txt path  
txtpath = os.path.join("..", "Analysis", "pypoll_analysis.txt") 

with open(txtpath, 'w') as txtfile:

    # Initialize txt.writer
    txtwriter = csv.writer(txtfile,delimiter =',')

# Outputs Header and Total
print([f"Election Results"])
print(["------------------------"])
print([f"Total Votes: {Total}"])
print(["------------------------"])

# Print the Candidates vote Percent and vote Count
#for x in Candidates:
    #print(f"{Candidates[x]}: {VotePercentage[x]}%, {Tally[x]}")

