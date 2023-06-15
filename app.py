from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('dashboard.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if not file:
        return "No file uploaded"

    # Read the CSV file
    data = pd.read_csv(io.StringIO(file.read().decode('utf-8')))

    # Generate graphs and fraud analysis
    graph1_url = generate_graph1(data)
    graph2_url = generate_graph2(data)
    fraud_table = generate_fraud_table(data)

    return render_template('result.html', graph1_url=graph1_url, graph2_url=graph2_url, fraud_table=fraud_table)

def generate_graph1(data):
    # Generate a graph based on total cost by diagnosis
    plt.figure(figsize=(10, 5))
    total_cost_by_diagnosis = data.groupby('diagnosis')['total_cost'].sum()
    total_cost_by_diagnosis.plot(kind='bar')
    plt.xlabel('Diagnosis')
    plt.ylabel('Total Cost')
    plt.title('Total Cost by Diagnosis')
    plt.grid(True)

    # Convert the graph to a base64-encoded image
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()  # Close the figure to free up memory

    return graph_url

def generate_graph2(data):
    # Generate a graph based on fraudulent claims
    plt.figure(figsize=(10, 5))
    fraudulent_counts = data['fraudulent'].value_counts()
    fraudulent_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title('Fraudulent Claims')
    plt.legend(labels=['Non-Fraudulent', 'Fraudulent'])

    # Convert the graph to a base64-encoded image
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()  # Close the figure to free up memory

    return graph_url

def generate_fraud_table(data):
    # Filter fraudulent claims
    fraudulent_claims = data[data['fraudulent'] == "fraudulent"]

    # Generate an HTML table with fraudulent claims
    fraud_table = fraudulent_claims.to_html(index=False, classes='table table-striped')

    return fraud_table

@app.route('/result')
def result():
    graph1_url = request.args.get('graph1_url')
    graph2_url = request.args.get('graph2_url')
    fraud_table = request.args.get('fraud_table')
    return render_template('result.html', graph1_url=graph1_url, graph2_url=graph2_url, fraud_table=fraud_table)

if __name__ == '__main__':
    app.run(debug=True)
