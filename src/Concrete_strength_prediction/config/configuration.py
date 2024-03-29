from src.Concrete_strength_prediction.utils.constant import *
from src.Concrete_strength_prediction.utils.common import read_yaml,create_directories
from src.Concrete_strength_prediction.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig

class ConfigurationManager:
    def __init__(self,
                 config_file_path=CONFIG_FILE_PATH,
                 params_file_path=PARAMS_FILE_PATH,
                 schema_file_path=SCHEMA_FILE_PATH):
        """
        Initialize the ConfigurationManager.

        Parameters:
        - config_file_path (str): Path to the configuration file.
        - params_file_path (str): Path to the parameters file.
        - schema_file_path (str): Path to the schema file.
        """
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        self.schema = read_yaml(schema_file_path)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Get DataIngestionConfig based on the configuration.

        Returns:
        - DataIngestionConfig: An instance of DataIngestionConfig.
        """
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            raw_data_path=config.raw_data_path,
        )

        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        """
        Get DataValidationConfig based on the configuration.

        This method extracts the relevant information from the configuration,
        creates a DataValidationConfig instance, and returns it.

        Returns:
        - DataValidationConfig: An instance of DataValidationConfig.
        """
        config = self.config.data_validation
        schema = self.schema.columns
        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            raw_data_path=config.raw_data_path,
            validation_status=config.validation_status,
            schema=schema
        )

        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        """
        Get the configuration for data transformation.

        Returns:
        - DataTransformationConfig: An instance of the DataTransformationConfig class representing
          the configuration for data transformation.
        """
        config = self.config.data_transformation
        columns_name = self.schema.columns
        target_columns_name = self.schema.target_columns

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            raw_data_path=config.raw_data_path,
            preprocessor=config.preprocessor,
            train_data=config.train_data,
            test_data=config.test_data,
            columns_name=columns_name,
            target_columns_name=target_columns_name
        )

        return data_transformation_config
    

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        """
        Get the ModelTrainer configuration.

        Returns:
        - ModelTrainerConfig: Configuration object containing settings for model training.
        """
        config = self.config.model_training
        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data=config.train_data,
            test_data=config.test_data,
            best_model_path=config.best_model_path,
            params=self.params
        )

        return model_trainer_config



