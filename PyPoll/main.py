#import the modules
import os
import csv

# set path for csvreader
pollcsv = '/Users/katieboals/Downloads/python-challenge-main/PyPoll/Resources/election_data.csv'


#set variable for votes
totalvotes = 0 

#make empty dictionary to add all the votes for the candidates
canvotes = {}

# open up csv file
with open(pollcsv, "r") as csvfile:

    # set your csv delimter and header informatoin
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # loop through the rows
    for row in csvreader:
        #count your votes and set paremeters
        totalvotes += 1
        if row[2] not in canvotes:
            canvotes[row[2]] = 1
        else:
            canvotes[row[2]] += 1   
#set your winner through the dictionare you created        
winner = max(canvotes, key=canvotes.get)        

#print reseults
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(totalvotes))
print("-------------------------")
for candidate, votes in canvotes.items():
    print(candidate + ": " + "{:.3%}".format(votes/totalvotes) + "   (" +  str(votes) + ")")  
print("-------------------------") 
print(f"Winner: {winner}")

#now to create your text file
#really had to figure out and research how to do the names of winners being listed when printed

file = open('/Users/katieboals/Downloads/python-challenge-main 3/PyPoll/Analysis/analysis.txt', "w")
file.write("Election Results")
file.write('\n')
file.write("-------------------------")
file.write('\n')
file.write("Total Votes: " + str(totalvotes))
file.write('\n')
file.write("-------------------------")
file.write('\n')

for candidate, votes in canvotes.items():
    file.write(candidate + ": " + "{:.3%}".format(votes/totalvotes) + "   (" +  str(votes) + ")")
    file.write('\n')
file.write("-------------------------") 
file.write('\n')
file.write(f"Winner: {winner}")
file.write('\n')
