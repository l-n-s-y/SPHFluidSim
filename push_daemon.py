#!/usr/bin/python3

import os,time
from datetime import datetime

log_file = "push_daemon.log"
def dlog(msg):
    datestamp = datetime.now().date().isoformat()
    time = datetime.now().time()
    timestamp = f"[{datestamp} - {time.hour}:{time.minute}:{time.second}]"
    print(msg)
    with open(log_file,"a") as f:
        f.write(timestamp," ",msg+"\n")

current_schedule = []
def load_schedule(schedule):
    global current_schedule

    current_schedule = schedule
    
    dlog("Loaded new schedule.")
    dlog("Restarting...")


pushart_repo = "" # TODO: Make repo
def setup_github():
    o = os.popen(f"git clone {pushart_repo}").read()
    print(o)
    o = os.popen(f"git remote set-url origin {pushart_repo}")
    print(o)
    o = os.popen(f"git pull {pushart_repo}")
    print(o)
   
def main():
    pushes_today = 0
    schedule_index = 0

    check_period = 10

    dlog("Starting daemon...")

    setup_github()

    while True:
        time.sleep(check_period)
        if current_schedule == []:
            dlog("No schedule loaded. Waiting...")
            continue

        dlog("Checking for pushes...")
        
        entry = current_schedule[schedule_index]

        # Handle scheduled pushes
        if datetime.date.today().isoformat() == entry[0]:
            # If push requirement has been reached
            if pushes_today >= entry[1]:
                dlog("Push quota has already been reached.")
                continue

            dlog("Valid push slot found. Committing")

            commit_command = f"git commit -m 'new push @ {datetime.date.today().isoformat}-{datetime.datetime.now().time().isoformat()}'"
            os.popen(commit_command + " && git push")
            dlog("Finished commit. Sleeping...")

if __name__ == "__main__":
    main()
