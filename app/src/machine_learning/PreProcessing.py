from abc import ABC, abstractmethod

class PreprocessingStep(ABC):
    @abstractmethod
    def apply(self, data):
        pass

class DataPreprocessingPipeline:
    def __init__(self):
        self.steps = []

    def add_step(self, step):
        if isinstance(step, PreprocessingStep):
            self.steps.append(step)
        else:
            raise ValueError("Step must be a PreprocessingStep instance.")

    def execute(self, data):
        for step in self.steps:
            data = step.apply(data)
        return data

class DataPreprocessingPipelineBuilder:
    def __init__(self):
        self.pipeline = DataPreprocessingPipeline()

    def add_imputation(self, imputer):
        # Add imputation step to the pipeline
        self.pipeline.add_step(imputer)
        return self

    def add_encoding(self, encoder):
        # Add encoding step to the pipeline
        self.pipeline.add_step(encoder)
        return self

    def add_scaling(self, scaler):
        # Add scaling step to the pipeline
        self.pipeline.add_step(scaler)
        return self

    def build(self):
        # Return the constructed pipeline
        return self.pipeline
