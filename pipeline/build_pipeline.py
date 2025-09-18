from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException

load_dotenv()

logger = get_logger(__name__)

def main():
    try:
        logger.info("Starting to build pipeline >>>")

        loader = AnimeDataLoader("data/anime_with_synopsis.csv", "data/updated_anime.csv")

        processed_csv = loader.load_and_process()
        logger.info("Data loaded and processed >>>")

        vector_builder = VectorStoreBuilder(processed_csv)
        vector_builder.build_and_save_vector_store()

        logger.info("Vector store built successfully")

        logger.info("pipeline built successfully")
    
    except Exception as e:
        raise CustomException("Error during pipeline intialization")
    

main()