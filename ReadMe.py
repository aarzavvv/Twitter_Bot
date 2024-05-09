# Importing Packages
"""
tweepy          : Provides interface for accessing Twitter's API
requests        : For making HTTP requests
BeautifulSoup   : Scrape information from web pages"""

# Importing Module
"""
simple_colors   : Allows user to use colors in the terminal"""

# Setup Client API
"""
api_key = "Enter Your API KEY"
api_s_key = "Enter your API Secret Key"
access_token = "Enter the Access Token"
access_token_s = "Enter Secret Access Token"
"""

# Authentication
""" Using the provided keys and tokens for authentication. It also creates
    a 'tweepy.API' instane ('client'), which can be used to interact with
    Twitter API """

# Connection Checking
""" Here, we are checking the credentials by calling 'verify_credentials()'
    method of 'client' object, with printing messages for confirmation  """





# Links and Methods to Fetch News 
""" '_news' points to the BBC's Business news page
    'requests.get()' retrieves HTML content of the page and creates a 'soup'
    to analyze the HTML """

## Fetching the News
""" Finding the first '<h2>' element with a specific class 'sc-ae29827d-0 cNPpME'
    and retrieves the text as headline 'headline'. Then finds '<p>' for retrieving
    text as description 'desc' """


### Tweet Format
""" 'tweet' concatenates the 'headline' and 'desc' with some related hashtags
    Then prints hadline and description in the terminal with some formatting
    of 'simple_colors' module for visual clarity """










### Tweet uploading on the twitter
""" This commented part in the code is actually used to post the data on the
    Twitter Account """


""" If no article is found then, the code will print the 'else' block in the
    terminal """

"""    In the terminal, type the following command to run the code 'python .\Bot.py'
        Also make sure that you open the terminal with the exact folder, where you saved 
        the bot.    """
