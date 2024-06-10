import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = 'Enter yours here'
# Your Auth Token from twilio.com/console
auth_token = 'Enter yours here'

client = Client(account_sid, auth_token)

# Read contacts from CSV file
contacts_df = pd.read_csv('contacts.csv')

# Message to send
message_body = 'Hello, this is albert!'

for index, row in contacts_df.iterrows():
    message = client.messages.create(
        to='Enter yours here',
        from_='Enter yours here',  # Your Twilio phone number
        body=message_body
    )
    print(f"Message sent to {row['name']} at {row['phone']}")

print("All messages sent!")
