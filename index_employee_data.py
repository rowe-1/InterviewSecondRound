import pandas as pd
from elasticsearch import Elasticsearch, helpers
from elasticsearch.helpers import BulkIndexError

# Initialize Elasticsearch client
es = Elasticsearch("http://localhost:9200", basic_auth=('elastic', '8BzQzbTcvlxMPGIydMeP'))

# Read the CSV file into a DataFrame
df = pd.read_csv('C:\\Users\\rowen\\Desktop\\elasticsearch_project\\employee_sample_data.csv', encoding='ISO-8859-1')

# Prepare the data for indexing
def generate_data():
    for index, row in df.iterrows():
        yield {
            "_index": "hash_3294",  # Replace with your index name
            "_source": {
                "Employee ID": row['Employee ID'],
                "Full Name": row['Full Name'],  # Updated to match actual column name
                "Job Title": row['Job Title'],
                "Department": row['Department'],
                "Business Unit": row['Business Unit'],
                "Gender": row['Gender'],
                "Ethnicity": row['Ethnicity'],
                "Age": row['Age'],
                "Hire Date": row['Hire Date'],
                "Annual Salary": row['Annual Salary'],
                "Bonus %": row['Bonus %'],
                "Country": row['Country'],
                "City": row['City'],
                "Exit Date": row['Exit Date']
            }
        }

# Index the data and handle errors
try:
    helpers.bulk(es, generate_data())
    print("Data indexed successfully.")
except BulkIndexError as e:
    print(f"Failed to index documents: {e.errors}")
