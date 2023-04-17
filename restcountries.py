import urllib.request 
import json
import pandas as pd


data_list = []
countries = ["thailand", "taiwan", "turkey"]
def get_data():
  for country in countries:
      url = f'https://restcountries.com/v3.1/name/{country}'
      request = urllib.request.urlopen(url)
      result = json.loads(request.read())
      con = country
      con ={
        "flag" : result[0]["flag"],
      "population" : result[0]["population"],
      "latitude": result[0]["latlng"][0],
      "longitude" :result[0]["latlng"][1],
        "map_g": result[0]["maps"]["googleMaps"],
        "map_o": result[0]["maps"]["openStreetMaps"]
      }
      data_list.append(con)
    
  
  df = pd.DataFrame(data_list)
  dfg = df.groupby(['flag','population','latitude', 'longitude','map_g','map_o'])
  df.to_html('templates/result.html')
  return data_list