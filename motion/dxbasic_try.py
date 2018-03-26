from pyax12.connection import Connection
import time

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

# Connect to the serial port
serial_connection = Connection(port="/dev/ttyUSB0", baudrate=1000000)

dynamixel_id = 1

# Go to 0°
serial_connection.goto(dynamixel_id, 0, speed=112, degrees=True)
time.sleep(1)    # Wait 1 second

# Go to -45° (45° CW)
serial_connection.goto(dynamixel_id, -60, speed=512, degrees=True)
time.sleep(1)    # Wait 1 second
"""
# Go to -90° (90° CW)
serial_connection.goto(dynamixel_id, -60, speed=512, degrees=True)
time.sleep(1)    # Wait 1 second

# Go to -135° (135° CW)
serial_connection.goto(dynamixel_id, -135, speed=512, degrees=True)
time.sleep(1)    # Wait 1 second

# Go to -150° (150° CW)
serial_connection.goto(dynamixel_id, -150, speed=512, degrees=True)
time.sleep(1)    # Wait 1 second

# Go to +150° (150° CCW)
serial_connection.goto(dynamixel_id, 150, speed=512, degrees=True)
time.sleep(2)    # Wait 2 seconds

# Go to +135° (135° CCW)
serial_connection.goto(dynamixel_id, 135, speed=512, degrees=True)
time.sleep(1)    # Wait 1 second

# Go to +90° (90° CCW)
serial_connection.goto(dynamixel_id, 30, speed=512, degrees=True)
time.sleep(1)    # Wait 1 second
"""
# Go to +45° (45° CCW)
serial_connection.goto(dynamixel_id, 45, speed=112, degrees=True)
time.sleep(1)    # Wait 1 second

# Go back to 0°
serial_connection.goto(dynamixel_id, 0, speed=112, degrees=True)

# Close the serial connection
serial_connection.close()
