from html import entities
from urllib import response
from google.cloud import language_v1
import time

client = language_v1.LanguageServiceClient()

text_content = "@105836 LiveChat is online at the moment - _https://t.co/SY94VtU8Kq_ (https://t.co/SY94VtU8Kq) or contact 03331 031 031 option 1, 4, 3 (Leave a message) to request a call back \n \
@VirginTrains see attached error message. I've tried leaving a voicemail several times in the past week _https://t.co/NxVZjlYx1k_ (https://t.co/NxVZjlYx1k)"
iterator = 5
total_time=0

document = language_v1.Document(content=text_content, type_=language_v1.Document.Type.PLAIN_TEXT)
# Available values: NONE, UTF8, UTF16, UTF32
encoding_type = language_v1.EncodingType.UTF8
for x in range(0,iterator):
    start = time.process_time()
    response = client.analyze_entities(request={"document": document,"encoding_type":encoding_type})
    total_time = total_time + (time.process_time() - start)
print("Total time taken to run",iterator,"is: ",total_time, "\nAverage time is:", (total_time/iterator)) 

iterator = 50
total_time=0
print("Runing : " , iterator, " times please wait ..")
for x in range(0,iterator):
    start = time.process_time()
    # Sending to east-us-1 region  
   # print(json.dumps(comprehend.detect_entities(Text=text,LanguageCode='en',)))
    response = client.analyze_entities(request={"document": document,"encoding_type":encoding_type})
    total_time = total_time + (time.process_time() - start)
print("Total time taken to run",iterator,"is: ",total_time, "\nAverage time is:", (total_time/iterator)) 