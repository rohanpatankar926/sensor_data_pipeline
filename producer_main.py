from src.kafka_producer.json_producer import produce_data_using_file
import os

if __name__=="__main__":
    topics=os.listdir(f"{os.getcwd()}/sample_data")
    print("topics",topics)
    for topic in topics:
        sample_topics_data_dir=os.path.join(os.getcwd(),"sample_data",topic)
        sample_file_path=os.path.join(sample_topics_data_dir,os.listdir(sample_topics_data_dir)[0])
        produce_data_using_file(topic=topic,file_path=sample_file_path)