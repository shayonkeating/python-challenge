#import tools
import os
import csv

#import csv
poll_data = os.path.join('.','poll_data.csv')

#create lists
candidates = []
unique_candidates = []
vote_count = []
vote_percent = []
total_votes = 0


#open csv
with open(poll_data, 'r') as csvfile: #open file
    csvreader = csv.reader(csvfile, delimiter=',') #read the file and make it pretty
    row = next(csvreader, None) #skip header
    
    for row in csvreader: #reads one row at a time
        total_votes = total_votes + 1 #count total votes
        candidates.append(row[2])
    for x in set(candidates): #unique candidates
        unique_candidates.append(x) 
        votes_count_can = candidates.count(x) #number of votes per candidate
        vote_count.append(votes_count_can)
        percent_total = round(((votes_count_can/total_votes)*100), 3) #percent total
        vote_percent.append(percent_total)
        winner = max(vote_count)


#Print Results
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {total_votes}")
for i in range(len(unique_candidates)):
    print(f"{unique_candidates[i]}: {vote_percent[i]}% ({vote_count[i]})")
print(f"-------------------------")
print(f"Winner: {winner}")
print(f"-------------------------")

#save text file
with open ('PyPoll Output','w') as text:
    text.write(f"Election Results\n")
    text.write(f"-------------------------\n")
    text.write(f"Total Votes: {total_votes}\n")
    for i in range(len(unique_candidates)):
        text.write(f"{unique_candidates[i]}: {vote_percent[i]}% ({vote_count[i]})\n")
    text.write(f"-------------------------\n")
    text.write(f"Winner: {winner}\n")
    text.write(f"-------------------------\n")
