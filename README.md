# superScheduler
Python 3.7 script to open links at specific times. Made for Zoom meetings mainly. Made for Windows, might work for Mac/Linux, might not. I need to test still.
You simply put your meeting data into the .csv and it handles the rest.
I made this so that it will auto-join Zoom classes for me, even when I forget. It's lightweight, portable, and simple.

**DISCLAIMER: I AM NOT RESPONSIBLE FOR MISSED MEETINGS DUE TO A FAULT IN THIS PROGRAM. USE AT YOUR OWN RISK.**
I have tested this various times but I don't want to be held accountable because you missed your economy class.
This is among one of the most complex things I've coded so I may have missed a few bugs.. Be cautious. 

## Usage
Add your classes/meetings into meetings.csv. Follow this format:
```
meeting title,meetingTime PM/AM,Meeting day Letter,https://examplemeetinglink.com,meeting duration in secs
```
Example:
```
example class,4:00 PM,M,zoommtg://examplelink,170
```
If you are using excel or something to write it out (which you can do- its a spreadsheet), the comma is the separator for each column header.

## Meeting day codes
The third column uses day codes, or whatever they're called. I have followed college's codes for that as tightly as possible, but regardless, here they are:
```
S: Sunday
M: Monday
T: Tuesday
W: Wednesday
R: Thursday
F: Friday
Sa: Saturday
```
So if your meeting is on a Friday, the third column should be F.

## Requirements
```
pyfiglet==0.8.post1
```
Simply run `pip install pyfiglet`. ez.

### 
