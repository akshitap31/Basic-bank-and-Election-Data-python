#importing dependencies
import os
import csv

#Setting variables
months=1
total_pl = 0
rev_change=[]
maxprofit=0
minprofit=0


#opening and reading CSV
csvpath=os.path.join('..', 'PyBank', 'Budget_data.csv')

with open(csvpath) as csvfile:
    csvreader=csv.DictReader(csvfile)
    prev_pl= int(next(csvreader)['Profit/Losses'])

    #performing operations
    for rows in csvreader:
        #total months count
        months += 1
        #Total of profit/loss
        total_pl +=int(rows['Profit/Losses'])
        # Greatest Increase month and amount
        if int(rows['Profit/Losses']) > maxprofit:
            maxprofit = int(rows['Profit/Losses'])- prev_pl
            maxmonth = rows['Date']
        # Greatest Decrease month and amount
        if int(rows['Profit/Losses']) < minprofit:
            minprofit = int(rows['Profit/Losses'])- prev_pl
            minmonth = rows['Date']
        #Average change in months
        revenue_change=int(rows['Profit/Losses']) - prev_pl
        prev_pl = int(rows['Profit/Losses'])
        rev_change += [revenue_change]


total_pl = total_pl+ prev_pl
average_change=round(sum(rev_change)/(months-1), 2)

#Print statements for terminal
print ("\nFinancial Analysis")
print ("-----------------------------------")
print ("Total Months: "+ str(months))
print("Total Profit/Loss: $" + str(total_pl))
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits: " + str(maxmonth)+" ($" + str(maxprofit)+ ")")
print("Greatest Decrease in Profits: "+ str(minmonth)+ " ($" + str(minprofit)+")")


#Exporting to a .txt
output= ("Financial Analysis\n"
        "-----------------------------------\n"
"Total Months: "+ str(months)+"\n"
"Total Profit/Loss: $" + str(total_pl)+"\n"
"Average Change: $" + str(average_change)+"\n"
"Greatest Increase in Profits: " + str(maxmonth)+" ($" + str(maxprofit)+ ")\n"
"Greatest Decrease in Profits: "+ str(minmonth)+ " ($" + str(minprofit)+")\n")

outputpath= os.path.join('..', 'PyBank', 'Budgetoutput.txt')
with open(outputpath, 'w', encoding="utf8") as csvfile:
    csvfile.write(output)