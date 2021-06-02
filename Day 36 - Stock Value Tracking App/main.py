cls = lambda: print("\033[2J\033[;H", end='')
cls()

import requests
import datetime as dt
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
"""
Day 36 - Stock news project
"""

STOCK = "GOOG"
COMPANY_NAME = "Google"
account_sid = "ACCOUNT_SID"
auth_token = "AUTH_TOKEN"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_parameters = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK,
    "interval": "60min",
    "outputsize": "compact",
    "apikey": "KOVDRJV4YL8RSHB1"
    }

stock_endpoint = requests.get("https://www.alphavantage.co/query", params=stock_parameters)
stock_endpoint.raise_for_status()
google_stock_data = stock_endpoint.json()

t = dt.datetime.now()
time = t.time().hour
weekday = t.weekday()

def process_data(data:dict, yesterday:str, before_yesterday:str) -> int:
    """
    

    Parameters
    ----------
    data : dict
        Input of the stock data of the selected company in JSON format.
    yesterday : str
        Yesterday's date.
    before_yesterday : str
        Before yesterday's date.

    Returns
    -------
    int
        Returns the percentage of change of the closing value of the stocks between yesterday and before yesterday.

    """
    key1 = "Time Series (60min)"
    key2 = "4. close"
    data_1 = float(data[key1][yesterday][key2])
    data_2 = float(data[key1][before_yesterday][key2])
    delta = round(((data_1-data_2)/data_2)*100, 2)
    print(f"Closing value on {yesterday}: {data_1}\nClosing value on {before_yesterday}: {data_2}\nDelta: {delta}%")
    return delta

def get_news(query=COMPANY_NAME, country="us") -> list:
    
    """
    Parameters
    ----------
    query : str, optional
        Keyword for the API to search. The default is COMPANY_NAME.
        
    country : str, optional
        ISO code of the country to search news. The default is "us".

    Returns
    -------
    headlines: list
        3 most important headlines for the input query.

    """
    news_parameters = {
        "q": query,
        "apiKey": "8b25aad12c404ae9b36ea69e675fcf84",
        "category": "business",
        "country": country,
        "pageSize": 3,    
        }
    
    news_endpoint = requests.get("https://newsapi.org/v2/top-headlines?", params=news_parameters)
    news_endpoint.raise_for_status()
    news = news_endpoint.json()["articles"]
    headlines = []
    for title in news:
        headlines.append(title["title"]) 
    return headlines
        
# Executing the task each time it is noon. It skips Sunday and Monday as stock exchange does not operate on weekends
if weekday == 0 or weekday == 6:
    pass
else:        
    today = str(t).split(" ")[0] + " " + "12:00:00"
    if weekday == 0:
        yesterday = str(t - dt.timedelta(3)).split(" ")[0] + " " + "12:00:00"
        byesterday = str(t - dt.timedelta(4)).split(" ")[0] + " " + "12:00:00"
    elif weekday == 1:
        yesterday = str(t - dt.timedelta(1)).split(" ")[0] + " " + "12:00:00"
        byesterday = str(t - dt.timedelta(4)).split(" ")[0] + " " + "12:00:00"
    else:
        yesterday = str(t - dt.timedelta(1)).split(" ")[0] + " " + "12:00:00"
        byesterday = str(t - dt.timedelta(2)).split(" ")[0] + " " + "12:00:00"
    
    # delta = process_data(google_stock_data, yesterday, byesterday)
    delta = 6
    if delta > 5 or delta < -5:
        headlines = get_news()
        
        msg=f"""
        A big change in the stock market of {COMPANY_NAME} was detected: {delta}%
            
        Here are the top 3 most relevant headlines on american news:
                
        1. {headlines[0]}
        2. {headlines[1]}
        3. {headlines[2]}
        """
        client = Client(account_sid, auth_token)
    
        message = client.messages \
                    .create(
                         body=msg,
                         from_='+18168009281',
                         to='+573203204915'
                 )
        print(message.status)


