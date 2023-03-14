#import modules
import os
import csv

budgetcsv = ('/Users/katieboals/Downloads/python-challenge-main/PyBank/Resources/budget_data.csv')

#create lists to store data
profit = []
monthlychanges = []
months = []

#read in the csv
with open(budgetcsv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    
    
    #loop the rows
    for row in csvreader:
      
      #append your profit and months to make sure they are adding to the list
        profit.append(int(row[1]))
                      
        months.append(row[0])

       #loop i
    for i in range(len(profit)-1):
        
        #calculation for changes in monthly profit
        monthlychanges.append(profit[i+1]-profit[i])
        
averagechange = round(sum(monthlychanges)/len(monthlychanges),2)
        
# obtain your greatest monthly profit increase and decrease
greatestincrease = max(monthlychanges)
greatestdecrease = min(monthlychanges)

# Use list and index from max and min
increasemonth = monthlychanges.index(max(monthlychanges)) + 1
decreasemonth = monthlychanges.index(min(monthlychanges)) + 1 

# Print your data

print("Financial Analysis")
print("-----------------------------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: $ {averagechange}")
print(f"Greatest Increase in Profits: {months[increasemonth]} (${(str(greatestincrease))})")
print(f"Greatest Decrease in Profits: {months[decreasemonth]} (${(str(greatestdecrease))})")



#output data as a text file
with open('/Users/katieboals/Downloads/python-challenge-main 2/PyBank/Analysis/analysis.txt', "w") as file:
    
    #Printing your data into the text file making sure to add a new line between sets of data
    file.write("Financial Analysis")
    file.write("\n")
    file.write("---------------------------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(months)}")
    file.write("\n")
    file.write(f"Total: ${sum(profit)}")
    file.write("\n")
    file.write(f"Average Change: $ {averagechange}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {months[increasemonth]} (${(str(greatestincrease))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {months[decreasemonth]} (${(str(greatestdecrease))})")
