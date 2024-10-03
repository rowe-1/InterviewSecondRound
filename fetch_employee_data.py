from elasticsearch import Elasticsearch

# Initialize Elasticsearch client with authentication
es = Elasticsearch(
    [{'host': 'localhost', 'port': 9200, 'scheme': 'http'}],
    http_auth=('elastic', '8BzQzbTcvlxMPGIydMeP')  # Replace with your actual username and password
)

# Fetch all documents from the index
response = es.search(index='employee_data', body={"query": {"match_all": {}}})

# Print the results
for hit in response['hits']['hits']:
    print(hit['_source'])
