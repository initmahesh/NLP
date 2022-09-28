import boto3
import json 

comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
text="@105836 LiveChat is online at the moment - _https://t.co/SY94VtU8Kq_ (https://t.co/SY94VtU8Kq) or contact 03331 031 031 option 1, 4, 3 (Leave a message) to request a call back \n \
@VirginTrains see attached error message. I've tried leaving a voicemail several times in the past week _https://t.co/NxVZjlYx1k_ (https://t.co/NxVZjlYx1k)"

print('calling DetectDominatingLanguage')
print(json.dumps(comprehend.detect_entities(Text=text,LanguageCode='en')))
print("End of DetectDominantLanguage\n")