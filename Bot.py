# Importing Packages

import tweepy
import requests
from bs4 import BeautifulSoup

# Importing Module

import simple_colors

# Setup Client API

api_key = "" # Enter Your API KEY
api_s_key = "" # Enter your API Secret Key
access_token = ""
access_token_s = ""


# Authentication
auth = tweepy.OAuthHandler(api_key, api_s_key)
auth.set_access_token(access_token, access_token_s)
client = tweepy.API(auth)

# Connection Checking
try:
    client.verify_credentials()
    print(simple_colors.cyan('Authentication OK', 'italic'))

except tweepy.TweepError as e:
    print(simple_colors.red(f'Error during authentication due to {e}', 'bold', 'italic'))

# Links and Methods to Fetch News 
_news_ = "https://www.bbc.com/business"
response = requests.get(_news_)
soup = BeautifulSoup(response.text, 'html.parser')

## Fetching the News
article = soup.find('h2', class_="sc-4fedabc7-3 bvDsJq")
if article:
    headline = article.text
    desc = article.find_next("p", class_="sc-ae29827d-0 cNPpME").text

    ### Tweet Format
    tweet = headline + " - " + desc + " #business #world #startups #businessnews"

    ### Output
    print("\n")
    print(simple_colors.blue('The "Headline" of the following Article is'))
    print("\n")
    print(simple_colors.red(headline))
    print("\n")
    print(simple_colors.blue('The following Article is'))
    print("\n")
    print(desc)
    print("\n")

    ### Tweet uploading on the twitter
    '''
    print(tweet)
    client.update_status(status=tweet)
    '''
else:
    print("No article found. Check if the class name or webpage structure has changed.")
