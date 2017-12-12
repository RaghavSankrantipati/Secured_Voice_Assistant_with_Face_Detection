from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging
import time
import argparse
import json
"""export AWS_ACCESS_KEY_ID='AKIAIUBIWWZORPQHNCFQ'
	export AWS_SECRET_ACCESS_KEY='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'"""
   
AllowedActions = ['both', 'publish', 'subscribe']

def customCallback(client, userdata, message):
    print("Received a new message: ")
    print(message.payload)
    print("from topic: ")
    print(message.topic)
    print("--------------\n\n")

host = 'aa1kkd852hct2.iot.us-west-2.amazonaws.com'
rootCAPath = '/home/pi/Desktop/project/deviceSDK/certificates/root-CA.crt'
clientId = 'AKIAIUBIWWZORPQHNCFQ'
topic = 'projectTopic'

myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId, useWebsocket=True)
myAWSIoTMQTTClient.configureEndpoint(host, 443)
myAWSIoTMQTTClient.configureCredentials(rootCAPath)

myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

myAWSIoTMQTTClient.connect()
myAWSIoTMQTTClient.subscribe(topic, 1, customCallback)

time.sleep(2)

# Publish to the same topic in a loop forever
loopCount = 0
while True:
    if True:
        message = {}
        message['message'] = 'dummy'
        message['sequence'] = loopCount
        messageJson = json.dumps(message)
        myAWSIoTMQTTClient.publish(topic, messageJson, 1)
        print('Published topic %s: %s\n' % (topic, messageJson))
        loopCount += 1
    time.sleep(1)


