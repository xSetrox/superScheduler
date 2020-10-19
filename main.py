from datetime import datetime
from time import sleep
import os
import csv
import calendar
import webbrowser
from pyfiglet import Figlet

# cool logo stuff. optional
fig = Figlet()
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# we need to call color as a command so the coloring/formatting works properly in consoles
os.system('color')
print(bcolors.OKBLUE + fig.renderText('superSchedule') + '\nDeveloped by Lance Faltinsky\nhttps://github.com/xsetrox')
# show logo for 5 seconds
sleep(5)
# init empty set. we will use this to store the currently ongoing meetings, that way the system doesn't reopen them.
runningclasses = []
# lookup table for converting weekdays to college-esque abbreviations.
lookup = {'Sunday':'S','Monday':'M','Tuesday':'T','Wednesday':'W','Thursday':'R','Friday':'F','Saturday':'Sa'}
# empty dict that we will store contents of the csv in
meetings = {}
# csv reading, writes to dict
with open('meetings.csv',newline='') as file:
    reader = csv.reader(file, delimiter=',')
    for line in reader:
        meetings[line[0]] = {'time':line[1],'days':line[2],'link':line[3],'duration':line[4]}

# self-explanatory, returns an int of the num. of minutes until the specified time. is negative if event is in the past
def get_time_from_now(target_time):
    return int((target_time - datetime.now()).total_seconds() / 60)

# opens meeting link when called. really just here for 'hooking' if we wanna add extra features or handling
def initiate_session(name):
    runningclasses.append(name)
    link = meetings[name]['link']
    print(f'{bcolors.OKBLUE}Initiating meeting...')
    #webbrowser.open(link)

# main loop
while True:
    # clear console every run for neatness
    os.system('cls')
    # get the time now, format it into stuff like 2:50 PM
    time = datetime.now().strftime("%H:%M %p")
    today = calendar.day_name[datetime.now().today().weekday()]
    print(f'{bcolors.OKGREEN}The current time is {time}.')
    for meeting in meetings.keys():
        classtime = meetings[meeting]['time']
        classdur = int(meetings[meeting]['duration'])
        classlink = meetings[meeting]['link']
        # if and only if the event is today, run this code
        if lookup[today] in meetings[meeting]['days'].split():
            # parse event time into a datetime object
            targettime = datetime.strptime(meetings[meeting]['time'],"%I:%M %p")
            # datetime object is just time, so we need to combine it with today's date so its not from 1997. literally
            targettime = datetime.combine(datetime.today().date(),targettime.time())
            # time from now
            tfn = get_time_from_now(targettime)
            # if meeting already running, do not run it again
            if meeting in runningclasses:
                break
            # check if event is in the future. if it is, run specific warnings, ie a 30-minute before warning
            if tfn > 0:
                if tfn < 30:
                    if tfn < 5:
                        print(f'{bcolors.OKBLUE}Starting up meeting with 5 minutes to spare...')
                        initiate_session(meeting)
                    else:
                        print(f'{bcolors.FAIL}30 MINUTE ALERT: Your meeting for \"{meeting}\" is today and occurs in ~{tfn} minutes, at {classtime}.')
                elif tfn > 30:
                    print(f'{bcolors.WARNING}Your meeting for \"{meeting}\" is today and occurs in ~{tfn} minutes, at {classtime}.')
            # event isnt in future??!?!! panic.
            else:
                # ok but was it in the past?
                if tfn < 0:
                    if tfn < -classdur:
                        # drat. it was in the past and we missed it. oh well
                        if meeting in runningclasses:
                            runningclasses.remove(meeting)
                            continue
                    else:
                        # wait! the meeting is still running, but we're late. jump in.
                        if meeting not in runningclasses:
                            initiate_session(meeting)
        elif meeting in runningclasses:
            # event isnt actually today but is in running classes. some nerd probably left it on overnight.
            # lets remove it.
            runningclasses.remove(meeting)
    # sleep for (a suggested) 30 seconds so the loop isnt out of control
    sleep(30)
