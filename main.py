from tweepy.auth import OAuthHandler, OAuth2UserHandler, HTTPBasicAuth
from tweepy.api import API
from tweepy.client import Client
from cred import *

from telegram import Update
from telegram.ext import ContextTypes
from telegram.ext import filters, MessageHandler, ApplicationBuilder



    
async def listen(update: Update, context: ContextTypes):
    tweet = update.channel_post.text
    
    thisclient = Client(bearer_token=bearer,consumer_key=key,consumer_secret=key_secret,access_token=token,access_token_secret=token_secret)

    thisclient.create_tweet(text=tweet)
    
    # # get all tweets with the word "forex" in the last 7 days
    # tweets = thisclient.search_recent_tweets(query="forex",max_results=1,sort_order="recent")
    
    # # for all the tweets follow the users
    # for tweet in tweets:
    #     thisclient.follow_user(tweet.author_id)
    #     print(tweet.author_id)
    
    
    # #update.message.reply_text('Hello World!')
    

if __name__ == '__main__':
    app = ApplicationBuilder().token(telegram_token).build()
    
    listener = MessageHandler(filters.TEXT, listen)
    app.add_handler(listener)
    
    app.run_polling()


