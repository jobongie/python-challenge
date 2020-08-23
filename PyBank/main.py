#Dependencies
import os 
import csv

ProfitLoss = []
Date = []
AverageChange = []
NextValue=[]
Change=[]

#Create csv reader file path
csvpath = os.path.join("..", "Resources", "budget_data.csv")

# Open csv import data and close csv
with open(csvpath,'r') as csvfile:
    
    # CSV reader with delimiter csvreader holds content
    csvreader = csv.reader(csvfile, delimiter = ",")
   
    # Read header row first
    csv_header = next(csvreader)   
                
    # Go through each row in the CSV     
    for row in csvreader:     
           
        # Read values into lists
        ProfitLoss.append(int(row[1]))
        Date.append(row[0])    
         
        #Tried to use indexing to find the average change between months
        # previously had the Sum / Months and was able to print
        # Code is wrong but if I could find a way to properly code the average 
        # Change it would print properly, but alas I have failed using the indices
        # to to logic my way into a list of size n-1
             
# for x in ProfitLoss:
#     If ProfitLoss.index(x) == 0: 
#         break
#     elif ProfitLoss.index(x) == len(ProfitLoss):
#         break
#     else:   
#         AverageChange = (ProfitLoss.index(x+1)-ProfitLoss.index(x))


# Number of months
months = len(ProfitLoss) 

# Total Profit/Loss    
total = sum(ProfitLoss)

# Find date and value of max profit
max = max(ProfitLoss)
max_index = ProfitLoss.index(max)
max_date = Date[max_index]
    
# Find Date and Value of max loss
min = min(ProfitLoss)
min_index = ProfitLoss.index(min)
min_date = Date[min_index]   
    
# Print to Terminal
print("Financial Analysis")
print("-------------------------------")
print(f"Total Months: {months}")
#print(f"Average Change: ${round(average,2)}")
print(f"Greatest Increase in Profits: {max_date}, (${max})")
print(f"Greatest Decrease in Profits: {min_date}, (${min})")
        
# Create txt path  
txtpath = os.path.join("..", "Analysis", "pybank_analysis.txt") 

with open(txtpath, 'w') as txtfile:

    # Initialize txt.writer
    txtwriter = csv.writer(txtfile,delimiter =',')

    txtwriter.writerow(["Financial Analysis"])
    txtwriter.writerow(["-------------------------------------------------"])
    txtwriter.writerow([f"Total Months: {months}"])
    #txtwriter.writerow([f"Average Change: ${round(average,2)}"])
    txtwriter.writerow([f"Greatest Increase in Profits: {max_date}, (${max})"])
    txtwriter.writerow([f"Greatest Decrease in Profits: {min_date}, (${min})"])
              

