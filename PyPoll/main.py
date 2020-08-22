#Dependencies
import os 
import csv

# Lists to store data
Voter_ID = []
County = []
Candidate = []
unique_candidates = dict()

#Created csv reader file path
csvpath = os.path.join("..", "Resources", "election_data.csv")

# Open csv import data and close csv
with open(csvpath,'r') as csvfile:
    
    # CSV reader with delimiter csvreader holds content
    csvreader = csv.reader(csvfile,delimiter = ",")
    
     # Read header row first
    csv_header = next(csvreader)

    for row in csvreader:

        # Read CSV File into Lists containing its Data
        Voter_ID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])

        for x in Candidate:
            if x == "Khan":
                Khan = Khan =+ 1

            
print(f"{Khan}")

# ['Voter ID', 'County', 'Candidate']

print("Election Results")
print("------------------------")
print(f"Total Votes: ")
print("------------------------")


print("------------------------")
print(f"Winner: ")
print("------------------------")