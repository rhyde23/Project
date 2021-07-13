formations = {
    '4-2-3-1 (Wide)':['GK', 'RB', 'RCB', 'LCB', 'LB', 'RDM', 'LDM', 'RM', 'LM', 'CAM', 'ST'],
    '5-2-3-1 (Attacking)':['GK', 'RWB', 'RCB', 'CB', 'LCB', 'LWB', 'RCM', 'LCM', 'CAM', 'RS', 'LS'],
    '4-4-2 (Flat)':['GK', 'RB', 'RCB', 'LCB', 'LB', 'RM', 'RCM', 'LCM', 'LM', 'RS', 'LS'],
    '5-2-3 (Flat)':['GK', 'RWB', 'RCB', 'CB', 'LCB', 'LWB', 'RCM', 'LCM', 'RW', 'ST', 'LW'],
    '4-3-3 (Defensive)':['GK', 'RB', 'RCB', 'LCB', 'LB', 'CDM', 'RCM', 'LCM', 'RW', 'ST', 'LW'],
    '4-5-1 (Defensive)':['GK', 'RB', 'RCB', 'LCB', 'LB', 'CDM', 'RM', 'RCM', 'LCM', 'LM', 'ST'],
    '4-3-3 (False 9)':['GK', 'RB', 'RCB', 'LCB', 'LB', 'CDM', 'RCM', 'LCM', 'CF', 'RW', 'LW'],
    '5-3-2 (Flat)':['GK', 'RWB', 'RCB', 'CB', 'LCB', 'LWB', 'RCM', 'CM', 'LCM', 'RS', 'LS'],
    '4-3-3 (Flat)':['GK', 'RB', 'RCB', 'LCB', 'LB', 'RCM', 'CM', 'LCM', 'RW', 'ST', 'LW'],
    '4-3-3 (Attacking)':['GK', 'RB', 'RCB', 'LCB', 'LB', 'RCM', 'LCM', 'CAM', 'RW', 'ST', 'LW'],
    '4-2-3-1 (Narrow)':['GK', 'RB', 'RCB', 'LCB', 'LB', 'RDM', 'LDM', 'RAM', 'CAM', 'LAM', 'ST'],
    '4-1-2-1-2 (Narrow)':['GK', 'RB', 'RCB', 'LCB', 'LB', 'CDM', 'LCM', 'RCM', 'CAM', 'LS', 'RS'],
}

def get_positions_from_formation(formation) :
    return formations[formation]