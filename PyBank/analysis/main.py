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

#Creating empty lists to iterate through specified variables
Total_Months=[]
Total_Profit=[]
Changes_profit=[]
#finds the path of the csv file containing the data we are analayzing
csvpath = os.path.join('PyBank','Resources','budget_data.csv')

#reads the csv file
#newline="" will tell python to consider an empty string as the flag to start a new line when reading the data csv file.
with open(csvpath, newline="") as file:

#created variable csv_read that will store the contents of the csv file 
#delimiter="," specifies the boundary between separate independent regions in the datas plain text.
    csv_read= csv.reader(file, delimiter=",")

#the next() function reads the iterations through datasets
# in this case it will read the first row of text in our dataset that we saved in variable "file" 
    csv_header=next(file)
#prints the header in terminal
    # print(f"{csv_header}")

#iterates through the rows in the dataset using the variable csv_read 
    for row in csv_read:

        #adds the total months and total profits to its corresponding lists
        Total_Months.append(row[0])
        Total_Profit.append(int(row[1]))

    # print(f"{len(Total_Months)}")
    # print(f"${sum(Total_Profit)}")

#iterating through profits list in order to obtain monthly change in profits
    for x in range(len(Total_Profit)-1):

        #Taking the difference between two months and adding that difference to the changes in profit list
        change= Total_Profit[x+1]-Total_Profit[x]
        Changes_profit.append(change)
    
    # print(f"{Changes_profit}")

#saving max profit change in a single month to variable
max_profit= max(Changes_profit)

#saving min profit change in a single month to variable
min_profit= min(Changes_profit)

# print(f"{max_profit}")
# print(f"{min_profit}")
#Correlate min and max profits to its corresponding months 
month_max_profit=Changes_profit.index(max(Changes_profit))+1
month_min_profit=Changes_profit.index(min(Changes_profit))+1

# print(f"{month_max_profit}")
# print(f"{month_min_profit}")

    
#Print Statements

print(f"Total Months: {len(Total_Months)}")
print(f"Total Revenue : ${sum(Total_Profit)}")
print(f"Average change in Revenue: ${round(sum(Changes_profit)/len(Changes_profit),2)}")
print(f"Greatest Increase in Profits: {Total_Months[month_max_profit]} (${(str(max_profit))})")
print(f"Greatest Decrease in Profits: {Total_Months[month_min_profit]} (${(str(min_profit))})")

#the following will follow a path to write my summary in a .txt file

Summary_file=os.path.join('PyBank','Financial_summary.txt')

with open(Summary_file,'w') as file:
    file.write("Financial Summary\n")
    file.write("-----------------------\n")
    file.write(f"Total Months: {len(Total_Months)}\n")
    file.write(f"Total Revenue : ${sum(Total_Profit)}\n")
    file.write(f"Average change in Revenue: ${round(sum(Changes_profit)/len(Changes_profit),2)}\n")
    file.write(f"Greatest Increase in Profits: {Total_Months[month_max_profit]} (${(str(max_profit))})\n")
    file.write(f"Greatest Decrease in Profits: {Total_Months[month_min_profit]} (${(str(min_profit))})\n")