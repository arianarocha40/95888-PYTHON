################################# PART A (P1) ############################################

import csv

# Define the path to the CSV file and output file for 2020 data
csv_path = 'C:/Users/arian/OneDrive/Documents/CMU-A_Laptop2/CLASSES/PYTHON/HW4/daily-treasury-rates.csv'
output_path = 'C:/Users/arian/OneDrive/Documents/CMU-A_Laptop2/CLASSES/PYTHON/HW4/daily_yield_curves_2020.txt'

# Initialize the list to store the daily yield curves
daily_yield_curves = []

# Read the CSV file and process the data
with open(csv_path, mode='r', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)

    # Define the columns to keep, ensuring they match the CSV headers
    columns_to_keep = ['Date', '1 Mo', '2 Mo', '3 Mo', '6 Mo', '1 Yr', '2 Yr',
                       '3 Yr', '5 Yr', '7 Yr', '10 Yr', '20 Yr', '30 Yr']

    # Append the header list to daily_yield_curves with lowercase formatting
    header = [col.lower() if 'mo' in col.lower() else col.lower() for col in columns_to_keep]
    daily_yield_curves.append(header)

    # Extract relevant rows and convert values to float
    for row in reader:
        try:
            # Create a list with the date and float-converted interest rate values
            data_row = [row['Date']] + [float(row[col]) for col in columns_to_keep[1:] if row[col] != '']
            # Append the data row
            daily_yield_curves.append(data_row)
        except KeyError as e:
            print(f"Column missing in row: {e}")
        except ValueError as e:
            print(f"Error converting data to float: {e}")

# Save the processed data to a text file with formatted output
with open(output_path, mode='w') as output_file:
    # Format the header
    header = "{:<12} {:<6} {:<6} {:<6} {:<6} {:<6} {:<6} {:<6} {:<6} {:<6} {:<6} {:<6} {:<6}".format(
        *daily_yield_curves[0])
    output_file.write(header + "\n")

    # Format and write each data row
    for row in daily_yield_curves[1:]:
        formatted_row = "{:<12} {:<6.2f} {:<6.2f} {:<6.2f} {:<6.2f} {:<6.2f} {:<6.2f} {:<6.2f} {:<6.2f} {:<6.2f} {:<6.2f} {:<6.2f} {:<6.2f}".format(
            row[0], *row[1:])
        output_file.write(formatted_row + "\n")
        
        
        
###################################### PART B (P1)  ############################################

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter

# Sample Data
X = np.array([[0, 0.25, 0.5, 0.75, 1]])  # 1 by 5
Y = np.array([[0.0], [0.5], [1.0]])  # 3 by 1
Z = np.array([[0.4, 0.2, 0.1, 0.1, 0.2],
              [0.3, 0.5, 0.2, 0.3, 0.4],
              [0.7, 0.6, 0.7, 0.9, 0.8]])  # 3 by 5

# Create the plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

# Plot the surface
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=1, antialiased=True)

# Show plot
plt.show()


######################################## PART C (P2) ##############################################


import pandas as pd

# Convert the list of lists to a DataFrame (no header)
columns = ['Date', '1 mo', '2 mo', '3 mo', '6 mo', '1 yr', '2 yr', '3 yr', '5 yr', '7 yr', '10 yr', '20 yr', '30 yr']
data = daily_yield_curves[1:]  # Skip the header row for the data
yield_curve_df = pd.DataFrame(data, columns=columns)

# Set the date as index and convert it to datetime format
yield_curve_df['Date'] = pd.to_datetime(yield_curve_df['Date'], format='%m/%d/%Y')
yield_curve_df.set_index('Date', inplace=True)

# Plot time series of interest rates per maturity
yield_curve_df.plot(figsize=(14, 8), title='Time Series of Interest Rates for Each Maturity')
plt.xlabel('Date')
plt.ylabel('Interest Rate (%)')
plt.grid(True)
plt.show()

# Transpose DataFrame to plot the daily yield curve for every 20th trading day
by_day_yield_curve_df = yield_curve_df.T.iloc[:, ::20]  # Select every 20th column
by_day_yield_curve_df.index = [1, 2, 3, 6, 12, 24, 36, 60, 84, 120, 240, 360]  # Convert maturity labels to months

# Plot the daily yield curve for specific trading days
by_day_yield_curve_df.plot(figsize=(14, 8), title='Daily Yield Curve for Every 20th Trading Day')
plt.xlabel('Months to Maturity')
plt.ylabel('Interest Rate (%)')
plt.grid(True)
plt.show()
