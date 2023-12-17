# Define a S_list of tiers and their status credits
tiers = [("Bronze", 0), ("Silver", 300), ("Gold", 700), ("Platinum", 1400), ("Platinum One", 3600)]

# Ask the user to enter their status credits
status_credits = int(input("Status credits: "))

# Find the current tier and the next tier
current_tier = None
next_tier = None
for i in range(len(tiers)):
    if status_credits >= tiers[i][1]:
        current_tier = tiers[i]
    if status_credits < tiers[i][1]:
        next_tier = tiers[i]
        break

# Print the current tier and the status credits needed to reach the next tier
if current_tier is not None and current_tier is not tiers[4]:
    print(f"Your membership tier is : {current_tier[0]}")
    print(f"Status credits needed to reach the next tier : {next_tier[1] - status_credits}")
else:
    print(f"Your membership tier is : {current_tier[0]}")
    print(f"Status credits needed to reach the next tier : 0")