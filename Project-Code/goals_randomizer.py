import random

tiers = [
    ['ST', 'LW', 'RW', 'CF', 'RF', 'LF'],
    ['CAM', 'RM', 'LM'],
    ['CM', 'CDM'],
    ['RB', 'RWB', 'LB', 'LWB']
]

chances = [
    85,
    25,
    10,
    5
]


def get_losing_team_score() :
    losing_randomization = random.randint(1, 100)
    if losing_randomization >= 80 :
        return 2
    return random.randint(0, 1)

def randomize_goals(dict_keys) :
    while True :
        for position in dict_keys :
            for i, tier in enumerate(tiers) :
                if position in tier :
                    chance = chances[i]
                    break
            randomized = random.randint(1, 100)
            if randomized <= chance :
                return position

def randomize_goals(team1, team2, winning_team, difference_in_score) :
    losing_score = get_losing_team_score()
    winning_score = losing_score+difference_in_score
    if team1 == winning_team :
        winning_dict = team1
        losing_dict = team2
    else :
        winning_dict = team2
        losing_dict = team1
    winning_dict_keys = random.shuffle(list(winning_dict.keys()))
    losing_dict_keys = random.shuffle(list(losing_dict.keys()))
    winning_scorers, losing_scorers = [], []
    for i in range(winning_score) :
        winning_scorers.append(randomize_goals(winning_dict_keys))
    for i in range(losing_score) :
        losing_scorers.append(randomize_goals(losing_dict_keys))
    if team1 == winning_team :
        score = '-'.join([str(winning_score), str(losing_score)])
        team1_scorers = [team1[position]['Name'] for position in winning_scorers]
        team2_scorers = [team2[position]['Name'] for position in losing_scorers]
    else :
        score = '-'.join([str(losing_score), str(winning_score)])
        team1_scorers = [team1[position]['Name'] for position in losing_scorers]
        team2_scorers = [team2[position]['Name'] for position in winning_scorers]
    return score, team1_scorers, team2_scorers
            
