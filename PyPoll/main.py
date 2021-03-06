# imports
import os
import csv


# declare global variables
total_votes = 0
list_of_candidates = []
candidate_votes = {}
votes = 0
votes_percentage = 0.0
winning_candidate = ""
winners_votes = 0

# import the data
file_to_read = os.path.join('Resources', 'election_data.csv')
file_to_write = os.path.join('output', 'election_results.txt')


with open(file_to_read) as election_data:
    csv_reader = csv.reader(election_data)

    # read the first row and store it in the variable 'header'
    header = next(csv_reader)
    # print(header)
    #first = next(csv_reader)
    # print(first[1])

    # for loop
    for row in csv_reader:
        total_votes = total_votes+1

        candidate = row[2]
        if candidate not in list_of_candidates:
            list_of_candidates.append(candidate)
            candidate_votes[candidate] = 0
        candidate_votes[candidate] = candidate_votes[candidate]+1
# add in here (nohing else in for loop or in with open)

# open the output file
with open(file_to_write, "w") as output_text:
    results = (
        f"\n\n Election Results\n"
        f"----------------------\n"
        f"Total Votes: {total_votes}\n"
        f"----------------------\n"
    )
    print(results)
    output_text.write(results)

    # loop for determining winner
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        votes_percentage = float(votes)/float(total_votes)*100
        # determine winner and wining vote count
        if (votes > winners_votes):
            winning_candidate = candidate
            winners_votes = votes
        candidate_output = (
            f"{candidate}: {votes_percentage:.3}% {votes}\n"
        )
        print(candidate_output, end="")
        output_text.write(candidate_output)

    # print each candidate and their vote count
    candidate_winner = (
        f"----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"----------------------\n"
    )
    # print winning candidate
    print(candidate_winner, end="")
    output_text.write(candidate_winner)
