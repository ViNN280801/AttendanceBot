import numpy as np
import matplotlib.pyplot as plt


class MonteCarloSimulator:
    def __init__(self, actions, num_iterations):
        self.actions = actions
        self.num_iterations = num_iterations
        self.user_actions = np.random.randint(1, len(actions) + 1, size=num_iterations)

    def simulate_user_actions(self):
        plt.figure(figsize=(10, 6))
        plt.hist(
            self.user_actions,
            bins=np.arange(1, len(self.actions) + 2) - 0.5,
            edgecolor="black",
            align="mid",
        )
        plt.title("Distribution of User Actions")
        plt.xlabel("User's action")
        plt.ylabel("Frequency")
        plt.xticks(np.arange(1, len(self.actions) + 1), self.actions)
        plt.show()
