import pandas as pd
import os

# The original file name and the assumed separator that Pandas can read locally
old_filename = 'marketing_campaign.tsv'
temp_filename = 'marketing_campaign_temp.csv'

# --- 1. Read the file using the assumed TAB separator ---
# If this line fails, you must manually inspect the file to find the true delimiter!
df = pd.read_csv(old_filename, sep='\t', engine='python')

# --- 2. Write it back out using the standard COMMA separator (sep=',') ---
df.to_csv(temp_filename, index=False, sep=',')

# --- 3. Replace the old file and delete the temp file ---
os.replace(temp_filename, 'marketing_campaign.csv')
os.remove(old_filename) # Delete the misaligned TSV file

print(f"File successfully converted to standard 'marketing_campaign.csv'.")