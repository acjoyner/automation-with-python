import time as tm
import schedule

def job():
    print("Welcome to Python task Automation")

# Schedule the job every 5 seconds
schedule.every(5).seconds.do(job)

# Run the scheduler loop (outside the job function)
while True:
    schedule.run_pending()
    tm.sleep(1)
