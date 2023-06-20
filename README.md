# home-depot-chatbot
This repository contains a case study of the use of Large Language Models to serve as a customer service
chatbot based off of Home Depot's website using the Langchain framework, Slack API, and Open AI API. The langchain
agent used is a database agent that can perform SQL queries on any database. For the purpose of this project,
a SQLite database is created containing data regarding Home Depot product information.

Skills:
- Flask
- Python
- API's
- Selenium
- Pandas
- Langchain

Setup:
- Create virtual environment: `python -m venv /path/to/new/virtual/environment`
- Navigate to directory containing `venv`, and enter `source venv/bin/activate`
- Create a `.env` file and input your Slack token, Signing Secret, and Open AI API key- refer to (https://api.slack.com/apis):
    - `SLACK_TOKEN=...`
    - `SIGNING_SECRET=...`
    - `OPEN_AI_API_KEY=...`

- Install dependencies: `pip install -r requirements.txt`
- Start Flask server: 
    - `export FLASK_APP=bot`
    - `flask run -h localhost -p 8000`
- Download ngrok: https://ngrok.com/ and open the ngrok application
    - Enter `ngrok http 8000`
    - Copy the link next to forwarding- i.e. https://xxxx.ngrok.io
    - Go to event subscriptions on slack api: https://api.slack.com/apps/A05CWK2PG8G/event-subscriptions?
    - Press "change" and paste the copied link from ngrok and append `slack/events` i.e. https://xxxx.ngrok.io/slack/events
    - Select save changes

Type in slack workspace: https://app.slack.com/client/T05BRR7MN0P/C05C6S2E32P and you're good to go!
