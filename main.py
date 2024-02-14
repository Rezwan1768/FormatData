import csv
import json

# Read the data from CSV file
data = []
with open('data.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)

# Organize the data into JSON format
disease_data = {}
for row in data:
    disease = row['Label']
    text = row['Text']
    response = row['Response']

    if disease not in disease_data:
        disease_data[disease] = {'tag': disease, 'phrases': [], 'response': []}

    disease_data[disease]['phrases'].append(text)
    disease_data[disease]['response'].append(response)


# Convert to JSON
json_data = {'Diseases': list(disease_data.values())}

# Write JSON to a file or print it
with open('data.json', 'w') as jsonfile:
    json.dump(json_data, jsonfile, indent=4)
