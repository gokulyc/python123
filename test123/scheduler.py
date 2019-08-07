# Schedule Library imported 
import schedule 
import time,logging,sys

logging.basicConfig(filename="test.log", level=logging.DEBUG)
# Functions setup 
def sudo_placement(): 
    # print("Get ready for Sudo Placement at Geeksforgeeks") 
    logging.debug("Get ready for Sudo Placement at Geeksforgeeks")
  
def good_luck(): 
    logging.debug("Good Luck for Test") 
  
def work(): 
    logging.debug("Study and work hard") 
  
def bedtime(): 
    logging.debug("It is bed time go rest") 
      
def geeks(): 
    logging.debug("Shaurya says Geeksforgeeks") 
  
# Task scheduling 
# After every 10mins geeks() is called.  
schedule.every(1).minutes.do(geeks) 
  
# After every hour geeks() is called. 
schedule.every().hour.do(geeks) 
  
# Every day at 12am or 00:00 time bedtime() is called. 
schedule.every().day.at("00:00").do(bedtime) 
  
# After every 5 to 10mins in between run work() 
schedule.every(5).to(10).minutes.do(work) 
  
# Every monday good_luck() is called 
schedule.every().monday.do(good_luck) 
  
# Every tuesday at 18:00 sudo_placement() is called 
schedule.every().tuesday.at("18:00").do(sudo_placement) 
  
# Loop so that the scheduling task 
# keeps on running all time. 
while True: 
  
    # Checks whether a scheduled task  
    # is pending to run or not 
    try:
        schedule.run_pending()
        time.sleep(1) 
    except KeyboardInterrupt:
        logging.debug("program stopped")
        sys.exit()