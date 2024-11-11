from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
# Define the network structure
model = BayesianNetwork([('Fire', 'Alert'), ('Storm', 'Alert'), ('Alert', 'RajCalls'), ('Alert', 'SimranCalls')])

# Define CPDs for each variable
cpd_fire = TabularCPD('Fire', 2, [[0.997], [0.003]])
cpd_storm = TabularCPD('Storm', 2, [[0.996], [0.004]])

cpd_alert = TabularCPD('Alert', 2, [[0.998, 0.65, 0.08, 0.02], [0.002, 0.35, 0.92, 0.98]],
                       ['Fire', 'Storm'], [2, 2])

cpd_raj_calls = TabularCPD('RajCalls', 2, [[0.88, 0.15], [0.12, 0.85]],
                           ['Alert'], [2])

cpd_simran_calls = TabularCPD('SimranCalls', 2, [[0.92, 0.25], [0.08, 0.75]],
                              ['Alert'], [2])

# Add CPDs to the model
model.add_cpds(cpd_fire, cpd_storm, cpd_alert, cpd_raj_calls, cpd_simran_calls)
assert model.check_model()

# Initialize the inference engine
inference = VariableElimination(model)

# Query the network
fire_result = inference.query(['Fire'], evidence={'RajCalls': 1, 'SimranCalls': 1})
print("Probability of Fire given Raj and Simran called:\n", fire_result)

alert_result = inference.query(['Alert'], evidence={'Fire': 1})
print("\nProbability of Alert given Fire:\n", alert_result)
