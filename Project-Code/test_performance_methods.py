import pickle
from file_path_converter import convert_path
from team_rating_calculator import calculate_rating

pi = True

save_path = 'C:\\Users\\rhyde23\\Desktop\\SoccerManager\\Saves\\File1.dat'

if pi :
    save_path = convert_path(save_path)


save = pickle.load(open(save_path, 'rb'))

def test() :
    arsenal_formation = save['Arsenal_Formation']
    arsenal_players = save['Arsenal_Players']
    arsenal_lineup = save['Arsenal_Lineup']

    aston_villa_formation = save['Aston Villa_Formation']
    aston_villa_players = save['Aston Villa_Players']
    aston_villa_lineup = save['Aston Villa_Lineup']
    

    #Now we actually start testing the functionality

    
    arsenal_rating = calculate_rating(arsenal_players, arsenal_lineup, arsenal_formation)
    
    print(arsenal_rating, 'arsenal rating')

    aston_villa_rating = calculate_rating(aston_villa_players, aston_villa_lineup, aston_villa_formation)
    
    print(aston_villa_rating, 'villa rating')




test()
