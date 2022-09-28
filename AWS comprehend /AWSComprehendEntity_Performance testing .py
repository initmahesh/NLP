import boto3
import json 
import time 

comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')

print("warming up for benchamrking")
text="@105836 LiveChat is online at the moment - _https://t.co/SY94VtU8Kq_ (https://t.co/SY94VtU8Kq) or contact 03331 031 031 option 1, 4, 3 (Leave a message) to request a call back \n \
@VirginTrains see attached error message. I've tried leaving a voicemail several times in the past week _https://t.co/NxVZjlYx1k_ (https://t.co/NxVZjlYx1k)"

iterator = 5
total_time=0
for x in range(0,iterator):
    start = time.process_time()
    # Sending to east-us-1 region  
    #print(json.dumps(comprehend.detect_entities(Text=text,LanguageCode='en',)))
    comprehend.detect_entities(Text=text,LanguageCode='en',)
    total_time = total_time + (time.process_time() - start)
    # printing time taken 
print("Total time taken to run",iterator,"is: ",total_time, "\nAverage time is:", (total_time/iterator)) 

iterator = 50
total_time=0
print("Runing : " , iterator, " times please wait ..")
for x in range(0,iterator):
    start = time.process_time()
    # Sending to east-us-1 region  
   # print(json.dumps(comprehend.detect_entities(Text=text,LanguageCode='en',)))
    comprehend.detect_entities(Text=text,LanguageCode='en',)
    total_time = total_time + (time.process_time() - start)
print("Total time taken to run",iterator,"is: ",total_time, "\nAverage time is:", (total_time/iterator)) 