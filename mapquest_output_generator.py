#Paiam Moghaddam

import mapquest_api_handler


class TotalDistanceCalc:
    def calculate(self, route_info: dict):
        #calculates and prints the total distance of the trip
        print('TOTAL DISTANCE: ' +  '{:.0f}'.format(float(route_info['route']['distance'])) + ' miles')


class DirectionsCalc:
    def calculate(self, route_info: dict):
        #calculates and prints the individual steps taken each leg of the trip
        print('DIRECTIONS')
        for y in range(len(route_info['route']['legs'])):
            for x in range(len(route_info['route']['legs'][y]['maneuvers'])):
                print(route_info['route']['legs'][y]['maneuvers'][x]['narrative']) 
        

class LatLongsCalc:
    def calculate(self, route_info: dict):
        #calculates and prints the latitude and longitude of each location
        latlngs = []
        for x in range(len(route_info['route']['locations'])):
            latlngs.append((route_info['route']['locations'][x]['latLng']['lat'], route_info['route']['locations'][x]['latLng']['lng']))
        print('LATLONGS')
        for x in latlngs:
            if(x[0] >= 0):
                print('{:.2f}'.format(float(x[0])) + 'N ', end = '')
            else:
                print('{:.2f}'.format(float(x[0]) * -1) + 'S ', end = '')
            if(x[1] >= 0):
                print('{:.2f}'.format(float(x[1])) + 'E')
            else:
                print('{:.2f}'.format(float(x[1]) * -1) + 'W')
            

class TotalTimeCalc:
    def calculate(self, route_info: dict):
        #calculates and prints the total time taken in the trip
        print('TOTAL TIME: ' + '{:.0f}'.format(float(route_info['route']['time']) / 60) + ' minutes')


class ElevationsCalc:
    def calculate(self, route_info: dict):
        #calculates and prints the elevations of each location
        elevation_infos = mapquest_api_handler.generate_elevation_info(route_info)
        print('ELEVATIONS')
        for x in range(len(elevation_infos)):
            for y in range(len(elevation_infos[x]['elevationProfile'])):
                print ('{:.0f}'.format(elevation_infos[x]['elevationProfile'][y]['height']))

        
def calculate_outputs(calcs: ['Output'], route_info: dict):
    #takes a list of outputs and the route info, then calculates the output objects
    outputs = []
    for x in calcs:
        if(x == 'LATLONG'):
            outputs.append(LatLongsCalc())
        if(x == 'STEPS'):
            outputs.append(DirectionsCalc())
        if(x == 'TOTALTIME'):
            outputs.append(TotalTimeCalc())
        if(x == 'TOTALDISTANCE'):
            outputs.append(TotalDistanceCalc())
        if(x == 'ELEVATION'):
            outputs.append(ElevationsCalc())
    for calc in outputs:
        calc.calculate(route_info)
        print('')
        
