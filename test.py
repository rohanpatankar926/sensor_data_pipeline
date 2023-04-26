from src.kafka_logger import logger


def div(a,b):
    try:
        logger.logging.info("div of two numbers")
        div=a/b
        logger.logging.info(f"div of {a} and {b} is {div}") 
        return div
    except Exception as e:
        logger.logging.error(f"error is {e}")
        raise e
    

if __name__=="__main__":
    div(2,0)