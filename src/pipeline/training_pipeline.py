<<<<<<< HEAD
from src.data_processing import DataProcessing
from src.model_training import ModelTraining

if __name__=="__main__":
    processor = DataProcessing("artifacts/raw/data.csv" , "artifacts/processed")
    processor.run()

    trainer = ModelTraining("artifacts/processed/" , "artifacts/models/")
    trainer.run()
=======
from src.data_processing import DataProcessing
from src.model_training import ModelTraining

if __name__=="__main__":
    processor = DataProcessing("artifacts/raw/data.csv" , "artifacts/processed")
    processor.run()

    trainer = ModelTraining("artifacts/processed/" , "artifacts/models/")
    trainer.run()
>>>>>>> afaeb17a88fcf97e9a4ada587857d23cd6c3bbbd
