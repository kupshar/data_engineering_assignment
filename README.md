Runing the code:

Windows users:
	1. Extract data_engineering_assignement.7zip
	2. Navigate to the project folder in your cmd
	3. Type command:python.exe main.py
Linux users:
	1. Extract data_engineering_assignement.7zip
	2. Navigate to the project folder in terminal
	3. Type command python3 main.py

This should create csv_database.db file in the project folder with two tables chunk_sql for the whole data and metrics_sql for metrics data.

4. Model the dataset to represent a fact-dimension type of schema. Draw the entity relationship diagram of your model and transform the data to fit it.

I don't know how to design databases or draw entity relationship diagrams yet.


5. Can you identify the weak points of the proposed solution? If you had more time, what parts of your solution would you improve? 

If I knew how to chunk parquet files I would've done it as the csv file turned out to be quite big and it takes some time to write it out and 
upload it to sql. I would also improve the data metrics part because I don't know what final solution should look like. I also need to learn more about 
fact-dimensional schemas and entity reltionships in order to complete this assignment fully.
