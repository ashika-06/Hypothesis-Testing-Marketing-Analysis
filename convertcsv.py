import pandas as pd
import os

filename = 'marketing_campaign.csv' 
temp_filename = 'marketing_campaign_clean.csv'

df = pd.read_csv(filename, engine='python')


df.to_csv(temp_filename, index=False, quoting=1) # quoting=1 means minimal quoting


os.replace(temp_filename, filename)
print(f"File {filename} successfully cleaned and standardized.")
