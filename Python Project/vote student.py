candidates = ["Spark", "Develop", "Reliable", "ผิง", "Guard", "SIREN", "Free Energy", "Miracle"]
votes = {candidate: 0 for candidate in candidates}

def vote(candidate):
    if candidate in candidates:
        votes[candidate] += 1
        print(f"Vote for {candidate} counted successfully")
    else:
        print("Invalid candidate")
    
def display_results():
    print("\nElection Results:")
    print("-----------------")
    total_votes = sum(votes.values())
    for candidate, vote_count in votes.items():
        percentage = (vote_count / total_votes) * 100 if total_votes > 0 else 0
        print(f"{candidate}: {vote_count} votes ({percentage:.2f}%)")
    print("-----------------")
    print(f"Total votes: {total_votes}")
    
if __name__ == "__main__":
    while True:
        print("\nCandidates:")
        print(" / ".join(candidates))
        selected_candidate = input("Enter the name of your chosen candidate (or 'exit' to finish): ")
        if selected_candidate.lower() == 'exit':
            break

        vote(selected_candidate)

    display_results()