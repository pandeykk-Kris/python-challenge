#import os module
import os

# import csv module
import csv

#create three list for months and profit
total_months = []
total_profit = []
monthly_profit_change = []

budget_data_csv= os.path.join("Resources", 'budget_data.csv')


#open the csv file
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(budget_data_csv)

#read/skip the header
    csv_header = next(csv_reader)

# iterate through rows in file
    for row in csv_reader:

#add total months and total profit in list
        total_months.append(row[0])
        total_profit.append(row[1])       

#iterate through profits to get monthly chnage in profit
    for i in range(1, len(total_profit)-1):

 #Take difference between two months and append to monthly profit change
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])

#determine max and min of monthly profit change
        max_increase_value= max(monthly_profit_change)
        max_decrease_value= min(monthly_profit_change)

#correlate max and min profit changes to appropriate month, +1 at the month end

        max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
        max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1

#print the analysis statements
print("Financial Analysis")
print("--------------------")
print(f"Total Months: {len(total_months)}")
print("Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit-Change)/len(monthly_profit_Change), 2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

#Output file generation
output_file=os.path.join ("Analysis", "Analysis_summary.txt")
# Write methods to print to Financial_Analysis_Summary 
file.write("Financial Analysis")
file.write("\n")
file.write("----------------------------")
file.write("\n")
file.write(f"Total Months: {len(total_months)}")
file.write("\n")
file.write(f"Total: ${sum(total_profit)}")
file.write("\n")
file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
file.write("\n")
file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
file.write("\n")
file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

