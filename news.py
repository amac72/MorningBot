import requests
import json
import os
from dotenv import load_dotenv
from datetime import date

current_date = str(date.today())

load_dotenv()
# In the ".env" file, this is the token from the news API
NEWS = os.getenv('NEWS')

def get_news(category):
    # Sends and gets requests, returns in JSON format
    response = requests.get(f'https://newsapi.org/v2/everything?q={category}&from={current_date}&sortBy=popularity&apiKey={NEWS}')
    info = response.text

    # Gets headline from JSON
    news = json.loads(str(info))
    articles = news["articles"]
    source = articles[0]["source"]["name"]
    headline = articles[0]["title"]

    message = f"Here's some {category} news from {source}: {headline}"

    return(message)