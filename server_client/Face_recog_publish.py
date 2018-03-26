from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import time

cert_path = "c:/certs/"
host = "a2kc9la4cp40qj.iot.us-east-1.amazonaws.com"
returntopic = "$aws/things/ir2_proj/shadow/return"
sendtopic = "$aws/things/ir2_proj/shadow/up"
logtopic = "$aws/things/ir2_proj/log"
root_cert = cert_path + "root-CA.crt"
cert_file = cert_path + "ir2_proj.cert.pem"
key_file = cert_path + "ir2_proj.private.key"

    
def customCallback(client, userdata, message):
    print("Received a new message: ")
    print(message.payload)
    print("from topic: ")
    print(message.topic)
    print("--------------\n\n")



#starting service
robot = AWSIoTMQTTClient(host)
robot.configureEndpoint(host, 8883)
robot.configureCredentials(root_cert, key_file, cert_file)

# AWSIoTMQTTClient connection configuration
robot.configureAutoReconnectBackoffTime(1, 32, 20)
robot.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
robot.configureDrainingFrequency(2)  # Draining: 2 Hz
robot.configureConnectDisconnectTimeout(10)  # 10 sec
robot.configureMQTTOperationTimeout(5)  # 5 sec

# Connect and subscribe to AWS IoT

robot.connect()
time.sleep(1)

#robot.subscribe(sendtopic, 1, customCallback)

#robot.loop()
time.sleep(1)
for x in range(0, 10):
    robot.publish(sendtopic, 'message %d'% (x),1)
    time.sleep(2)

robot.disconnect()

#loops for ever so that connection will be present
#while True:
	#robot.loop()
#	time.sleep(1)
