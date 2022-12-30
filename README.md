# synthetic_table_metric_v2
Modifying the existing synthetic_table_metric 

## Installing using pip

    pip install git+https://github.com/automuitton/synthetic_table_metric_v2.git


## Example

    import json

    import pandas as pd
    from synthetic_table_metrics import SyntheticTableMetrics, Data

    # Metrics where synthetic is a clone of the original dataset:
    # Load both datasets
    real = pd.read_csv(Path("data", "iris_original.csv"))
    synthetic = pd.read_csv(Path("data", "iris_original.csv"))
    # Put datasets in datacontainer
    data = Data(real, synthetic)
    # Create metrics object and run for data
    metrics = SyntheticTableMetrics()
    results = metrics.run(data)
    # Print results
    print("\n-- COPY:")
    print(json.dumps(results, indent=2))


    # Metrics on a bad synthetic dataset:
    synthetic = pd.read_csv(Path("data", "iris_bad_synthetic_data.csv"))
    data = Data(real, synthetic)
    metrics = SyntheticTableMetrics()
    results = metrics.run(data)
    print("\n-- BAD SYNTHETIC DATA:")
    print(json.dumps(results, indent=2))

- supports only python 3.10 below and 3.8 above
- csv's for this example you can find data folder
- This library does support nan values! for score
- Updated packages so installation can be fluent
