
import os
import csv

# SET PATH
election_csvpath = os.path.join("..","Resources","election_data.csv")
print(election_csvpath)

# VARIABLES
all_votes = 0
candidates = []
individuals_vote_count = []

# FIND TOTAL VOTE COUNTS
with open(election_csvpath, newline="") as csvfile:
    election_csvreader = csv.reader(csvfile, delimiter=",")
    csv_reader = next(election_csvreader)
    
    # SEARCH THROUGH THE ROWS
    for row in election_csvreader:
        
        all_votes += 1
        
        # CANDIDATES ARE IN 3RD ROW (listed as row 2 because 0,1,'2')
        candidate_in = (row[2])

        # CHECK IF CANDIDATE IS IN THE LIST, LOCATE & ADD 1 TO VOTE COUNT
        if candidate_in in candidates:
            candidate_index = candidates.index(candidate_in)
            individuals_vote_count[candidate_index] = individuals_vote_count[candidate_index] + 1
        
        else:
            # CANDIDATE NOT FOUND?
            candidates.append(candidate_in)
            individuals_vote_count.append(1)

# SOME MORE VARIABLES
percentage = []
max_votes = individuals_vote_count[0]
max_index = 0

for x in range(len(candidates)):
    
    # FIND THE PERCENTAGE
    vote_pct = round(individuals_vote_count[x]/all_votes*100, 2)
    percentage.append(vote_pct)
    
    if individuals_vote_count[x] > max_votes:
        max_votes = individuals_vote_count[x]
        max_index = x

winner = candidates[max_index] 


# PRINTING TO TERMINAL
print('Election Results')
print('-------------------------')
print(f'Total Votes: {all_votes}')
for x in range(len(candidates)):
    print(f'{candidates[x]} : {percentage[x]}% ({individuals_vote_count[x]})')
print('-------------------------')
print(f'Election winner: {winner.title()}')
print('-------------------------')

# OUTPUTTING TO A TXT FILE
output_file = os.path.join("pypoll_election_results.txt")
with open(output_file, "w", newline="") as datafile:
    datafile.write('Election Results\n')
    datafile.write('-------------------------\n')
    datafile.write(f'Total Votes: {all_votes}\n')
    for x in range(len(candidates)):
        datafile.write(f'{candidates[x]} : {percentage[x]}% ({individuals_vote_count[x]})\n')
    datafile.write('-------------------------\n')
    datafile.write(f'Election winner: {winner.title()}\n')
    datafile.write('-------------------------\n')