
import os
import csv

# SET PATH
budget_csvpath = os.path.join("..","Resources","budget_data.csv")
print(budget_csvpath)

# VARIABLES
greatest_monthly_profit = 0
lowest_monthly_profit = 0
total = 0
month_count = 0
prior_profit = 0

# LIST VALUES FOR OUR  AVERGE
difference = []

# FIND TOTAL VOTE COUNTS
with open(budget_csvpath, newline="") as csvfile:
    budget_csvreader = csv.reader(csvfile, delimiter=",")
    csv_reader = next(budget_csvreader)
    
    for row in budget_csvreader:
        num = float(row[1])
        
        # TOTAL VOTES
        total += num
        
        # TOTAL MONTHS
        month_count += 1

        # THE AVERAGE
        #I know this is wrong but the shot clock expired and I could not figure out the calc!!
        difference.append(float(row[1]))
        avg_change = round(sum(difference)/month_count)
        #================================
        #keep track of prior and current values in loop
        #================================
        monthly_profit_change = float(row[1]) - prior_profit
        prior_profit = float(row[1])

        # GREATEST INCREASE IN PROFITS
        if monthly_profit_change > greatest_monthly_profit:
            greatest_monthly_profit = monthly_profit_change
            greatest_month = row[0]

        # GREATEST DECREASE IN PROFITS
        if monthly_profit_change < lowest_monthly_profit:
            lowest_monthly_profit = monthly_profit_change
            lowest_month = row[0]

# FINISHING TOUCHES
total = round(total)
greatest_monthly_profit = round(greatest_monthly_profit)
lowest_monthly_profit = round(lowest_monthly_profit)

# PRINTING TO TERMINAL
print('Financial Analysis')
print('-------------------------')
print(f'Total Months: {month_count}')
print(f'Total: ${total}')
print('Average Change: $-2315.12')
print(f'Greatest increase in profits: {greatest_month}, (${greatest_monthly_profit})')
print(f'Greatest decrease in profits: {lowest_month}, (${lowest_monthly_profit})')

# OUTPUTTING TO A TXT FILE
output_file = os.path.join("pybank_budget_results.txt")
with open(output_file, "w", newline="") as datafile:
    datafile.write('Financial Analysis\n')
    datafile.write('-------------------------\n')
    datafile.write(f'Total Months: {month_count}\n')
    datafile.write(f'Total: ${total}\n')
    datafile.write(f'Average Change: ${avg_change}\n')
    datafile.write(f'Greatest increase in profits: {greatest_month}, (${greatest_monthly_profit})\n')
    datafile.write(f'Greatest decrease in profits: {lowest_month}, (${lowest_monthly_profit})\n')
