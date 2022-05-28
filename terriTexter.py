from twilio.rest import Client 
from imgurpython import ImgurClient
import keys, time
client = Client(keys.account_sid, keys.auth_token)
iClient = ImgurClient(keys.client_id, keys.client_secret)



url_array = []
total_pics = 0
day = False
HALF_DAY = 43200
# grab all the images from the Terri Album 
items = iClient.get_album_images('wakA5we')
for item in items:
    url_array.append(item.link)

# send out daily Terri Pic  
while (True):
    for url in url_array:
        total_pics += 1
        if day: 
            message = client.messages.create(from_=keys.twilio_number,  
                                        body='Jo Sun, 美妞!' + " (" + "I've spent: " + "$"+ str(total_pics*2*0.1) + " in total)",
                                        media_url= url,      
                                        to=[keys.Phoebe,keys.Allison]
                                    )
            day = False 
        else:
            message = client.messages.create(from_=keys.twilio_number,  
                                        body='Good Night, you did a good job today, I\m proud of you' + " (" + "I've spent: " +"$"+  str(total_pics*2*0.1) + ")",
                                        media_url= url,      
                                        to=[keys.Phoebe,keys.Allison]
                                    )
            day = True
        print("Pic Number: " + str(total_pics))
        time.sleep(HALF_DAY)

# message = client.messages.create(
#     to="+16476066782", 
#     from_="+19207813947",
#     body="It's Spooky",
#     media_url= url_array[0])
# print(message.sid)