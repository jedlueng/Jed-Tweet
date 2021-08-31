import tweepy

#authenticator paste 4 of the keys 


""" 
API Key

loTURVelbJA4gAM20x0PyX59b

API Key Secret

vVkB1bmzgZwUlW0ULWNG7oFgCsLcSTiXaVR5CaYG0HcM8nUb5K

Bearer Token

AAAAAAAAAAAAAAAAAAAAAP3pTAEAAAAA8MRWEPXHoubOAy99NDXG7DhNY%2BE%3Db11s1oOI3i3A4woiMhU022yzNSni3moZBnRVrR7Xo5fwCpVXkH

Access Token

1392104701911470081-ZC1CasNzUxhLLT4XQ7nkYGZUWubebD

Access Token Secret

aQMpciMy0eDa9rAscdflv3C7aQMg8RueNT1enXCUXYhFo

"""


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)