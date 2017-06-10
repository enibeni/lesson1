import json
from pprint import pprint

with open('data-397-2016-11-24.json', 'r', encoding='cp1251') as f:
    data = json.load(f)    # type - list
    stations = set()
    for station in data:    # type - dict
        if station['RepairOfEscalators']:
            stations.add('На станции метро ' + station['NameOfStation'] + ' идет ремонт экскалаторов!')
    pprint(stations)

