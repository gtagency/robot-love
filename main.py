import csv
from matrices import Matrix
from match import gale_shapely
import random

# Get rid of repeated responses
# 33: major, 34: social media (optional)
responses = {}

with open('2020results.csv', newline='', encoding='utf8') as file:
    reader = csv.reader(file, delimiter=',')
    i = 1
    for row in reader:
        responses[row[1]] = row

class Match:
    def __init__(self, email, score):
        self.email = email
        self.score = score
    def __lt__(self, other):
        return self.score < other.score
    def __repr__(self):
        return self.email

# Randomly split a dict in half
# Second dict may be smaller by 1
def random_split_dict(g):
    g_items = list(g.items())
    random.shuffle(g_items)
    n = len(g_items) / 2
    s1 = {}
    s2 = {}
    for i in range(len(g_items)):
        if i < n:
            s1[g_items[i][0]] = g_items[i][1]
        else:
            s2[g_items[i][0]] = g_items[i][1]
    
    return s1, s2    

# Rank the preferences of the two groups
def rank_pref(g1, g2):
    g1_pref = {}
    g2_pref = {}
    
    for p1_email, p1_response in g1.items():
        pref = []
        for p2_email, p2_response in g2.items():
            pref.append(Match(p2_email, Matrix.weight(p1_response, p2_response)))
        random.shuffle(pref)
        pref.sort()
        g1_pref[p1_email] = pref
    
    for p2_email, p2_response in g2.items():
        pref = []
        for p1_email, p1_response in g1.items():
            pref.append(Match(p1_email, Matrix.weight(p2_response, p1_response)))
        random.shuffle(pref)    
        pref.sort()
        g2_pref[p2_email] = pref       
    
    return g1_pref, g2_pref
    
# Group people for gale-shapely
matches = []
g1 = {}
g2 = {}
g3 = {}
    
for email, response in responses.items():
    if response[4] == "Male" and response[5] != 'Homosexual' and response[5] != 'Bisexual' and response[5] != 'Pansexual':
        g1[email] = response
    elif response[4] == "Female" and response[5] != 'Homosexual':
        g2[email] = response
    else:
        g3[email] = response

g4 = {}
g5 = {}
g6 = {}

for email, response in g3.items():
    if response[4] == "Other":
        g4[email] = response
    elif response[4] == "Female" and response[5] == "Homosexual":
        g5[email] = response
    else:
        g6[email] = response
    
# Rank preferences and match
g1_pref, g2_pref = rank_pref(g1, g2)
matches.append(gale_shapely.gale_shapely(g1_pref, g2_pref))

g4_1, g4_2 = random_split_dict(g4)
g4_1_pref, g4_2_pref = rank_pref(g4_1, g4_2)
matches.append(gale_shapely.gale_shapely(g4_1_pref, g4_2_pref))

g5_1, g5_2 = random_split_dict(g5)
g5_1_pref, g5_2_pref = rank_pref(g5_1, g5_2)
matches.append(gale_shapely.gale_shapely(g5_1_pref, g5_2_pref))

g6_1, g6_2 = random_split_dict(g6)
g6_1_pref, g6_2_pref = rank_pref(g6_1, g6_2)
matches.append(gale_shapely.gale_shapely(g6_1_pref, g6_2_pref))

# Check to make sure that people are only matched once
matched = set()
for match_dict in matches:
    for p1, p2 in match_dict.items():
        if p1 in matched or p2 in matched:
            print("Error")
        matched.add(p1)
        matched.add(p2)
        
print(f"Matched {len(matched)} people!")

with open('2020matches.csv', 'w', newline='', encoding='utf8') as file:
    writer = csv.writer(file)
    for match_dict in matches:
        for p1, p2 in match_dict.items():
            writer.writerow([p1, responses[p1][34], p2, responses[p2][34]])
        
        