import ssl, certifi
ssl._create_default_https_context = lambda *args, **kwargs: ssl.create_default_context(cafile=certifi.where())
import flask
import slack
import os
import pathlib
from pathlib import Path
from dotenv import load_dotenv
from slackeventsapi import SlackEventAdapter


env_path = Path('..') / '.env'
load_dotenv(dotenv_path=env_path)
app = flask.Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.getenv("SIGNING_TOKEN"), '/slack/events', app)
client = slack.WebClient(token=os.getenv("SLACK_TOKEN"))

client.chat_postMessage(channel="#a-space-mans-journey", text="Good morning yall!")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run("0.0.0.0", port=port)