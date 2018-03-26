from pyax12.connection import Connection

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

for dynamixel_id in range(1, 11) :

	# Ping the third dynamixel unit
	is_available = serial_connection.ping(dynamixel_id)

	print(dynamixel_id,is_available)

# Close the serial connection
serial_connection.close()
