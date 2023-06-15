import csv

def compare_csv(csv1_path, csv2_path, column_name, output_path):
    # Read csv1 and store column x values in a dictionary
    csv1_data = {}
    with open(csv1_path, 'r') as csv1_file:
        csv1_reader = csv.DictReader(csv1_file)
        for row in csv1_reader:
            csv1_data[row[column_name]] = row

    # Read csv2 and compare values in column x with csv1
    with open(csv2_path, 'r') as csv2_file, open(output_path, 'w', newline='') as csv3_file:
        csv2_reader = csv.DictReader(csv2_file)
        fieldnames = csv2_reader.fieldnames + ['Fraudulent']
        csv3_writer = csv.DictWriter(csv3_file, fieldnames=fieldnames)
        csv3_writer.writeheader()

        for row in csv2_reader:
            csv1_row = csv1_data.get(row[column_name])
            if csv1_row and float(row[column_name]) > float(csv1_row[column_name]):
                row['Fraudulent'] = 'Yes'
            else:
                row['Fraudulent'] = 'No'
            csv3_writer.writerow(row)

    print(f"Comparison completed. Results saved in {output_path}.")

# Usage example:
csv1_path = 'medical_data.csv'
csv2_path = 'fraud_data.csv'
column_name = 'total_cost'
output_path = 'csv3.csv'

compare_csv(csv1_path, csv2_path, column_name, output_path)
