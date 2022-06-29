# import modules
import csv
import os

# set path to csv file
fileLoad = os.path.join("Resources", "election_data.csv")

# file to hold the output of the PyPoll analysis
outputFile = os.path.join("analysis", "PyPollAnalysis.txt")

# create variables, starting empty
totalVotes = 0
candidateList = []

# read CSV file
with open(fileLoad) as Election_Data:
    # create csv reader object
    csvreader = csv.reader(Election_Data)

    # read header row
    header = next(csvreader)
    # move to first row
    firstRow = next(csvreader)

    # increment count of first vote starting at 1st non-header row 
    totalVotes += 1

    for row in csvreader:
        # increment count of total months
        totalVotes += 1

        # add on to the list of candidates
        candidates = row[2]
        candidateList.append(candidates)
    
    # using set() to remove all duplicate candidate names and then restore back to a list
    candidateList = list(set(candidateList))


    # start generating the output
    output = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {totalVotes}\n"
        f"-------------------------\n"
        f"{candidateList[0].title()}: \n"
        f"{candidateList[1].title()}: \n"
        f"{candidateList[2].title()}: \n"

    )


# print output to terminal
print(output)

# export the output to the output text file
with open(outputFile, "w") as textFile:
    textFile.write(output)