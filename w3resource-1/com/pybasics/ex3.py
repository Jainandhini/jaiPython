"""
Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14     """


import datetime
a=datetime.datetime.now().strftime("%Y - %m - %d  %H:%M:%S")

print("Current date and time\n"+a)
