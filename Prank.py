import time as t
import subprocess as s
import os
import glob
import winsound

#This is a prank program I created at the beginning of my python journey. I found out python could activate programs
# and so this is "practice" with that. The awesome thing about this program is you click on it and it does nothing....
#......for 30 minutes. Then every 10 minutes this program plays a sound from the sounds folder. The sound only
# lasts for 5 seconds and then the next one will play 10 minutes later. And of course this program will repeat forever
# until your computer is shutdown or the participant will have to stop in the task manager as no prompt or shell
# is visible.


sounds = glob.glob('J:\Sounds\*.wav')
os.chdir('J:\Sounds')

#Sleep for 30 minutes
t.sleep(1800)

prank = 1

#Prank will always equal 1 so forever...

while prank == 1:
    for sound in sounds:
        #10 minutes
        t.sleep(600)
        winsound.PlaySound(sound, winsound.SND_FILENAME)
