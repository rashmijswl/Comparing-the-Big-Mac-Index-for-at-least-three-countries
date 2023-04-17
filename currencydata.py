import urllib.request 
import json
import pygal  # First import pygal
import cprint

data = {"Turkey": [], "Thailand": [], "Taiwan":[]}  #dictionary of list

countries = ["TUR", "THA", "ROC"] #country codes for the three countries I chose for currency api

for country in countries:
  if country == "TUR":
      code = "tur"
      name = "Turkey"
      country = data["Turkey"]
      cur = "try"
  if country == "THA":
      code = "tha"
      name = "Thailand"
      cur = "thb"
      country = data["Thailand"]
  if country == "ROC":
      code = "roc"
      name = "Taiwan"
      country = data["Taiwan"]
      cur = "twd"
  print("Now getting currency data for " + name)
  for value in range(30): #for July 2022
    if value <= 8:
      url = f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/2022-07-0{1+value}/currencies/usd/{cur}.json'
    else:
      url = f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/2022-07-{1+value}/currencies/usd/{cur}.json'
      
  
  
      request = urllib.request.urlopen(url)
      result = json.loads(request.read())
  
      
      country.append(result[cur])

  chart = pygal.Line() #Line Chart for every country
  
  chart.add(f"{name}",country)
  chart.title = f'USD to {code} line chart'
  chart.render_to_file(f'static/images/line_chart_{code}.svg')  #New line chart created for every country beore extracting data for next country






