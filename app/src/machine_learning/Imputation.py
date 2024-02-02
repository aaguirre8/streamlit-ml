import pandas as pd
from sklearn.impute import SimpleImputer
from src.machine_learning.PreProcessing import PreprocessingStep


class ImputationStep(PreprocessingStep):
    def __init__(self, strategy='mean'):
        self.strategy = strategy

    def apply(self, data):
        if isinstance(data, pd.DataFrame):
            imputer = SimpleImputer(strategy=self.strategy)
            data_imputed = imputer.fit_transform(data)
            return pd.DataFrame(data_imputed, columns=data.columns)
        else:
            raise ValueError("Data must be a pandas DataFrame.")