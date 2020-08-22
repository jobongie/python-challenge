#Dependencies
import os 
import csv

maxProfitLoss = []
Date = []

#Create csv reader file path
csvpath = os.path.join("..", "Resources", "budget_data.csv")

# Open csv import data and close csv
with open(csvpath,'r') as csvfile:
    
    # CSV reader with delimiter csvreader holds content
    csvreader = csv.reader(csvfile,delimiter = ",")
   
    # Read header row first
    csv_header = next(csvreader)   
                
    # Go through each row in the CSV  
    
    for row in csvreader:     
           
        # Read values into lists
        maxProfitLoss.append(int(row[1]))
        Date.append(row[0])
    
    # Number of months
    months = len(maxProfitLoss) 

    # Total Profit/Loss    
    total = sum(maxProfitLoss)

    # Average of Profit/Loss per month
    average = total / months

print("Financial Analysis")
print("-------------------------------")
print(f"Total Months: {months}")
print(f"Average Change: ${round(average,2)}")
print(f"Greatest Increase in Profits: ", max(maxProfitLoss))
print(f"Greatest Decrease in Profits: ", min(maxProfitLoss))

        
# use if statement to pull out the date for increase and decrease using index (file wrestling functions)
