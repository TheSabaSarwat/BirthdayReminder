import time
from pynotifier import Notification

birthdayFile = 'C:\\Users\\saba\\Documents\\personal\\birthdayReminder\\birthday.txt'
def SendNotification(name):
    Notification(
            title="Birthday",
            description= "Birthday Today \n" +name,
            icon_path='C:\\Users\\saba\\Documents\\personal\\birthdayReminder\\birthday.ico', # On Windows .ico is required, on Linux - .png
            duration=3,                              # Duration in seconds
            urgency=Notification.URGENCY_CRITICAL
            ).send()
    
def BirthdayCheck():
    file = open(birthdayFile,'r')
    today = time.strftime('%m%d')
    flag =0;
    for line in file:
        if today in line:
            line = line.split(' ', 1)
            flag = 1
            SendNotification(line[1])
			#we cannot have multiple desktop notification at a time
			#hence put a sleep when we have multiple birthday on same date
            time.sleep(5) 
if __name__ == '__main__':
    BirthdayCheck()
