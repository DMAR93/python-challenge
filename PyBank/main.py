# import  
import csv
import os

# Path to the file
file_path = os.path.join("Resources", "budget_data.csv")

# Initialize varibale
total_months = 0
net_total = 0
previous_profit = None
changes = []
dates = []

# read the file

with open(file_path, mode="r") as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)

# the for loop 
    for row in csv_reader:
        date = row[0]
        profit = int(row[1])

        total_months += 1
        net_total += profit

        if previous_profit is not None:
            change = profit - previous_profit
            changes.append(change)
            dates.append(date)

        previous_profit = profit

# calculate the average
average_change = sum(changes)/ len(changes)

# find the greates increase in profits (date and amount)
greatest_increase = max(changes) if changes else 0
greates_increase_date = dates[changes.index(greatest_increase)]

# find the greatest decrease in profits (date and amount)
greatest_decrease = min(changes) if changes else 0
greatest_decrease_date = dates[changes.index(greatest_decrease)]

#results
print("Financial Analysis")
print("-------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest increase in Profits: {greates_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
