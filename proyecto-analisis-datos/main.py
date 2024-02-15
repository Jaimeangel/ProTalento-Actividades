import requests
import csv
import pandas as pd

URL='https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv'

def urlToCSV(URL):
    response = requests.get(URL)

    if response.status_code == 200:

        csv_file = 'api_data.csv'

        with open(csv_file, 'w', newline='') as file:
            file.write(response.text)

    else:
        print('Error request API')

urlToCSV(URL)