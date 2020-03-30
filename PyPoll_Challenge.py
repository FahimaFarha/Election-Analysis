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
#Declare dictionary
candidate_votes = {}     

# Winning candidate and winning count tracker
winning_candiate = ""
winning_count = 0
winning_percentage = 0

# Total votes in each county
county_total_votes = 0
# Which county will it be
county_options = []
# Declare county dictionary
county_votes = {}

# Largest County trackers
largest_county_turnout = ""
largest_county = 0
largest_county_percentage = 0


# # #Open the election results and read the file.
with open(file_to_load) as election_data:
     
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

        # Finding total votes & percentage of each county
        county_total_votes += 1
        #Print the name of the counties
        county_name = row[1]

        if county_name not in county_options:
            # Add the county name to the list
            county_options.append(county_name)

            county_votes[county_name] = 0
            
        county_votes[county_name] += 1
            

#Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    #Write some data to the file.
    election_results = (
        f"\nElection Results\n"
        f"--------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------\n")

    print(election_results, end="")
    # Save final vote count to the text file
    txt_file.write(election_results)

    # Print header for new section
    print("\nCounty Votes:")
    txt_file.write("\nCounty Votes:\n")

    # Find the percent of voter turnout and the number of votes from each county
    for county in county_votes:
        tally = county_votes[county]

        tally_percentage = float(tally) / float(county_total_votes) *100

        county_results = (f"{county}: {tally_percentage: .1f}% ({tally:,})\n")

        # Save election results of each county
        print(county_results, end="")
        txt_file.write(county_results)

        # Set largest county turnout equal to county name
        if (tally > largest_county) and (tally_percentage > largest_county_percentage):
        
            largest_county = tally
            largest_county_percentage = tally_percentage
            largest_county_turnout = county
        

           
    # Write the largest county turnout in file
    largest_county_summary = (
        f"\n--------------------\n"
        f"Largest County Turnout: {largest_county_turnout}\n"
        f"--------------------\n")
    print(largest_county_summary, end="")
    txt_file.write(largest_county_summary)


    for candidate in candidate_votes:
        votes = candidate_votes[candidate]

        vote_percentage = float(votes) / float(total_votes) *100
        #Print each candidate, their voter count, and percentage to the terminal.
        #print(f"{candidate}; {vote_percentage: .1f}% ({votes:,})\n")
        # Determine if the votes is greater than the winning count.
        candidate_results = (f"{candidate}: {vote_percentage: .1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to terminal
        print(candidate_results, end="")
        # Save candidate_results to text file
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And set the winning_candiate equal to the candidate's name
            winning_candidate = candidate 
              
    # Summary of who won what
    winning_candidate_summary = (
        f"---------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------\n")
    print(winning_candidate_summary, end="")

    txt_file.write(winning_candidate_summary)

#Close the file.
election_data.close()
