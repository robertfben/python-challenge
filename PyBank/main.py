# import modules
import csv
import os

# set path to csv file
fileLoad = os.path.join("Resources", "budget_data.csv")

# file to hold the output of the PyBank analysis
outputFile = os.path.join("PyBankAnalysis.txt")

# create variables, starting empty
totalMonths = 0
totalProfit_Loss = 0
monthlyChanges = []
greatestIncrease = ["", 0] # hold month and value of greatest increase
greatestDecrease = ["", 0] # hold month and value of greatest decrease
# read csv file
with open(fileLoad) as Budget_Data:
    # create csv reader object
    csvreader = csv.reader(Budget_Data)

    # read the header row
    header = next(csvreader)
    # move to the first row
    firstRow = next(csvreader)

    # increment count of total months
    totalMonths += 1 

    # add on to total amount of revenue (index 1)
    totalProfit_Loss += float(firstRow[1])

    # establish the previous revenue
    previousProfit = float(firstRow[1]) # Proft_Loss is index 1 (2nd col)

    for row in csvreader:
        # increment count of total months
        totalMonths += 1 

        # add on to total amount of revenue (index 1)
        totalProfit_Loss += float(row[1])

        # calculate the net change of Profit/Loss
        netChange = float(row[1]) - previousProfit
        # add on to the list of monthly changes
        monthlyChanges.append(netChange)

        # update the previous Profit/Loss
        previousProfit = float(row[1])
  
# calculate the average net change per month
averageMonthlyChange = sum(monthlyChanges) / len(monthlyChanges)

# start generating the output
output = (
    f"\nFinancial Analysis\n"
    f"-------------------------------\n"
    f"Total Months: {totalMonths}\n"
    f"Total: ${int(totalProfit_Loss)}\n"    # converting to int will remove decimals and decimal point
    f"Average Change: ${averageMonthlyChange:,.2f}\n"
    )

# print output to terminal
print(output)
# print(monthlyChanges)

# export the output to the output text file
with open(outputFile, "w") as textFile:
    textFile.write(output)