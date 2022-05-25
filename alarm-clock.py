# Author: SMR (AMDG) 05/17/22

# Import Modules
from tkinter import *
import datetime
import time
from threading import *

# Creating an object
root = Tk()

# Setting the Geometry to fit the threads
root.geometry("400x200")

# Implementing the threading
def Threading():
	t1=Thread(target=alarm)
	t1.start()

def alarm():
	# While Loop
	while True:
		# Setting the alarm time
		set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

		# Making it sleep for a second
		time.sleep(1)

		# Function that will get the systems current time to refer to
		current_time = datetime.datetime.now().strftime("%H:%M:%S")
		print(current_time,set_alarm_time)

		# If statement to check whether or not the alarm is synced properly
		if current_time == set_alarm_time:
			print("Time to Wake up")
			# Playing sound

# Add Labels, Frame, Button, Drop down 
Label(root,text="Alarm Clock",font=("Times 20 bold"),fg="blue").pack(pady=10)
Label(root,text="Set Time",font=("Times 15 bold")).pack()

frame = Frame(root)
frame.pack()

# Drop down menu to select the amount of hours
hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23', '24'
		)
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

# Drop down choices to select the amount of minutes
minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23',
		'24', '25', '26', '27', '28', '29', '30', '31',
		'32', '33', '34', '35', '36', '37', '38', '39',
		'40', '41', '42', '43', '44', '45', '46', '47',
		'48', '49', '50', '51', '52', '53', '54', '55',
		'56', '57', '58', '59', '60')
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

# Drop down doices to choose the amount of seconds
second = StringVar(root)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23',
		'24', '25', '26', '27', '28', '29', '30', '31',
		'32', '33', '34', '35', '36', '37', '38', '39',
		'40', '41', '42', '43', '44', '45', '46', '47',
		'48', '49', '50', '51', '52', '53', '54', '55',
		'56', '57', '58', '59', '60')
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

# Button layout
Button(root,text="Set Alarm",font=("Times 15"),command=Threading).pack(pady=20)

# Final call of the function
root.mainloop()
