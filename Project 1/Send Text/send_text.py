#from twilio.rest import TwilioRestClient
from twilio import rest

account_sid = "AC6393f02f6423fd7ebf1f7f576a0b2c0f" # Your Account SID from www.twilio.com/console
auth_token  = "4f5b1daeb04900a432fa214adfdf937f"  # Your Auth Token from www.twilio.com/console

#client = TwilioRestClient(account_sid, auth_token)
client = rest.TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body="Hello from Python",
    to="+16475015882",    # Replace with your phone number
    from_="+16476913910") # Replace with your Twilio number

print(message.sid)