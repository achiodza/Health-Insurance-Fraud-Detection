import csv

def compare_prices(afoz_file, healthrecords_file, fraud_file):
    inflated_price_factor = 1.05  # 5% increase threshold for flagging as fraud
    
    with open(afoz_file, 'r') as afoz_csv, open(healthrecords_file, 'r') as healthrecords_csv, \
            open(fraud_file, 'w', newline='') as fraud_csv:
        
        afoz_reader = csv.DictReader(afoz_csv)
        healthrecords_reader = csv.DictReader(healthrecords_csv)
        fraud_writer = csv.DictWriter(fraud_csv, fieldnames=healthrecords_reader.fieldnames + ['fraudulent'])
        fraud_writer.writeheader()

        afoz_prices = {row['item_name']: float(row['standard_price']) for row in afoz_reader}

        for record in healthrecords_reader:
            medication = record['medication']
            item_cost = float(record['item_cost'])
            standard_price = afoz_prices.get(medication)
            
            if standard_price is not None and item_cost > standard_price * inflated_price_factor:
                record['fraudulent'] = 'fraudulent'
            else:
                record['fraudulent'] = 'not fraudulent'
            
            fraud_writer.writerow(record)

# Usage:
compare_prices('afoz.csv', 'healthrecords.csv', 'fraud_records.csv')
