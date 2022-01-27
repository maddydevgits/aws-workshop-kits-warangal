# import the packages

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import random
import time

# create a client object
client=AWSIoTMQTTClient("kits_client")

# configure the end-point
client.configureEndpoint('a366shaagepcsd-ats.iot.eu-west-1.amazonaws.com',8883)

# configure the credentials
client.configureCredentials("AmazonRootCA1.pem","device-private.pem.key","device-certificate.pem.crt")

client.configureOfflinePublishQueueing(-1) # infinite
client.configureDrainingFrequency(2) # frequency of data transfer
client.configureConnectDisconnectTimeout(10) # disconnect timeout
client.configureMQTTOperationTimeout(5) # operation timeout

def notification(client,userdata,message):
    print(message.payload)
    print(message.topic)

client.connect()
print("AWS IoT is connected")
time.sleep(2)
client.subscribe("kits/iot",1,notification)

while True:
    humidity=random.randint(20,50) # sample data
    temperature=random.randint(20,50) # sample data
    payload='{"temperature": ' + str(temperature) + ', "humidity" :' + str(humidity)+'}'
    print(payload) # displaying the sensory feed
    client.publish('kits/iot',payload,0)
    time.sleep(2)
