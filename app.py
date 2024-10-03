from flask import Flask, render_template
from elasticsearch import Elasticsearch

app = Flask(__name__)

# Connect to Elasticsearch
es = Elasticsearch(
    [{'host': 'localhost', 'port': 9200, 'scheme': 'http'}],
    basic_auth=('elastic', '8BzQzbTcvlxMPGIydMeP')  # Replace 'your_password' with the actual password
)

# Route to display employee data from Elasticsearch
@app.route('/')
def get_employees():
    # Search for all employee records in Elasticsearch
    results = es.search(index="employee_data", body={"query": {"match_all": {}}})
    employees = [doc["_source"] for doc in results["hits"]["hits"]]
    return render_template('employees.html', employees=employees)

if __name__ == '__main__':
    app.run(debug=True)
