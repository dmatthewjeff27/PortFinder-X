import json
import csv
from datetime import datetime

def save_json(results, filename):
    with open(filename, "w") as f:
        json.dump(results, f, indent=4)

def save_csv(results, filename):
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["port", "service", "banner"])
        writer.writeheader()
        for row in results:
            writer.writerow(row)
