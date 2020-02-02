import csv
from matrices import Matrix

# Get rid of repeated responses
# 33: major, 34: social media (optional)
responses = {}

with open('2020results.csv', newline='', encoding='utf8') as file:
    reader = csv.reader(file, delimiter=',')
    i = 1
    for row in reader:
        responses[row[1]] = row
        
        
        
    