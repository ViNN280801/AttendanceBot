from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination


class AttendanceBayesianNetwork:
    def __init__(self):
        """
        Initializes the Bayesian Network model with the defined structure and CPDs.
        """
        self.model = BayesianNetwork(
            [
                ("Register", "Check_in"),
                ("Register", "Go_on_vacation"),
                ("Register", "Delete_account"),
                ("Check_in", "Check_out"),
                ("Check_out", "Check_in_again"),
                ("Go_on_vacation", "End_vacation"),
                ("Go_on_vacation", "Delete_account_on_vacation"),
            ]
        )
        self.define_cpds()
        self.model.add_cpds(
            self.cpd_register,
            self.cpd_check_in,
            self.cpd_go_on_vacation,
            self.cpd_delete_account,
            self.cpd_check_out,
            self.cpd_check_in_again,
            self.cpd_end_vacation,
            self.cpd_delete_account_on_vacation,
        )
        assert self.model.check_model(), "Model is not valid"

    def define_cpds(self):
        """
        Defines the Conditional Probability Distributions (CPDs) for the Bayesian Network.
        """
        self.cpd_register = TabularCPD(
            variable="Register", variable_card=2, values=[[0.6], [0.4]]
        )
        self.cpd_check_in = TabularCPD(
            variable="Check_in",
            variable_card=2,
            values=[[0.7, 0.3], [0.3, 0.7]],
            evidence=["Register"],
            evidence_card=[2],
        )
        self.cpd_go_on_vacation = TabularCPD(
            variable="Go_on_vacation",
            variable_card=2,
            values=[[0.8, 0.5], [0.2, 0.5]],
            evidence=["Register"],
            evidence_card=[2],
        )
        self.cpd_delete_account = TabularCPD(
            variable="Delete_account",
            variable_card=2,
            values=[[0.9, 0.6], [0.1, 0.4]],
            evidence=["Register"],
            evidence_card=[2],
        )
        self.cpd_check_out = TabularCPD(
            variable="Check_out",
            variable_card=2,
            values=[[0.6, 0.3], [0.4, 0.7]],
            evidence=["Check_in"],
            evidence_card=[2],
        )
        self.cpd_check_in_again = TabularCPD(
            variable="Check_in_again",
            variable_card=2,
            values=[[0.5, 0.2], [0.5, 0.8]],
            evidence=["Check_out"],
            evidence_card=[2],
        )
        self.cpd_end_vacation = TabularCPD(
            variable="End_vacation",
            variable_card=2,
            values=[[0.7, 0.4], [0.3, 0.6]],
            evidence=["Go_on_vacation"],
            evidence_card=[2],
        )
        self.cpd_delete_account_on_vacation = TabularCPD(
            variable="Delete_account_on_vacation",
            variable_card=2,
            values=[[0.8, 0.5], [0.2, 0.5]],
            evidence=["Go_on_vacation"],
            evidence_card=[2],
        )

    def perform_inference(self, evidence):
        """
        Performs inference on the Bayesian Network given the evidence.

        :param evidence: Dictionary containing evidence for the inference.
        :return: Result of the query.
        """
        inference = VariableElimination(self.model)
        query_result = inference.query(
            variables=["Delete_account_on_vacation"], evidence=evidence
        )
        return query_result

    def display_cpds(self):
        """
        Displays the Conditional Probability Distributions (CPDs) of the Bayesian Network.
        """
        for cpd in self.model.get_cpds():
            print(f"CPD of {cpd.variable}:")
            print(cpd)
