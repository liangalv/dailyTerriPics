from twilio.rest import Client 
from imgurpython import ImgurClient
import keys, time
client = Client(keys.account_sid, keys.auth_token)
iClient = ImgurClient(keys.client_id, keys.client_secret)



url_array = []
total_pics = 0
# grab all the images from the Terri Album 
items = iClient.get_album_images('wakA5we')
for item in items:
    url_array.append(item.link)

# send out daily Terri Pic  
while (True):
    for url in url_array:
        total_pics += 1
        message = client.messages.create(from_=keys.twilio_number,  
                                    body='Here is your Daily Terri Pic!' + " (" + "We've sent: " + str(total_pics) + ")",
                                    media_url= url,      
                                    to=keys.Allison
                                )
        
        print("Pic Number: " + str(total_pics))
        time.sleep(600)

# message = client.messages.create(
#     to="+16476066782", 
#     from_="+19207813947",
#     body="It's Spooky",
#     media_url= url_array[0])
# print(message.sid)