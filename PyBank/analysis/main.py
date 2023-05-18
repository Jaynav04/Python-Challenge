# Your task is to create a Python script that analyzes the records to calculate each of the following values:

# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period



#import os is used for providing easy functions that allow us to interact and get operating system information
import os
#import csv module is used for analyzing tabular like data like the data in the excel like format
import csv

Total_Months=[]
Total_Profit=[]
Changes_profit=[]
#finds the path of the csv file containing the data we are analayzing
csvpath = os.path.join('Resources','budget_data.csv')

#reads the csv file
#newline="" will tell python to consider an empty string as the flag to start a new line when reading the data csv file.
with open(csvpath, newline="") as file:
#creatd variable csv_read that knows that code must read the file using the ".reader function"
#delimiter="," specifies the boundary between separate independent regions in the datas plain text.
    csv_read= csv.reader(file, delimiter=",")
#the next() function reads the iterations through datasets
# in this case it will read the forst row of text in our dataset that we saved in variable "file" 
    csv_header=next(file)
#prints the header in terminal
    print(f"{csv_header}")

    for row in csv_read:
        Total_Months.append(row[0])
        Total_Profit.append(int(row[1]))

    print(f"{len(Total_Months)}")
    print(f"${sum(Total_Profit)}")

    for x in range(len(Total_Profit)-1):
        change= Total_Profit[x+1]-Total_Profit[x]
        Changes_profit.append(change)
    
    # print(f"{Changes_profit}")

#max profit change in a month
max_profit= max(Changes_profit)

#Min profit change in a month
min_profit= min(Changes_profit)

print(f"{max_profit}")
print(f"{min_profit}")
month_max_profit=Changes_profit.index(max(Changes_profit))+1
month_min_profit=Changes_profit.index(min(Changes_profit))+1

# print(f"{month_max_profit}")
# print(f"{month_min_profit}")

    
#Print Statements

# print(f"{len(Total_Months)}")
# print(f"${sum(Total_Profit)}")
# print(f"{}")