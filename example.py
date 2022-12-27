import json
from pathlib import Path

import pandas as pd
from synthetic_table_metrics import SyntheticTableMetrics, Data
from sklearn import datasets
iris = datasets.load_iris()


# Metrics where synthetic is a clone of the original dataset:
# Load both datasets
# real = pd.read_csv(Path("data", "iris_original.csv"))
# synthetic = pd.read_csv(Path("data", "iris_original.csv"))
real = pd.read_csv(Path("data", "Users.csv"))
synthetic = pd.read_csv(Path("data", "SyntheticUsers.csv"))
# Put datasets in datacontainer
data = Data(real, synthetic)
# data = Data(iris, iris)
# Create metrics object and run for data
metrics = SyntheticTableMetrics()
results = metrics.run(data)
# Print resultsv1v      
print("\n-- COPY:")
print(json.dumps(results, indent=2))


# Metrics on a bad synthetic dataset:
# synthetic = pd.read_csv(Path("data", "iris_bad_synthetic_data.csv"))
# data = Data(real, synthetic)
# metrics = SyntheticTableMetrics()
# results = metrics.run(data)
# print("\n-- BAD SYNTHETIC DATA:")
# print(json.dumps(results, indent=2))
