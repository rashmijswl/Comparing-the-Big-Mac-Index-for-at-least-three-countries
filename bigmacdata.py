import nasdaqdatalink
import pandas as pd
import json
import urllib.request

nasdaqdatalink.ApiConfig.api_key = "wrHvFnxKjo3Bgzx_LdzA"
def get_data():
    nasdaqdatalink.ApiConfig.api_key = 'wrHvFnxKjo3Bgzx_LdzA'
    countries = ["TUR", "THA", "ROC"]
    data_list = []

    for country in countries:
        print("Now getting Big Mac data for ", {country})
        data = nasdaqdatalink.get(f'ECONOMIST/BIGMAC_{country}',
                                  start_date='2022-07-01',
                                  end_date='2022-07-31')
        if country == "TUR":
            country = "Turkey"
        if country == "THA":
            country = "Thailand"
        if country == "ROC":
            country = "Taiwan"

        country = {
            "country": country,
            "local_price": data.iloc[0, 0],
            "dollar_ex": data.iloc[0, 1],
            "dollar_price": data.iloc[0, 2],
            "dollar_ppp": data.iloc[0, 3],
            "dollar_valuation": data.iloc[0, 4],
            "dollar_adj_valuation": data.iloc[0, 5],
        }

        data_list.append(country)
    return data_list