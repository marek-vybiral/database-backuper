import os
import schedule
import time

from backup import do_backup

for schedule_entry in os.environ['SCHEDULE'].split(','):
    schedule_entry = schedule_entry.strip()
    schedule.every().day.at(schedule_entry).do(do_backup)
    
    print(f'Scheduling for {schedule_entry}')

print('\nScheduler is running...')

while 1:
    schedule.run_pending()
    time.sleep(10)
