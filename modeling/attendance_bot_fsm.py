import networkx as nx
import matplotlib.pyplot as plt
from random import choice


class AttendanceBotFSM:
    def __init__(self):
        self.states = [
            "initial",
            "registered",
            "present",
            "left",
            "on_vacation",
            "deleted",
        ]
        self.transitions = [
            ("initial", "registered"),
            ("registered", "present"),
            ("registered", "on_vacation"),
            ("registered", "deleted"),
            ("present", "left"),
            ("left", "present"),
            ("on_vacation", "registered"),
            ("on_vacation", "deleted"),
        ]
        self.G = nx.DiGraph()
        self.G.add_nodes_from(self.states)
        self.G.add_edges_from(self.transitions)
        self.current_state = "initial"
        self.state_counts = {state: 0 for state in self.states}

    def transition(self):
        possible_transitions = [
            t[1] for t in self.transitions if t[0] == self.current_state
        ]
        if not possible_transitions:
            raise ValueError("No valid transition from current state.")
        self.current_state = choice(possible_transitions)
        self.state_counts[self.current_state] += 1

    def simulate(self, num_iterations):
        for _ in range(num_iterations):
            self.state_counts[self.current_state] += 1
            self.transition()

    def get_state_counts(self):
        return self.state_counts

    def draw(self):
        pos = nx.spring_layout(self.G)
        nx.draw(
            self.G,
            pos,
            with_labels=True,
            node_size=3000,
            node_color="lightblue",
            font_size=10,
            font_weight="bold",
            edge_color="gray",
            arrows=True,
        )
        plt.title("AttendanceBot Finite State Machine")
        plt.show()
