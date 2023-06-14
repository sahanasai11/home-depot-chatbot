# home-depot-chatbot
A chatbot built using the Slack API and Open AI API that answers questions about products available on Home
Depot's website.

Setup:
- Create virtual environment: `python -m venv /path/to/new/virtual/environment`
- Navigate to directory containing `venv`, and enter `source venv/bin/activate`
- Create a `.env` file and input your Slack token, Signing Secret, and Open AI API key:
- Install dependencies: `pip install -r requirements.txt`
- Start Flask server: 
    - `export FLASK_APP=bot`
    - `flask run -h localhost -p 8000` ()
- Download and go to ngrok application
    - `ngrok http 8000`
    - Copy the link next to forwarding- i.e. https://xxxx.ngrok.io
    - Go to event subscriptions on slack api: https://api.slack.com/apps/A05CWK2PG8G/event-subscriptions?
    - Press "change" and paste the copied link from ngrok and append `slack/events` i.e. https://xxxx.ngrok.io/slack/events
    - Select save changes
- Type in slack workspace that the bot exists in and you're good to go!
