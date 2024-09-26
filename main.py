from src.Mask.Pipelines.data_ingestion_training import DataIngestionTraining
import os,sys
from src.Mask.exceptions import CustomException
from src.Mask.loggers import logger


stage_name = "Data ingestion stage"
try:
    logger.info(f">>>>{stage_name} started <<<<<")
    #creating an object of DataIngestionTraining class
    dit = DataIngestionTraining()
    dit.main()

    logger.info(f">>>>{stage_name} stopped <<<<<")

except Exception as e:
    raise CustomException(e,sys)