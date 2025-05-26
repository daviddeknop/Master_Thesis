import pandas as pd

# Path to your CSV file
input_file = r"E:\Users\ddknop\PDM\master_thesis\data\Zwalm_data\preprocess_output\zwalm_p_thiessen.csv"
output_file = r"E:\Users\ddknop\PDM\master_thesis\data\Zwalm_data\preprocess_output\zwalm_p_thiessen_daily.csv"

# Read the CSV file
df = pd.read_csv(input_file)

# Ensure the 'Timestamp' column is converted to datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'], format='%d/%m/%Y %H:%M')

# Set 'Timestamp' as the index (useful for resampling)
df.set_index('Timestamp', inplace=True)

# Resample the data to daily sums, aggregating 'P_thiessen' (assuming you want to sum this column daily)
df_daily = df.resample('D')['P_thiessen'].sum()

# Reset index to get 'Timestamp' back as a column (it will be in the date-only format)
df_daily = df_daily.reset_index()

# Save the result to a new CSV file
df_daily.to_csv(output_file, index=False)

print(f"Daily sum of 'P_thiessen' saved to: {output_file}")


import matplotlib.pyplot as plt

# Assuming df is the dataframe with the columns 'P_thiessen' and 'P'
df = pd.read_csv(output_file)
plt.figure(figsize=(10, 6))

# Plot 'P_thiessen' and 'P'
plt.plot(df['Timestamp'], df['P_thiessen'], label='P_thiessen', color='blue')
plt.plot(df['Timestamp'], df['P'], label='P', color='orange')

plt.xlabel('Timestamp')
plt.ylabel('Values')
plt.title('Comparison of P_thiessen and P')
plt.legend()

plt.xticks(rotation=45)  # Rotate x-axis labels if needed
plt.tight_layout()  # Adjust layout to prevent clipping
plt.show()
