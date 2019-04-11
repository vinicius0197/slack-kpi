from slackclient import SlackClient
import time
import yaml
# "* {} :* \n {}".format(key, value)

# slack_token = os.environ["SLACK_API_TOKEN"]
# Auth for Slack API
with open('config.yml') as f:
    config = yaml.safe_load(f)

sc = SlackClient(config["slack_token"])


def build_message(dictionary):
    return [{
        "type": "mrkdwn",
        "text": "*" + key + ":* \n" + value
    } for key, value in dictionary.items()
    ]


def send_message(message):
  # Use Slack API to send messege to channel
    return sc.api_call(
        "chat.postMessage",
        channel="CH18469GS",
        blocks=[
            {
                "type": "section",
                "fields": message
            }
        ]
    )


def task_slack_message(dictionary):
    """
    Connects to Google Drive and Slack API and sends message at
    given intervals.
    """
    # build message in slack format
    message = build_message(dictionary)
    message.reverse()  # show most import values first

    # Use Slack API to send messege to channel
    for mes in [message[:9], message[10:]]:
        # Make the API call and save results to `response`
        response = send_message(mes)    # Send in chuncks
        # Check to see if the message sent successfully.
        # If the message succeeded, `response["ok"]`` will be `True`
        if response["ok"]:
            print("Message posted successfully: " + response["message"]["ts"])
        # If the message failed, check for rate limit headers in the response
        elif response["ok"] is False and response["headers"]["Retry-After"]:
            # The `Retry-After` header will tell you how long to wait before retrying
            delay = int(response["headers"]["Retry-After"])
            print("Rate limited. Retrying in " + str(delay) + " seconds")
            time.sleep(delay)
            send_message(mes)
