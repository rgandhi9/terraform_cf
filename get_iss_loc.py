from google.cloud import storage
import requests
import pandas as pd
import datetime
data = requests.get('http://api.open-notify.org/iss-now.json')
data_dict = data.json()['iss_position']
data_dict['timestamp'] = data.json()['timestamp']
df = pd.DataFrame.from_dict(data_dict, orient='index')

storage_client = storage.Client(project='tough-flow-388709')
bucket = storage_client.bucket('iss_data')
blob = bucket.blob(f'{datetime.datetime.now()}.csv')
blob.upload_from_string(df.to_csv(), 'text/csv')
#df.to_csv(f'gs://iss_data/{datetime.datetime.now()}.csv')
