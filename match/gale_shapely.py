# Determine the position of p1 in p2's preferences 
def rank_in_pref(p1, pref):
    i = 0
    for person in pref:
        if p1 == person.email:
            return i
        i += 1

import random

# Perform the gale-shapely algorithm on the two groups
def gale_shapely(g1, g2):
    
    matches = {}
    # Index of the next unproposed preference
    asked = {}
    isMatched = {}
    
    # First round:
    # Key: person, Value: list of preferences
    # Make tiebreakers random, also remove bias for lower hash
    g1_items = list(g1.items())
    random.shuffle(g1_items)
    for p1, pref in g1_items:
        
        # Everyone from g1 "proposes" to their first preference
        asked[p1] = 1
        p2 = pref[0].email
        
        if p2 in matches:
            cur_match = matches[p2]
            isMatched[p1] = False
            
            # p2 "trades up"
            if rank_in_pref(p1, g2[p2]) < rank_in_pref(cur_match, g2[p2]):
                matches[p2] = p1
                isMatched[p1] = True
                isMatched[cur_match] = False
        else:
            matches[p2] = p1
            isMatched[p1] = True
        
    # Continue until all people in g2 (the smaller group) are matched
    round_num = 1
    while len(matches) < len(g2):
    
        random.shuffle(g1_items)
        for p1, pref in g1_items:
            
            if isMatched[p1]:
                continue
            
            
            num = asked[p1]
            asked[p1] += 1
            p2 = pref[num].email
            
            if p2 in matches:
                cur_match = matches[p2]
                if rank_in_pref(p1, g2[p2]) < rank_in_pref(cur_match, g2[p2]):
                    matches[p2] = p1
                    isMatched[p1] = True
                    isMatched[cur_match] = False
            else:
                matches[p2] = p1
                isMatched[p1] = True
        round_num += 1

    print(f"Matching concluded after {round_num} rounds")

    return matches        