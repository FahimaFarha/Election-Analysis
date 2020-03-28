# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.


# Add our dependencies.
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

#Create a file name variable to a direct or indirect path to the file.
file_to_save = os.path.join('analysis', 'election_analysis.txt')

# 1. Initialize a total vote counter.
total_votes = 0

#Candidate options 
candidate_options = []

# Declare dictionary
candidate_votes = {}     

# Winning candidate and winning count tracker
winning_candiate = ""
winning_count = 0
winning_percentage = 0

# # #Open the election results and read the file.
with open(file_to_load) as election_data:

     # To do: read and analyze the data here
     # Read the file object with the reader function.
     file_reader = csv.reader(election_data)

     # Read the header row
     headers = next(file_reader)
     

     # Print each row in the CSV file
     for row in file_reader:
          # 2. Add to the total vote count.
          total_votes += 1

          # Print candidate name from each row.
          candidate_name = row[2]

          # If the candidate does not match any existing candidate...
          if candidate_name not in candidate_options:
               # Add candidate name to the candidate list.
               candidate_options.append(candidate_name)

               # 2. Begin tracking candidate's vote count
               candidate_votes[candidate_name] = 0

     # Add a vote to that candidate's count
          candidate_votes[candidate_name] += 1

# Print the candidate vote dictionary
#print(candidate_votes)

     for candidate in candidate_votes:
          votes = candidate_votes[candidate]

          vote_percentage = float(votes) / float(total_votes) *100

          # Determine if the votes is greater than the winning count.
          if (votes > winning_count) and (vote_percentage > winning_percentage):
               # If true then set winning_count = votes and winning_percent = vote_percentage.
               winning_count = votes
               winning_percentage = vote_percentage
               # And set the winning_candiate equal to the candidate's name
               winning_candidate = candidate 

          print(f"{candidate}: {vote_percentage: .1f}% ({votes:,})\n")

     # Summary of who won
     winning_candidate_summary = (
          f"---------------\n"
          f"Winner: {winning_candidate}\n"
          f"Winning Vote Count: {winning_count:,}\n"
          f"Winning Percentage: {winning_percentage:.1f}%\n"
          f"---------------\n")
     print(winning_candidate_summary)

#Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
#Write some data to the file.
     txt_file.write("Counties in the Election\n----------------------------\nArapahoe\nDenver\nJefferson")
     
#Close the file













#Close the file.
#election_data.close()
