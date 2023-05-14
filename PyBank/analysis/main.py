import os
import csv

#finds the path of the csv file
csvpath = os.path.join('..','PyBank','Resources','budget_data.csv')

#reads the csv file
with open(csvpath,'r') as file:
    excel_lines = file.read()
    print(excel_lines)
    print(type(excel_lines))

Total_months=[]
Net_total_profit_losses=[]

