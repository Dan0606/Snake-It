import schedule
import time

def print_me(string):
    print(string)

strings = ["Dan", "Yarin"]

schedule.every(5).seconds.do(print_me, "dan")

while True:
    schedule.run_pending()
    time.sleep(1)

