import pandas as pd
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def extract_data():
    data_filepath = "data/data.csv"
    try:
        wildfires_data = pd.read_csv(data_filepath)
        return wildfires_data
    except FileNotFoundError:
        logging.error(f"File {data_filepath} not found")
        raise
