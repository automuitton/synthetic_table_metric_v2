"""data_container.py

Simple container class for real and synthetic data.
"""
from rdt.hyper_transformer import HyperTransformer


class Data:
    """
    Container for real and synthetic data as well as their
    transformed versions.
    """
    def __init__(self, real, synthetic):
        self.real_raw = real
        self.synthetic_raw = synthetic
        ht = HyperTransformer()
        ht.detect_initial_config(data = real)
        ht.fit(real)
        self.real = ht.transform(real)
        ht.detect_initial_config(data = synthetic)
        ht.fit(synthetic)
        self.synthetic = ht.transform(synthetic)
        