import csv

with open('data-398-2016-11-07.csv', 'r', encoding='cp1251') as f:
    fields = ["system_object_id", "global_id", "Name", "Longitude_WGS84", "Latitude_WGS84", "Street",
              "AdmArea", "District", "RouteNumbers", "OperatingOrgName", "EntryState",
              "Pavilion", "Direction", "ID", "StationName", "geoData"]
    reader = csv.DictReader(f, fields, delimiter=';')
    stations = set()
    streets = {}
    for row in reader:
        stations.add(row['StationName'])
        if row['Street'] in streets:
            streets[row['Street']] += 1
        else:
            streets[row['Street']] = 1
    print('Колличесвто остановок: ' + str(len(stations)))

    maximum = max(streets, key=streets.get)
    print(maximum, streets[maximum])
