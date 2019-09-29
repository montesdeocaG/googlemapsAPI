import googlemaps
import requests
import json
import pandas as pd
gmaps = googlemaps.Client(key='"*APISTRING*"')

def problemA():
###Description:
    #This function uses python googlemaps library and gets nearby searches of the UPY type restaurant
###Parameters:
    
###Returns:
    #A pandas dataframe
    pythmod = gmaps.places_nearby(location = '20.988459, -89.736768', radius = 2000, type = 'restaurant')
    df = pd.read_json(json.dumps(pythmod['results']), orient='columns')
    df = df[['name', 'id', 'rating', 'types', 'user_ratings_total']]
    return df

def problemB(string,lat,lon):
###Description:
    #this function uses python googlemaps library and returns the id given a string name and coordenates
###Parameters: 
    #string: place name string
    #lat: latitude
    #lon: longitude
###Returns:
    #A string
    return gmaps.find_place(input = string, input_type = 'textquery', location_bias = 'point:{}, {}'.format(lat,lon))['candidates'][0]['place_id']
problemB('Chalmuch',20.988459,-89.736768)

#ProblemC
problemB("McCarthy's Irish Pub - Caucel",20.999916,-89.682617)
problemB('Starbucks',20.984958,-89.618152)
problemB('Los Trompos',20.998694,-89.6175974)

def problemD(placeid):
###Description:
    #this function uses python googlemaps library and returns a dataframe with reviews in english and spanish.
###Parameters: 
    #placeid: place id string, example: 'ChIJaUUfylFxVo8RgEGjoansPbc'
###Returns:
    #A dataframe    
    data = gmaps.place(place_id = placeid, fields = ['review'], language = 'en, es')
    df = pd.DataFrame(data['result']['reviews'])
    df['time'] = pd.to_datetime(df['time'],unit='s')
    df = df[['author_name','language','rating','time','text']]
    return df

def problemE():
###Description:
    #this function uses python googlemaps library and returns a dataframe with similar restaurants ranked that are close to los trompos restaurant.
###Parameters: 

###Returns:
    #A dataframe       
    tromposdata = gmaps.places_nearby(location = '20.998694, -89.6175974', radius =  300, type = 'restaurant', rank_by = 'prominence')
    df = pd.DataFrame(tromposdata['results'])
    df = df.sort_values('rating',ascending=False).reset_index(drop=False)
    df = df[['id', 'name', 'rating', 'user_ratings_total']]
    return df