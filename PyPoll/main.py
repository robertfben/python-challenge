# import modules
import csv
import os

# set path to csv file
fileLoad = os.path.join("Resources", "election_data.csv")

# file to hold the output of the PyPoll analysis
outputFile = os.path.join("analysis", "PyPollAnalysis.txt")

# create variables, starting empty
totalVotes = 0
Stockham_Votes = 0
Degette_Votes = 0 
Doane_Votes = 0
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

    # increment count of first vote for Stockham at 1st non-header row
    Stockham_Votes += 1

    # increment count of first Doane vote
    Degette_Votes = 0

    for row in csvreader:
        # increment count of total months
        totalVotes += 1

        # add on to the list of candidates
        candidates = row[2]
        candidateList.append(candidates)

        # running count of each of the three candidate's votes
        if row[2] == "Charles Casper Stockham":
            Stockham_Votes += 1
        elif row[2] == "Diana DeGette":
            Degette_Votes += 1
        elif row[2] == "Raymon Anthony Doane":
            Doane_Votes += 1
        else:
            pass
     
    # using set() to remove all duplicate candidate names and then restore back to a sorted list
    candidateList = sorted(list(set(candidateList)))

    # can print the candidate List to verify who the candidates are, and in what order when sorted alphabetically
    #print(candidateList) 

    # Calculating % of Votes for each candidate
    Stockham_Votes_Percent = (Stockham_Votes / totalVotes) * 100
    Degette_Votes_Percent = (Degette_Votes / totalVotes) * 100
    Doane_Votes_Percent = (Doane_Votes / totalVotes) * 100

    # start generating the output
    output = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {totalVotes}\n"
        f"-------------------------\n"
        f"{candidateList[0]}: {Stockham_Votes_Percent:,.3f}% ({Stockham_Votes})\n"
        f"{candidateList[1]}: {Degette_Votes_Percent:,.3f}% ({Degette_Votes})\n"
        f"{candidateList[2]}: {Doane_Votes_Percent:,.3f}% ({Doane_Votes})\n"
        f"Winner: {candidateList[1]}\n"
        f"-------------------------\n"

    )


# print output to terminal
print(output)

# export the output to the output text file
with open(outputFile, "w") as textFile:
    textFile.write(output)