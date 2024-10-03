# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
List_candidates = []
candidate_votes = {}  # Dictionary to track candidate names and vote counts

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        # Increment the total vote count for each row
        total_votes += 1
        candidate_name = str(row[2])

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in List_candidates:
            List_candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0  # Initialize vote count for the new candidate

        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    # Print the total vote count (to terminal)
    print("Election Results")
    print("-----------------------------")
    print(f"Total votes: {total_votes}")
    print("-----------------------------")
    print(f"Candidates list: {List_candidates}")
    print("-----------------------------")
    # Write the total vote count to the text file
    txt_file.write("Election Results\n")
    txt_file.write("-----------------------------\n")
    txt_file.write(f"Total votes: {total_votes}\n")
    txt_file.write("-----------------------------\n")
    txt_file.write(f"Candidates list: {List_candidates}\n")
    txt_file.write("-----------------------------\n")
    # Initialize variables for the winning candidate
    winning_candidate = ""
    winning_count = 0

    # Loop through the candidates to calculate their vote counts and percentages
    for candidate, votes in candidate_votes.items():
        # Calculate the vote percentage
        vote_percentage = (votes / total_votes) * 100
        
        # Print and save each candidate's vote count and percentage
        print(f"{candidate}: {votes} votes ({vote_percentage:.2f}%)")
        txt_file.write(f"{candidate}: {votes} votes ({vote_percentage:.2f}%)\n")
        
        # Update the winning candidate if this one has more votes
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate

    # Print and save the winning candidate summary
    print("-----------------------------")
    print(f"Winner: {winning_candidate}")
    print(f"Winning Vote Count: {winning_count}")
    print("-----------------------------")

    # Save the winning candidate summary to the text file
    txt_file.write("-----------------------------\n")
    txt_file.write(f"Winner: {winning_candidate}\n")
    txt_file.write(f"Winning Vote Count: {winning_count}\n")
    txt_file.write("-----------------------------\n")



     