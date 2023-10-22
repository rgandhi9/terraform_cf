from google.cloud import storage
import requests
import pandas as pd
import datetime

# Get positional data from url
# Correctly format dictionary
# Convert dictionary to DF
# Convert to csv and store in GCS bucket

def function_entry():
    data = requests.get('http://api.open-notify.org/iss-now.json')
    data_dict = data.json()['iss_position']
    data_dict['timestamp'] = data.json()['timestamp']
    df = pd.DataFrame.from_dict(data_dict, orient='index')

    storage_client = storage.Client(project='tough-flow-388709')
    bucket = storage_client.bucket('iss_data')
    blob = bucket.blob(f'{datetime.datetime.now()}.csv')
    blob.upload_from_string(df.to_csv(), 'text/csv')

function_entry()
