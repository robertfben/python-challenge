# import modules
import csv
import os

# set path to csv file
fileLoad = os.path.join("Resources", "budget_data.csv")

# file to hold the output of the PyBank analysis
outputFile = os.path.join("analysis", "PyBankAnalysis.txt")

# create variables, starting empty
totalMonths = 0
totalProfit_Loss = 0
monthlyChanges = []
months = [] 

# read csv file
with open(fileLoad) as Budget_Data:
    # create csv reader object
    csvreader = csv.reader(Budget_Data)

    # read the header row
    header = next(csvreader)
    # move to the first row
    firstRow = next(csvreader)

    # increment count of first month starting at 1st non-header row
    totalMonths += 1 

    # add on to total amount of Profit/Loss starting at 1st non-header row (index 1, 2nd col)
    totalProfit_Loss += float(firstRow[1])

    # establish the previous revenue
    previousProfit_Loss = float(firstRow[1]) # Profit_Loss is index 1 (2nd col)

    for row in csvreader:
        # increment count of total months
        totalMonths += 1 

        # add on to total amount of revenue (index 1)
        totalProfit_Loss += float(row[1])

        # calculate the net change of Profit/Loss
        netChange = float(row[1]) - previousProfit_Loss
        # add on to the list of monthly changes
        monthlyChanges.append(netChange)

        # add first month that a change occurred
        months.append(row[0]) # month is index 0

        # update the previous Profit/Loss
        previousProfit_Loss = float(row[1])
  
# calculate the average net change per month
averageMonthlyChange = sum(monthlyChanges) / len(monthlyChanges)

greatestIncrease = [months[0], monthlyChanges[0]] # hold month and value of greatest increase
greatestDecrease = [months[0], monthlyChanges[0]] # hold month and value of greatest decrease

# create loop to calculate index of the greatest and least monthly change
for m in range(len(monthlyChanges)):
    # calculate greatest increase and decrease
    if(monthlyChanges[m] > greatestIncrease[1]):
        # if value is greater than the greatest increase, that value becomes new greatest increase
        greatestIncrease[1] = monthlyChanges[m]
        # update month
        greatestIncrease[0] = months[m]

    if(monthlyChanges[m] < greatestDecrease[1]):
        # if value is less than the greatest increase, that value becomes new greatest decrease
        greatestDecrease[1] = monthlyChanges[m]
        # update month
        greatestDecrease[0] = months[m]

# start generating the output
output = (
    f"\nFinancial Analysis\n"
    f"-------------------------------\n"
    f"Total Months: {totalMonths}\n"
    f"Total: ${int(totalProfit_Loss)}\n"    # converting to int to remove decimals and decimal point in output
    f"Average Change: ${averageMonthlyChange:,.2f}\n"
    f"Greatest Increase in Profits: {greatestIncrease[0]} (${int(greatestIncrease[1])})\n"
    f"Greatest Decrease in Profits: {greatestDecrease[0]} (${int(greatestDecrease[1])})"
    )

# print output to terminal
print(output)
# print(monthlyChanges)

# export the output to the output text file
with open(outputFile, "w") as textFile:
    textFile.write(output)