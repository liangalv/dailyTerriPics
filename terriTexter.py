from twilio.rest import Client 
import keys
 
client = Client(keys.account_sid, keys.auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Here is your Daily Terri Pic!',
                              media_url= 'https://demo.twilio.com/owl.png',      
                              to='whatsapp:+16476066782'
                          )  
 
print(message.sid)