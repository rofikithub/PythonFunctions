# pip install schedule
import schedule
import time

def task():
    print("Task executed...")

schedule.every(10).seconds.do(task)

while True:
    schedule.run_pending()
    time.sleep(1)
