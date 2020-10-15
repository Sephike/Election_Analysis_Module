#The data we need to retrieve.
#1. The total number of votes cast.
#2. A complete list of candidates who recieved votes
#3. The percentage of votes each candidate won.
#4. The total number of votes each candidate won.
#5. The winner of the election based on popular vote.
# Import the datetime class from the datetime module.
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Making a list for the candidates names.
candidate_options = []
# Make int to hole the total number of votes in the election.
total_votes = 0
# 1. Declare the empty dictionary.
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print the header row.
    headers = next(file_reader)
    #print each row in the csv file.
    for row in file_reader:
        # Increamenting the total votes at the beginning of each iteration
        total_votes+=1
        # Saves the candidate name on the current iteration
        candidate_name = row[2]
        # Testing to see if the current candidate is different from the last one.
        if candidate_name not in candidate_options:
            #If the candidates current name is not in the list it will be added.
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] +=1
# Using the open() function with the "w" mode we will write data to the file.
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
        # Write some data to the file.
        txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. If true then set winning_count = votes and winning_percent =
        # vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # 3. Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name
    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)