from pyax12.connection import Connection
import time

# Connect to the serial port
chain = Connection(port="/dev/ttyUSB0", baudrate=1000000)

NK  = 1 # range -60 to 50
RSU = 2 # range -53 to 115
RSS = 3 # range -87 to 51
RER = 4 # range -114 to 100
REU = 5 # range -150 to 40
LSU = 6 # range -113 to 40
LSS = 7 # range -49 to 81
LER = 8 # range -90 to 98
LEU = 9 # range -133 to 86
HD  = 10 # range -39 to 36

speed = 200

def send_pos(mid, deg):
    serial_connection.goto(mid, deg, speed, degrees=True)
    time.sleep(1)    #` Wait 1 second

def initall():
    for dynamixel_id in range(1, 11) :
        serial_connection.goto(dynamixel_id, 0, speed, degrees=True)
        #time.sleep(1)    # Wait 1 second

# Go to 0°
## POSE 1 
#dynamixel_id = RSU
#pos = -35
for mid in range(1,11):
    pos = chain.get_present_position(mid,True)
    print(mid," ",pos)

# Close the serial connection
chain.close()
