import pandas as pd

file_path = r'C:\Users\vjmar\Desktop\DataScience\blue-team-project-1\hpstimeseries.txt'

df = pd.read_csv(file_path, sep='|', comment='#')

# Print the first few rows (head) of the DataFrame
print(df.head())
