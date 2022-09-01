from sqlalchemy import create_engine
import pandas as pd


df = pd.read_parquet('yellow_tripdata_2020-01.parquet')
df.to_csv('yellow_tripdata_2020-01.csv')
csv_database = create_engine('sqlite:///csv_database.db')

chunk_size = 215000
batch_no = 0


for chunk in pd.read_csv('yellow_tripdata_2020-01.csv', chunksize=chunk_size,
                         iterator=True, low_memory=False, index_col=0):
    chunk.to_sql('chunk_sql', csv_database, if_exists='append')
    batch_no += 1
    print(f'[+] uploading chunk_index: {batch_no}')

# Data metrics 3rd task
data = pd.read_sql_query('SELECT * FROM chunk_sql', csv_database)

# check how many missing values are in each column
missing_values = data.isnull().sum()
missing_values_df = pd.DataFrame(missing_values).T

# add missing values to a new table in the database
missing_values_df.to_sql('metrics_sql', csv_database, if_exists='append')

# Failed attempt to get more data quality metrics

# # I tried finding all total_amount values below zero saving them to a dataframe like this :
# invalid_total_amount = data[(data['total_amount'] < 0)]
# invalid_total_amount_df = pd.DataFrame(invalid_total_amount)
#
# # then finding all tpep_pickup_datetime values which were greater than tpep_dropoff_datetime
# invalid_p_d_times = data[(data['tpep_pickup_datetime'] > data['tpep_dropoff_datetime'])]
# invalid_p_d_times_df = pd.DataFrame(invalid_p_d_times)
#
# # then adding all three dataframes and uploading them as one table to the database
# metrics_df = pd.concat([missing_values, invalid_total_amount_df, invalid_p_d_times_df], axis=1, ignore_index=True)
