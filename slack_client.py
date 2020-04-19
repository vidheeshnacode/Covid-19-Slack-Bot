import requests
import json
import logging

DEFAULT_SLACK_WEBHOOK = 'https://hooks.slack.com/services/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'

HEADERS = {
    'Content-type': 'application/json'
}


def slacker(webhook_url=DEFAULT_SLACK_WEBHOOK):
    def slackit(msg):
        logging.info('Sending {msg} to slack'.format(msg=msg))
        payload = { 'text': msg }
        return requests.post(webhook_url, headers=HEADERS, data=json.dumps(payload))
    return slackit
