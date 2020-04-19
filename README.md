# Covid-19-Slack-Bot

Implementing this project will create a bot on slack which provides live notifiation of Covid-19 cases in each state of India.
This Slack bot is implemented in Python using beautifulsoup and Slack api. 
The information is fetched from The Ministry of Health and Family Welfare website (mohfw.gov.in)

Prerequisites are the following
dependencies: tabulate, beautifulsoup, requests
slack account and slack webhook (Follow steps from api.slack.com/messaging/webhooks)

replace your slack webhook in slack_client.py in 'YOUR WEBHOOK'


The above program works and updated for the current (19th April 2020) layout of the webiste from which the data is fetched. 
If error occurs refer to bot.log file to find the problem and modify the program accordingly. 

Cheerio!
