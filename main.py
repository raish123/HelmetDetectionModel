from src.Mask.Pipelines.data_ingestion_training import DataIngestionTraining
import os,sys
from src.Mask.exceptions import CustomException
from src.Mask.loggers import logger
from src.Mask.Pipelines.basemodel_pipeline import BaseModelTraining
from src.Mask.Pipelines.callback_pipeline import CallbackModelTraining
from src.Mask.Pipelines.training_pipeline import ModelTrainingPipeline
from src.Mask.Pipelines.evaluating_pipeline import EvaluatingTraining


stage_name = "Data ingestion stage"
try:
    logger.info(f">>>>{stage_name} started <<<<<")
    #creating an object of DataIngestionTraining class
    dit = DataIngestionTraining()
    dit.main()

    logger.info(f">>>>{stage_name} stopped <<<<<")

except Exception as e:
    raise CustomException(e,sys)


stage_name2 = "Base Model and Sequential Model stage"
try:
    logger.info(f">>>>{stage_name2} started <<<<<")
    #creating an object of BaseModelTraining class
    bmt = BaseModelTraining()
    bmt.main()
    
    logger.info(f">>>>{stage_name2} stopped <<<<<")

except Exception as e:
    raise CustomException(e,sys)


stage_name3 = "Callback model Stage"
try:
    logger.info(f">>>>{stage_name3} started <<<<<")
    #creating an object of BaseModelTraining class
    cmt = CallbackModelTraining()
    cmt.main()
    
    logger.info(f">>>>{stage_name3} stopped <<<<<")

except Exception as e:
    raise CustomException(e,sys)



stage_name4 = "model training Stage"
try:
    logger.info(f">>>>{stage_name4} started <<<<<")
    #creating an object of BaseModelTraining class
    mtp = ModelTrainingPipeline()
    mtp.main()
    
    logger.info(f">>>>{stage_name4} stopped <<<<<")

except Exception as e:
    raise CustomException(e,sys)



stage_name5 = "Evaluating Model Stage"
try:
    logger.info(f">>>>{stage_name5} started <<<<<")
    #creating an object of BaseModelTraining class
    et = EvaluatingTraining()
    et.main()
    
    logger.info(f">>>>{stage_name5} stopped <<<<<")

except Exception as e:
    raise CustomException(e,sys)