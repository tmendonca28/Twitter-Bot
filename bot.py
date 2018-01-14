import tweepy
import gspread
import csv
from oauth2client.service_account import ServiceAccountCredentials
from time import sleep

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret1.json', scope)
client = gspread.authorize(creds)

sheet = client.open('twitter-bot').sheet1

index = 2
# authentication data
consumer_key='MXZ3Y3aTPBREpsN9vrB47PV2O'
consumer_secret='Z76L9U6Cggxol6XkTc6ZjNxPGTYLEr14ijS8ZQw6rSYEHCxYoH'
access_token='2485129816-7onWo3oM7mDoayMSQJhkckEHIf8ZPO2PN9tmQFu'
access_token_secret='1sdgQA2fPc3AJRy0VXHok0rJaWJv1QB3s4XeaYmuzFWSJ'
# establishing a connection with the API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# I am targeting accounts with specific hashtags, for instance #mindfulness and a range
# of between 500-1000 followers...limiting items per search to 50
# Query Twitter profile name and number of followers
# Unable to extract email address as Twitter does not export email addresses, you can only access email addresses from
# users that register on your app
for tweet in tweepy.Cursor(api.search,
                           q='#mindfulness',
                           lang='en').items(50):
    if 500 <= tweet.user.followers_count <= 1000:
        print('Twitter Profile Name: @' + tweet.user.screen_name)
        print('Number of followers: ', tweet.user.followers_count)
        print(index)
        values = [tweet.user.screen_name,tweet.user.followers_count]
        sheet.append_row(values)
        index += 1
