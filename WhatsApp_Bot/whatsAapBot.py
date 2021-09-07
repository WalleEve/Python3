from twilio.rest import Client

account_sid = 'AC3977a98c97849d5799e354e7397cf708'
auth_token = 'e516357a55b6901db84860a30c8123c8'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              from_='whatsapp:+14155238886',
                              body='Your Twilio code is 1238432',
                              to='whatsapp:+919692392243'
                          )

print(message.sid)
