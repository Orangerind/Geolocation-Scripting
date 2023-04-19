#This script groups condos in 1km radius and tries to update locations as accurately as possible
import pandas as pd
from math import radians, sin, cos, sqrt, atan2

# Load the CSV file
file_path = r'C:\Users\Admin\Documents\Self learn\Data Analytics\Data Analytics Client 2\Lat Long Project sample - Sheet1.csv'
dfs = pd.read_csv(file_path)

# Define the Haversine formula function
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Earth's radius in km
    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    a = sin(dLat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dLon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

# Define a function to find the pattern between Latitude and Longitude
def find_pattern():
    lat_pattern = dfs[~dfs['NewLat'].isna()]['NewLat'] / dfs[~dfs['NewLat'].isna()]['Latitude']
    lat_pattern_mean = lat_pattern.mean()
    lat_pattern_std = lat_pattern.std()
    long_pattern = dfs[~dfs['NewLong'].isna()]['NewLong'] / dfs[~dfs['NewLong'].isna()]['Longitude']
    long_pattern_mean = long_pattern.mean()
    long_pattern_std = long_pattern.std()
    return lat_pattern_mean, lat_pattern_std, long_pattern_mean, long_pattern_std

# Compute the pattern between Latitude and Longitude
lat_pattern_mean, lat_pattern_std, long_pattern_mean, long_pattern_std = find_pattern()

# Fill in AveLatDiff and AveLongDiff columns
dfs.loc[dfs['NewLat'].isna(), 'AveLatDiff'] = (dfs[dfs['NewLat'].isna()]['Latitude'] * lat_pattern_mean) - dfs[dfs['NewLat'].isna()]['Latitude']
dfs.loc[dfs['NewLong'].isna(), 'AveLongDiff'] = (dfs[dfs['NewLong'].isna()]['Longitude'] * long_pattern_mean) - dfs[dfs['NewLong'].isna()]['Longitude']

# Compute missing values for NewLat and NewLong
dfs.loc[dfs['NewLat'].isna(), 'NewLat'] = dfs['Latitude'] + dfs['AveLatDiff']
dfs.loc[dfs['NewLong'].isna(), 'NewLong'] = dfs['Longitude'] + dfs['AveLongDiff']

# Create a new column for group number
dfs['Group#'] = -1

# Check if each row is within 1km radius of each other and assign the same group number
group_num = 0
for i, row1 in dfs.iterrows():
    if dfs.loc[i, 'Group#'] == -1:
        group_num += 1
        dfs.loc[i, 'Group#'] = group_num
    for j, row2 in dfs.iterrows():
        if i < j and dfs.loc[j, 'Group#'] == -1:
            dist = haversine(row1['NewLat'], row1['NewLong'], row2['NewLat'], row2['NewLong'])
            if dist <= 1:
                dfs.loc[j, 'Group#'] = dfs.loc[i, 'Group#']
# Fill in 'Condo Names' column with group numbers if blank
for i, row in dfs.iterrows():
    if pd.isnull(row['Condo Name']):
        group_num = str(row['Group#'])
        dfs.loc[i, 'Condo Name'] = f'Group {group_num}'

# Define a function to calculate the distance between two coordinates
def distance(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in kilometers
    d_lat = radians(lat2 - lat1)
    d_lon = radians(lon2 - lon1)
    a = sin(d_lat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(d_lon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

# Calculate the average latitude and longitude difference for each row
dfs['AveLatDiff'] = dfs.apply(lambda row: distance(row['Latitude'], row['Longitude'], row['NewLat'], row['Longitude']) / 2, axis=1)
dfs['AveLongDiff'] = dfs.apply(lambda row: distance(row['Latitude'], row['Longitude'], row['Latitude'], row['NewLong']) / 2, axis=1)

dfs = dfs.drop(['AveLatDiff', 'AveLongDiff', 'Group#'], axis=1)

dfs.to_csv(r'C:\Users\Admin\Documents\Self learn\Data Analytics\Data Analytics Client 2\Output.csv')