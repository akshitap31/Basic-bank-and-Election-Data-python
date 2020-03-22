#Import Dependencies
import os
import csv

#Define Variables
total_count=0
khan_votes=0
correy_votes=0
li_votes=0
tooley_votes=0

#Open and read CSV
csvpath= os.path.join('..', 'PyPoll', 'election_data.csv')
with open(csvpath, encoding="utf8") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')
    #Skip Header
    header= next(csvreader)
    #Perform Operations
    for row in csvreader:
        #Total Votes
        total_count += 1
        #Candidate Vote Count
        if row[2] == "Khan":
            khan_votes += 1
        elif row[2]== "Correy":
            correy_votes += 1
        elif row[2] == "Li":
            li_votes += 1
        else:
            tooley_votes += 1
#Percentage of total
average_khan= round(khan_votes/total_count*100,3)
average_correy= round(correy_votes/total_count*100,3)
average_li= round(li_votes/total_count*100,3)
average_tooley= round(tooley_votes/total_count*100,3)

#Winner
if khan_votes>correy_votes and khan_votes>li_votes and khan_votes>tooley_votes:
    winner="Khan"
elif correy_votes>khan_votes and correy_votes>li_votes and correy_votes>tooley_votes:
    winner = "Correy"
elif li_votes>khan_votes and li_votes>correy_votes and li_votes>tooley_votes:
    winner = "Li"
else:
    winner = "O'Tooley"


#Print Statements
print("Election Results")
print("------------------------")
print("Total Votes: "+str(total_count))
print("------------------------")
print("Khan: "+ str(average_khan)+"%  (" + str(khan_votes)+")")
print("Correy: "+ str(average_correy)+"%  (" + str(correy_votes)+")")
print("Li: "+ str(average_li)+"%  (" + str(li_votes)+")")
print("O'Tooley: "+ str(average_tooley)+"%  (" + str(tooley_votes)+")")
print("------------------------")
print("Winner: "+ winner)
print("------------------------")

#Export File
outputpath= os.path.join('..', 'PyPoll', 'election_results.txt')
output=( "Election Results\n"
    "------------------------\n"
    "Total Votes: " + str(total_count)+"\n"
    "------------------------\n"
    "Khan: " + str(average_khan) + "%  (" + str(khan_votes) + ")\n"
    "Correy: " + str(average_correy) + "%  (" + str(correy_votes) + ")\n"
    "Li: " + str(average_li) + "%  (" + str(li_votes) + ")\n"
    "O'Tooley: " + str(average_tooley) + "%  (" + str(tooley_votes) + ")\n"
    "------------------------\n"
    "Winner: " + winner + "\n"
    "------------------------\n")
with open(outputpath, 'w', encoding="utf8") as csvfile:
    csvfile.write(output)