import requests
import pandas as pd
import datetime
data = requests.get('http://api.open-notify.org/iss-now.json')
data_dict = data.json()['iss_position']
data_dict['timestamp'] = data.json()['timestamp']
df = pd.DataFrame.from_dict(data_dict, orient='index')
df.to_csv(f'./{datetime.datetime.now()}.csv')
