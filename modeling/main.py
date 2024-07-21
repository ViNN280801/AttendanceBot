from attendance_bot_fsm import AttendanceBotFSM
from monte_carlo_simulator import MonteCarloSimulator, plt

# Create FSM and run simulation
fsm = AttendanceBotFSM()
try:
    fsm.simulate(1000)
except Exception:
    pass

# Get state counts and visualize results
state_counts = fsm.get_state_counts()
fsm.draw()

# Plot state frequency distribution
plt.figure(figsize=(10, 6))
plt.bar(state_counts.keys(), state_counts.values(), color="skyblue")
plt.xlabel("States")
plt.ylabel("Frequency")
plt.title("State Frequency Distribution using Monte Carlo Simulation")
plt.xticks(rotation=45)
plt.show()

# Define possible user actions
actions = [
    "register",
    "check_in",
    "go_on_vacation",
    "delete_account",
    "check_out",
    "check_in_again",
    "end_vacation",
    "delete_account_on_vacation",
]

# Create Monte Carlo simulator and run simulation
mc_simulator = MonteCarloSimulator(actions, 1000)
mc_simulator.simulate_user_actions()

# Calculate percentages for state counts
total_states = sum(state_counts.values())
state_percentages = {
    state: (count / total_states) * 100 for state, count in state_counts.items()
}

# Save results to text file
with open("simulation_results.txt", "w") as f:
    f.write("State Counts:\n")
    for state, count in state_counts.items():
        f.write(f"{state}: {count}\n")
    f.write("\nState Percentages:\n")
    for state, percentage in state_percentages.items():
        f.write(f"{state}: {percentage:.2f}%\n")

# Calculate percentages for user actions
user_actions_distribution = {
    action: int((mc_simulator.user_actions == idx + 1).sum())
    for idx, action in enumerate(actions)
}
total_actions = sum(user_actions_distribution.values())
action_percentages = {
    action: (count / total_actions) * 100
    for action, count in user_actions_distribution.items()
}

# Append user actions results to text file
with open("simulation_results.txt", "a") as f:
    f.write("\nUser Actions Counts:\n")
    for action, count in user_actions_distribution.items():
        f.write(f"{action}: {count}\n")
    f.write("\nUser Actions Percentages:\n")
    for action, percentage in action_percentages.items():
        f.write(f"{action}: {percentage:.2f}%\n")
