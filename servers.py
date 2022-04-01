from ObstacleHandler import oh
from TLSimulator import sim
import time 
import logging
from LCDServer import LCD
from pathlib import Path

print(Path("servers.py").absolute())

def runServers():

    # LCD Print
    lcdON = True
    lcd = LCD(numofTL=3)

    try:        
        """Method for sending the simulated semaphore signals.
        """
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger('root')

        # Set to true for output on LCD screen
        # Get time stamp when starting tester
        timeout_duration = 3600
        start_time = time.time()

        # Create broadcaster object
        Adv = sim()
        
        ObsHanServer = oh(logger)

        # Start the broadcaster
        Adv.start()
        ObsHanServer.start()

        # Wait until 60 seconds passed
        while (time.time()-start_time < timeout_duration):
            if lcdON:
                lcd.TLstate = [Adv.main_state, Adv.main_state, Adv.start_state]
                if(ObsHanServer.data_saver.appends) > 0:
                    lcd.detectedObject = ObsHanServer.data_saver.return_obstacle()

                lcd.runLCD()
                time.sleep(0.5)

        # Stop the broadcaster
        Adv.stop()
    except KeyboardInterrupt:
        lcd.stopLCD()
        Adv.stop()

runServers()
# runAdvertiser()
# print("Trying to run OH")
# try:
#     runOH()
# except Exception as e:
#     print("OH error = ", e)
