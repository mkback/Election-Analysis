
import csv
import os
# Assing a variable for the file to load and the path 
file_to_load = os.path.join("Resources", "election_results.csv")
#Create the file name to save results in 
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Intitialize a total vote count 
total_votes = 0

#Declare a candidate list
candidate_options = []

#Declare a candidate dictionary 
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open the election results and read the file 
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Print just header row in the CSV file 
    headers = next(file_reader)
    
    #Print each row in the CSV file 
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #tracking candidate voter count
            candidate_votes[candidate_name] = 0
        #add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

#Determine % of votes each got
for candidate_name in candidate_votes:
    #get votes for each candidate
    votes = candidate_votes[candidate_name]
    #calc %
    vote_percentage = float(votes) / float(total_votes) *100
    #Determine winning vote count & Canidate
    if(votes>winning_count) and (vote_percentage > winning_percentage): 
        #if this cand is the most, then change winning 
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name
    # To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
