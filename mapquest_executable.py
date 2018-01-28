#Paiam Moghaddam
import mapquest_api_handler
import mapquest_output_generator
import sys

def _create_location_list()->list:
    #generates the list of locations for the trip
    locations = []
    inp = input().strip()
    for x in range (int(inp)):
        locations.append(input())
    return locations


def _create_output_list()->list:
    #generates the list of desired outputs for the trip
    outputs = []
    inp = input().strip()
    for x in range(int(inp)):
        outputs.append(input())
    return outputs
        
    
def user_interface():
    #handles the main interaction between the client and the program
    #also checks if the location input for the trip is feasible
    locations = _create_location_list()
    outputs = _create_output_list()
    #print()
    url = mapquest_api_handler.generate_url_route(locations)
    response = mapquest_api_handler.get_route_info(url)
    if(response['info']['messages'] == ['We are unable to route with the given locations.']):
        print ('NO ROUTE FOUND')
        sys.exit()
    mapquest_output_generator.calculate_outputs(outputs, response)
    print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')
    

if __name__=='__main__':
    #iniates the program by calling on the user interface
    user_interface()  
