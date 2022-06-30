# import modules
import csv
import os

# set path to csv file
fileLoad = os.path.join("Resources", "election_data.csv")

# file to hold the output of the PyPoll analysis
outputFile = os.path.join("analysis", "PyPollAnalysis.txt")

# create variables, starting empty
totalVotes = 0     # will hold total # of votes
candidateList = [] # list to hold candidate names
candidateVotes = {} # dictionary to hold the votes each candidate receives
winningCount = 0 # will hold the winning count
winningCandidate = ""

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

    # rows will be lists
        # index 2 is the name of candidate the vote is for

    for row in csvreader:
        # increment count of total months
        totalVotes += 1

        # check to see if candidate is in list of candidates
        if row[2] not in candidateList:
            # if candidate is not in the list, add it to the list of candidates
            candidateList.append(row[2])

            # add the value to the dictionary as well
            # start the count at 1 for the votes
            candidateVotes[row[2]] = 1
        
        else:
            # if candidate is already in list of candidates
            # add a vote to candidate vote count
            candidateVotes[row[2]] += 1

    # create empty string to initialize final vote output    
    voteOutput = ""

    for candidate in candidateVotes:
        # get vote count and percentage of the vote from vote dictionary
        votes = candidateVotes.get(candidate)
        votePct = (float(votes) / float(totalVotes)) * 100.00

        # generate a formatted string for each candidate with their % of votes
        voteOutput += f"{candidate}: {votePct:,.3f}% ({votes:,})\n"

        # compare the votes to the winning count
        if votes > winningCount:
            # update the votes to be the new winning count 
            winningCount = votes
            # update the winning candidate
            winningCandidate = candidate

    winningCandidateOutput = f"Winner: {winningCandidate}\n"


    # start generating the output
    output = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {totalVotes:,}\n"
        f"-------------------------\n"
        f"{voteOutput}"
        f"-------------------------\n"
        f"{winningCandidateOutput}"
        f"-------------------------\n"
    )

# print output to terminal
print(output)

# export the output to the output text file
with open(outputFile, "w") as textFile:
    # write output to to text file
    textFile.write(output)