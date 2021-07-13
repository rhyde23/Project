import random

#Passes in two team ratings

difference_dictionary = {
    1:53,
    2:56,
    3:59,
    4:62,
    5:65,
    6:68,
    7:71,
    8:74,
    9:77,
    10:81,
    11:84,
    12:87,
    13:90,
    14:93,
    15:96,
    16:99,
}

def get_goal_difference(randomization_difference) :
    if randomization_difference > 80 :
        return random.randint(4, 5)
    if randomization_difference > 60 :
        return random.randint(3, 4)
    if randomization_difference > 40 :
        return random.randint(2, 3)
    if randomization_difference > 20 :
        return random.randint(1, 2)
    return random.randint(1, 2)
    


def match_sim(team1, team2, team1_name, team2_name) :
    randomized = random.randint(1, 100)
    change_factors = random.randint(1, 5)
    if team1 > team2 :
        better_team, better_team_name, worse_team, worse_team_name = team1, team1_name, team2, team2_name
    elif team2 > team1 :
        better_team, better_team_name, worse_team, worse_team_name = team2, team2_name, team1, team1_name
    else :
        if randomized > 45 and randomized < 55 :
            return 'Draw', 0
        if randomized >= 55 :
            return team2_name, get_goal_difference(100-randomized) 
        else :
            return team1_name, get_goal_difference(randomized) 
    try :
        target = difference_dictionary[better_team-worse_team]-change_factors
        if randomized > target :
            return worse_team_name, get_goal_difference(randomized-target) 
        return better_team_name, get_goal_difference(target-randomized) 
    except :
        return better_team_name, random.randint(2, 5)
        
        
"""
team1, team2, team1_name, team2_name = 75, 85, 'Burnley', 'Chelsea'
team1, team2, team1_name, team2_name = 78, 74, 'Brighton', 'Sheffield'
team1, team2, team1_name, team2_name = 90, 76, 'Barcelona', 'Newcastle'
n = 0
for i in range(200) :
    r = match_sim(team1, team2, team1_name, team2_name)
    if r[0] == 'Newcastle' :
        n += 1

print(n)
"""
        