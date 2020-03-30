#import tools
import os
import csv

#import csv
budget_csv = os.path.join('.', 'budget_data.csv')

#create variables to calculate, these are lists
month = []
rev = []
change_rev = []

total_rev = 0

with open(budget_csv, 'r') as csvfile: #opens as csvfile
    csvreader = csv.reader(csvfile, delimiter=',') #formats csv and places a comma betwen variables
    print(csvreader) #print the data
    csv_header = next(csvreader, None) #apply header after the first row using next fxn
    
#Calculate number of months
    for row in csvreader: #reads one row at a time
        month.append(row[0]) #makes it into a list
        rev.append(row[1]) #makes it into a list
        month_count = len(month) #counts number of months

#Calculate net total of "Profit/Losses"
        total_rev = total_rev + int(row[1]) #converts row from string to int and sums it

#Calculate average change in "Profit/Loss" over entire period     
for x in range(0,month_count-1):
    change_rev.append(int(rev[x+1]) - int(rev[x]))
    sum_change_rev = sum(change_rev[:]) #sum of change list through whole list
    average_change = round((sum_change_rev / (month_count-1)), 2) #doing average and round
    
#Greatest increase in profits (date and amount)
max_inc = max(change_rev)#get the max change
max_date = change_rev.index(max_inc)#index will find the location
inc_date = month[max_date+1]

#Greatest decrease in losses (date and amount) 
max_dec = min(change_rev)#get the min changee
min_date = change_rev.index(max_dec)#index will find the location
dec_date = month[min_date+1]

#Print results
print(f"Financial Analysis:")
print(f"-------------------------------")
print(f"Total Months: {month_count}")
print(f"Net Total: ${total_rev}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {inc_date} ${max_inc}")
print(f"Greatest Decrease in Profits: {dec_date} ${max_dec}")

#save text file
with open ('PyBank Financial Analysis SK','w') as text:
    text.write(f"Financial Analysis:\n")
    text.write(f"-------------------------------\n")
    text.write(f"Total Months: {month_count}\n")
    text.write(f"Net Total: ${total_rev}\n")
    text.write(f"Average Change: ${average_change}\n")
    text.write(f"Greatest Increase in Profits: {inc_date} ${max_inc}\n")
    text.write(f"Greatest Decrease in Profits: {dec_date} ${max_dec}\n")
