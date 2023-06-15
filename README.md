# Health-Insurance-Fraud-Detection / Flask Fraud Analysis Web Application

This is a Flask web application that performs fraud analysis on a provided CSV file. It generates visualizations and a table to analyze fraudulent claims. Follow the steps below to set up and run the application.

## Setup Instructions

1. Clone the repository or download the code files.

2. Install the required dependencies by running the following command:
   ```shell
   pip install -r requirements.txt
   ```

3. Ensure you have Python 3.x installed on your machine.

## Running the Application

1. Open a terminal or command prompt and navigate to the project directory.

2. Run the following command to start the Flask application:
   ```shell
   python app.py
   ```

3. The application will be available at [http://localhost:5000](http://localhost:5000).

## Usage

1. Access the home page by visiting [http://localhost:5000](http://localhost:5000).

2. Click on the "Login" link to access the dashboard.

3. Upload a CSV file containing the data for analysis. The file should have the following columns: `diagnosis`, `total_cost`, and `fraudulent`.

4. The application will generate two graphs and a table based on the uploaded data:
   - **Graph 1:** Total Cost by Diagnosis (Bar Chart)
   - **Graph 2:** Fraudulent Claims (Pie Chart)
   - **Fraud Table:** Table displaying fraudulent claims

5. The graphs and table will be displayed on the result page.

## Dependencies

The following dependencies are required to run the application:
- Flask
- pandas
- matplotlib

You can install these dependencies by running `pip install -r requirements.txt`.

**Note:** Make sure to provide a CSV file with the required columns (`diagnosis`, `total_cost`, and `fraudulent`) for the application to perform the analysis correctly.

Feel free to customize the application as per your requirements and design preferences. Happy fraud analysis!
