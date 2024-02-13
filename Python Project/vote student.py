candidates = ["Spark", "Develop", "Reliable", "ผิง", "Guard", "SIREN", "Free Energy", "Miracle"]
votes = {candidate: 0 for candidate in candidates}

print("\nCandidates:")
print(" / ".join(candidates))

while True:
    selected_candidate = input("Enter the name of your chosen candidate (or 'exit' to finish): ")
    if selected_candidate.lower() == 'exit':
        break

    if selected_candidate in candidates:
        votes[selected_candidate] += 1
        print(f"Vote for {selected_candidate} counted successfully")
    else:
        print("Invalid candidate")

print("\nElection Results:")
print("-----------------")
total_votes = sum(votes.values())
for candidate, vote_count in votes.items():
    percentage = (vote_count / total_votes) * 100 if total_votes > 0 else 0
    print(f"{candidate}: {vote_count} votes ({percentage:.2f}%)")
print("-----------------")
print(f"Total votes: {total_votes}")
