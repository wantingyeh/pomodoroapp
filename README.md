# pomodoro app
The Pomodoro Technique was developed in the late 1980s by Francesco Cirillo. Nowadayds, it's been widely used for time management. The process of the pomodoro timer is:
1. start the timer and work for 25 minutes
2. have a 5-minute short break
3. After 4 rounds, you can have a longer break of 20 minutes

# main.py
1. written in Python with Tkinter for the GUI interface
2. press "Start" to start the timer
  - The timer goes to the work mode for 25 minutes
  ![image](https://user-images.githubusercontent.com/83806848/205884113-960b5328-73db-4161-9708-b54b2d3bb283.png)
  - After you complete one work round, you'll get a check. Then, it goes to the break mode for 5 minutes.
  ![image](https://user-images.githubusercontent.com/83806848/205884300-b9f72742-6fb9-4f12-8dbe-d6b2d0dfb087.png)
3. Press "reset" to restart the timer
  - Once you reset the timer, the clock will go back to the start "00:00" and restart the round
  - You'll also lose all the checks
  
# modification
If you want to modify the constants of this app, you can change the variables in "CONSTANTS" section

PINK = "#e2979c" \
RED = "#e7305b" \
GREEN = "#9bdeac" \
YELLOW = "#f7f5dd" \
FONT_NAME = "Courier" \
WORK_MIN = 25 \
SHORT_BREAK_MIN = 5 \
LONG_BREAK_MIN = 20 \
reps = 0     # repetition \
timer = None
