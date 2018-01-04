#My Name: Samuel Monnat

def generate_pokemon(names,powers):
    """ randomly creates and returns pokemon dictionary based on provided names and powers. Assigns random level to each. """
    return {'name': names[random.randint(0,len(names)-1)],'power': powers[random.randint(0,len(powers)-1)], 'level': random.randint(1,10)}


def get_level(ditto):
    """ Calculates and returns the level of the ditto """
    count = ditto['count'] + 1 #adds one to the given count to include your "ditto" in the calculation
    sum_level = sum(ditto['level']) #sums the levels in the ditto level list
    return float(sum_level/count)

def should_absorb(ditto,pokemon):
    """ Ditto will only absorb if it will increase its level, returns True/False """
    if get_level(ditto) > pokemon['level']:
        return False
    else:
        return True

def absorb(ditto,pokemon):
    """ adds absorbed information to ditto """
    ditto['count'] += 1 #increments count when absorbed
    ditto['power'].append(pokemon['power']) #adds power to ditto's power list
    ditto['level'].append(pokemon['level']) #adds level to ditto's level list

def take_walk(poke_list):
    """ Iterates through list of given pokemon and calls the should_absorb function to determine if it should be absorbed. If true, then uses absorb to add its information to the ditto_dict. """
    ditto_dict = {'count': 0, 'power': ['absorb'], 'level': [1]}
    for pokemon in poke_list:
        if should_absorb(ditto_dict,pokemon) == True: #to absorb pokemon who will increase Ditto's level
            absorb(ditto_dict,pokemon)
        if should_absorb(ditto_dict,pokemon) == False:
            if not (pokemon['power'] in ditto_dict['power']):  #to absorb pokemon with power not yet present in ditto
                absorb(ditto_dict,pokemon)

    return ditto_dict
