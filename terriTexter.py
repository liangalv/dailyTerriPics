from twilio.rest import Client 
from bs4 import BeautifulSoup
import requests 
import keys, time
client = Client(keys.account_sid, keys.auth_token)

source = requests.get('https://photos.app.goo.gl/S5S3p71fJVeqH8hL7').text
#generate the url_array, through web scrapping 
soup = BeautifulSoup(source, 'lxml')
images = soup.findAll('img')
# print(images)
url_array = []
total_pics = 0

for image in images:
    # print(image['src'])
    url_array.append(str(image['src']))
url_array.pop(0)

# each API call requires a 1Cent each
# send out daily Terri Pic  
while (True):
    for url in url_array:
        message = client.messages.create(from_='+19207813947',  
                                    body='Here is your Daily Terri Pic!',
                                    media_url= url,      
                                    to='+16476066782'
                                )
        total_pics += 1
        print("Pic Number: " + str(total_pics))
        time.sleep(86400)
        