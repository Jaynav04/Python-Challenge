# create a Python script that analyzes the votes and calculates each of the following values:

# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote

import csv
import os

#Setting variables
candidates={}
total_votes=0

#Getting csv file path
csv_data= os.path.join('PyPoll','Resources','election_data.csv')

#making python read the csv
with open(csv_data,newline="") as file:
    read_csv= csv.reader(file,delimiter=",")

#Skipping the first row 
    header_csv=next(file)

#Iterating through each row of data 
    for row in read_csv:
        #adds 1 to our count of total_votes everytime the for loop finds a vote in the dataset
        total_votes += 1
        #assigns variable and extracts candidates name from corresponding column
        name_candidate=row[2]

        #The following keeps track of the number of votes recieved by each candidate
        #adds the candidates name to dictionary and updates vote count
        if name_candidate in candidates:
            #If candidate is present in dictionary this line adds the value associated with that candidate by +1 vote 
            candidates[name_candidate]+=1
        #the following code adds a new candidate to the dictionary and sets value to 1 which represents their first vote
        else:
            candidates[name_candidate]=1

#Calculates percentage of votes for each candidate
percentage={}

#the candidates dictionary stores candidate names as keys and the votes as values
#By using .items() we create a sequence of tuples where each contains a key value pair inside the dictionary
#This loop assigns each key value pair to variables candidate and votes allowing access to name and vote count in each iteration
for candidate, votes in candidates.items():

    #calculation for percent
    percent=(votes/total_votes) *100

    #store each candidates percentage in the percentage dictionary and 
    #used the round function to round to two decimal places
    percentage[candidate]=round(percent,2)

#Using the max function we ask it to calculate the max number of votes in the candidates dictionary 
#the .get makes python retrieve the vote count associated with the candidte with the most votes 
winner=max(candidates,key=candidates.get)


#Print Statements
print(f"Total votes: {total_votes}")

#here we change the variable percent to equal the percentage of each candidate in the candidates dictionary 
for candidate, votes in candidates.items():
    percent=percentage[candidate]
    print(f"{candidate}:  {percent}% ({votes})")
   
print(f"Winner: {winner}")

#output to Summary .txt file
Summary= os.path.join('PyPoll','Election_summary.txt')
with open(Summary,'w')as file:
    
    file.write( "Election Summary \n")
    file.write("---------------------------- \n")
    file.write(f"Total votes: {total_votes}\n")
    file.write(f'---------------------------\n')
    for candidate, votes in candidates.items():
     percent=percentage[candidate]
     file.write(f"{candidate}:  {percent}% ({votes})\n")
    file.write(f'---------------------------\n')
    file.write(f"Winner: {winner}\n")
    file.write(f'---------------------------\n')
