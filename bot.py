import slack
import os
from pathlib import Path
from dotenv import load_dotenv
import ssl
import certifi
from slackeventsapi import SlackEventAdapter
from flask import Flask
from slack_bolt import App

from ai import AI
from database_access import sql_query

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# slack_bolt setup
app = App(signing_secret=os.environ['SIGNING_SECRET'],
          token=os.environ['SLACK_TOKEN'])

# API Setup
flask_app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(
    os.environ['SIGNING_SECRET'], '/slack/events', flask_app)

ssl_context = ssl.create_default_context(cafile=certifi.where())
client = slack.WebClient(token=os.environ['SLACK_TOKEN'], ssl=ssl_context)
BOT_ID = client.api_call('auth.test')['user_id']

ai = AI(sql_query)

# On user message, return a message from the bot
@slack_event_adapter.on('message')
def message(payload):
    print('payload received')
    event = payload.get('event', {})
    channel = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')

    if user_id != BOT_ID:
        try:
            response = ai.run(text)
            client.chat_postMessage(channel=channel, text=response)
        except Exception as e:
            response = "I'm sorry, I had a tough time answering that question. Please ask me something else!"
            client.chat_postMessage(channel=channel, text=response)
            print(e)

if __name__ == '__main__':
    flask_app.run(debug=True, port=8000)