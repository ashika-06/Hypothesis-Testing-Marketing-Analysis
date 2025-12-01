import pandas as pd
import os

filename = 'marketing_campaign.csv' 
temp_filename = 'marketing_campaign_clean.csv'

# --- 1. Read the file assuming it is a quoted CSV (which it is) ---
# We use the default comma separator.
df = pd.read_csv(filename, engine='python')

# --- 2. Write it back out using standard CSV settings (no quotes, no index) ---
df.to_csv(temp_filename, index=False, quoting=1) # quoting=1 means minimal quoting

# --- 3. Replace the old file ---
os.replace(temp_filename, filename)
print(f"File {filename} successfully cleaned and standardized.")