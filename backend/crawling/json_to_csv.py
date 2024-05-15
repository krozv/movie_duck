import json
import csv

def json_to_csv(json_file, csv_file):
    # Open the JSON file and load data
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Get the fieldnames (header) from the first item
    fieldnames = list(data[0].keys())

    # Open CSV file for writing
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        # Write header
        writer.writeheader()

        # Write data rows
        writer.writerows(data)

# Example usage:
json_to_csv('discover_kor_movie.json', 'discover_kor_movie.csv')
