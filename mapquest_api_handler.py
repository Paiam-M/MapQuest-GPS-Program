#Paiam Moghaddam

import json
import urllib.request
import urllib.parse
import sys

MAPQUEST_API_KEY = 'CT1FhqDvreG0RFqVhMVtWMeB2fsno5lq'

MAPQUEST_BASE_URL_ROUTE = 'http://open.mapquestapi.com/directions/v2/route?'

MAPQUEST_BASE_URL_ELEVATION = 'http://open.mapquestapi.com/elevation/v1/profile?'


def generate_url_route(locations: list)->str:
    #given a series of locations, generates the url of the general route information
    num_locations = len(locations)
    query_parameters = [('key', MAPQUEST_API_KEY), ('from', locations[0])]
    for x in range(num_locations - 1):
        query_parameters.append(('to', locations[x + 1]))
    url = MAPQUEST_BASE_URL_ROUTE + urllib.parse.urlencode(query_parameters)
    return url


def generate_elevation_info(route_info: dict)->list:
    #given the route information, creates a list of elevation informations for each location
    #used to find the elevation of each location without causing an error in MapQuest
    elevation_infos = []
    for x in range(len(route_info['route']['locations'])):
        latlngs = str(route_info['route']['locations'][x]['latLng']['lat']) + ',' + str(route_info['route']['locations'][x]['latLng']['lng'])
        query_parameters = [('key', MAPQUEST_API_KEY), ('latLngCollection', latlngs), ('unit', 'f')]
        url = MAPQUEST_BASE_URL_ELEVATION + urllib.parse.urlencode(query_parameters)
        #print(url)
        elevation_infos.append(get_route_info(url))
    return elevation_infos


def get_route_info(url: str)->dict:
    #given a url, opens up the url and returns the response in the form of a dictionary
    #also handles errors invovling communication with MapQuest
    response = None
    flag = False
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        results = json.loads(json_text)
        print()         
        return results
    except:
        if(not flag):
            print ('MAPQUEST ERROR')
            sys.exit()
    finally:
        if response != None:
            response.close()
