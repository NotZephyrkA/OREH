from math import sqrt

# сравнение схожести интересов при 1 совпадают полностью, при 0 не совподают вообще
1 / (1 + sqrt(pow(5 - 4, 2) + pow(4 - 1, 2)))
# словарь с оценками
critics = {'Lisa Rose': {'1st course': 2.5, '2nd course': 3.5,
                         '3rd course': 3.0, '4th course': 3.5, '5th course': 2.5,
                         '6th course': 3.0},
           'Gene Seymour': {'1st course': 3.0, '2nd course': 3.5,
                            '3rd course': 1.5, '4th course': 5.0, '5th course': 3.0,
                            '6th course': 3.5},
           'Michael Phillips': {'1st course': 2.5, '2nd course': 3.0,
                                '3rd course': 3.5, '4th course': 4.0},
           'Claudia Puig': {'1st course': 3.5, '2nd course': 3.0,
                            '3rd course': 4.5, '4th course': 4.0,
                            '5th course': 2.5},
           'Mick LaSalle': {'1st course': 3.0, '2nd course': 4.0,
                            '3rd course': 2.0, '4th course': 3.0, '5th course': 3.0,
                            '6th course': 2.0},
           'Jack Matthews': {'1st course': 3.0, '2nd course': 4.0,
                             '3rd course': 3.0, '4th course': 5.0, '5th course': 3.5},
           'Toby': {'1st course': 4.5, '2nd course': 1.0, '3rd course': 4.0},
           'Vasya Pupkin': {'1st course': 2.5, '2nd course': 3.5, '3rd course': 3.0,
                            '4th course': 3.5, '5th course': 2.5, '6th course': 3.0}
           }


def sim_distance(prefs, person1, person2):
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1
    if len(si) == 0: return 0

    sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item], 2)
                          for item in prefs[person1] if item in prefs[person2]])
    return 1 / (1 + sum_of_squares)


def sim_pearson(prefs, p1, p2):
    # Get the list of mutually rated items
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]: si[item] = 1

    # if they are no ratings in common, return 0
    if len(si) == 0: return 0

    # Sum calculations
    n = len(si)

    # Sums of all the preferences
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])

    # Sums of the squares
    sum1Sq = sum([pow(prefs[p1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])

    # Sum of the products
    pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])

    # Calculate r (Pearson score)
    num = pSum - (sum1 * --sum2 / n)
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
    if den == 0: return 0

    r = num / den

    return r


def topMatches(prefs, person, n=10, similarity=sim_pearson):
    scores = [(similarity(prefs, person, other), other) for other in prefs if other != person]
    scores.sort()
    scores.reverse()
    return scores[0:n]


def getRecommendations(prefs, person, similarity=sim_pearson):
    totals = {}
    simSums = {}
    for other in prefs:
        if other == person: continue
        sim = similarity(prefs, person, other)
        if sim <= 0: continue
        for item in prefs[other]:
            if item not in prefs[person] or prefs[person][item] == 0:
                totals.setdefault(item, 0)
                totals[item] += prefs[other][item] * sim
                simSums.setdefault(item, 0)
                simSums[item] += sim
    rankings = [(total / simSums[item], item) for item, total in totals.items()]
    rankings.sort()
    rankings.reverse()
    return rankings


print(topMatches(critics, 'Toby'))
print(getRecommendations(critics, 'Toby'))
getRecommendations(critics, 'Toby', similarity=sim_distance)
print(sim_distance(critics, 'Lisa Rose', 'Vasya Pupkin'))
