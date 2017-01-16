'''
Created on 9 Jun 2015

@author: matthew oppenheim
witilt constants
'''
# byte locations in binary data string
# START_CHAR = 0
# DOD = 1
# COUNT_HIGH = 2
# COUNT_LOW = 3
# X_HIGH = 4
# X_LOW = 5
# Y_HIGH = 6
# Y_LOW = 7
# Z_HIGH = 8
# Z_LOW = 9
# BATT_LOW = 10
# BATT_HIGH = 11
# R_HIGH = 12
# R_LOW = 13
# END_CHAR = 14

# byte locations in binary data string when start_char and dod removed
COUNT_HIGH = 0
COUNT_LOW = 1
X_HIGH = 2
X_LOW = 3
Y_HIGH = 4
Y_LOW = 5
Z_HIGH = 6
Z_LOW = 7
#BATT_LOW = 8
#BATT_HIGH = 9
R_HIGH = 8
R_LOW = 9
END_CHAR = 10

# calibration values
X_MID = 484
X_WIDTH = 255
Y_MID = 477
Y_WIDTH = 126
Z_MID = 598
Z_WIDTH = 253
R_ZERO = 458

BAUD = 115200
NUM_SAMPLES = 300
SIGNAL_FROM_GUI_TO_SERIAL = 'signal_from_gui_to_serial'
SIGNAL_FROM_GUI_FOR_DATA = 'signal_from_gui_for_data'
SENDER_FROM_GUI = 'sender_from_gui'
SENDER_FROM_SERIAL = 'sender_from_serial'
SERIAL_PORT = '/dev/ttyUSB0'
SIGNAL_FROM_BOARD = 'signal_from_board'

G_MAX = 3
G_MIN = -3
R_MAX = 3
R_MIN = -3