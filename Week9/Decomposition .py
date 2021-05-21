# Example: Similar Restaurants

def search(query, ranking=lambda r: -r.stars):
    results = [r for r in Restaurant.all if query in r.name]
    return sorted(results, key=ranking)

# Set Intersection

def fast_overlap(s, t):   #take Linear time
    """Return the overlap between sorted S and sorted T.
    >>> fast_overlap([3, 4, 6, 7, 9, 10], [1, 3, 5, 7, 8])
    2
    """
    i, j, count = 0, 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            count, i, j = count + 1, i + 1, j + 1
        elif s[i] < t[j]:
            i += 1
        else:
            j += 1
    return count

def reviewd_both(r, s):
    #return len([x for x in r.reviewers if x in s.reviewers])  #too slow
    return fast_overlap(r.reviewers, s.reviewers)

class Restaurant:
    all = []
    def __init__(self, name, stars, reviewers):
        self.name, self.stars = name, stars
        self.reviewers = reviewers
        Restaurant.all.append(self)
    
    def similar(self, k, similarity):
        "Return the K most similar restaurants to SELF, using Similarity for comparsion."
        others = list(Restaurant.all)
        others.remove(self)
        return sorted(others, key=lambda r: -similarity(self, r))[:k]
    
    def __repr__(self):
        return '<' + self.name + '>'

import json

reviewers_for_restaurant = {}
for line in open('reviews.json'):
    r = json.loads(line)
    biz = r['business_id']
    if biz not in reviewers_for_restaurant:
        reviewers_for_restaurant[biz] = [r['user_id']]
    else:
        reviewers_for_restaurant[biz].append(r['user_id'])

for line in open('restaurant.json'):  #JavaScript object notation
    r = json.loads(line)
    reviewers = reviewers_for_restaurant[r['business_id']]
    Restaurant(r['name'], r['stars'], sorted(reviewers))

while True:
    print('>', end = ' ')
    results = search(input().strip())
    for r in results:
        print(r, 'shares reviewers with', r.similar(3))