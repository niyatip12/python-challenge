# Import the dependecies
import os
import csv

#setting path for csv file 
py_bank_csv = os.path.join("Resources", "budget_data.csv")

# Lists to store the data
profit = []
monthly_changes = []
date = []

# declare variables
count = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0

#Open and read the csv file

with open(py_bank_csv, newline="",encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        # use the function count to count the number of monthsin the data set
        count = count + 1
        #append the date as it will be needed to collect greatest increase and decrease 
        date.append(row[0])

        #append the profit information & calculate total profit
        profit.append(row[1])
        total_profit = total_profit + int(row[1])

        #calculate the avg change in profits
        final_profit = int(row[1])
        monthly_change_profits = final_profit - initial_profit

        #Store these changes in a list
        monthly_changes.append(monthly_change_profits)
        total_change_profits = total_change_profits - monthly_change_profits
        initial_profit = final_profit

        #Calculating the avg change 
        average_change_profits = (total_change_profits/count)

        #Find the maximum and minimum change in profits and associated dates
        greatest_increase_profits = max(monthly_changes)
        greatest_decrease_profits = min(monthly_changes)

        increase_date = date[monthly_changes.index(greatest_increase_profits)]
        decrease_date = date[monthly_changes.index(greatest_decrease_profits)]

print("----------------------------------------------------------")
print("Financial Analysis")
print("----------------------------------------------------------")
print("Total Months: " + str(count))
print("Total Profits: " + "$" + str(total_profit))
print("Average Change: " + "$" + str(int(average_change_profits)))
print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
print("----------------------------------------------------------")

# Print file to text file  : financila_analysis.txt
with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_change_profits)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
    text.write("----------------------------------------------------------\n")

