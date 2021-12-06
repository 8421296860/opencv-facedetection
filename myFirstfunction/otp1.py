from twilio.rest import Client


def sendotp(otpreci):
    account_sid = 'ACe8caad8112e2135294377d739ce3e9b9'
    auth_token = '1f64cdbd1b9b17eda2e22281de410c6c'
    client = Client(account_sid, auth_token) 
    msg='OTP for Login : ' + str(otpreci)
    
    message = client.messages.create(
    from_='whatsapp:+14155238886',
    body= msg ,
    to='whatsapp:+918421296860'
    )
    



