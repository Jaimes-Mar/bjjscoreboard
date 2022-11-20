import tkinter as tk
import time
from tkinter import messagebox


# window setup()
window = tk.Tk()
window.title("BJJ Scoreboard")
window.geometry('1080x720')

#global score variables
score_a = 0
score_b = 0

# Declaration of time variables
hour=tk.StringVar()
minute=tk.StringVar()
second=tk.StringVar()

# setting the default value as 0
hour.set("00")
minute.set("00")
second.set("00")

# Use of Entry class to take input from the user
hourEntry= tk.Entry(window, width=3, font=("Arial",18,""),
                 textvariable=hour)
hourEntry.grid(row=1, column=4)
  
minuteEntry= tk.Entry(window, width=3, font=("Arial",18,""),
                   textvariable=minute)
minuteEntry.grid(row=2, column=4)
  
secondEntry= tk.Entry(window, width=3, font=("Arial",18,""),
                   textvariable=second)
secondEntry.grid(row=3, column=4)

def submit():
    try:
        # the input provided by the user is
        # stored in here :temp
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        print("Please input the right value")
    while temp >-1:
         
        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins,secs = divmod(temp,60)
  
        # Converting the input entered in mins or secs to hours,
        # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
        # 50min: 0sec)
        hours=0
        if mins >60:
             
            # divmod(firstvalue = temp//60, secondvalue
            # = temp%60)
            hours, mins = divmod(mins, 60)
         
        # using format () method to store the value up to
        # two decimal places
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
  
        # updating the GUI window after decrementing the
        # temp value every time
        window.update()
        time.sleep(1)
  
        # when temp value = 0; then a messagebox pop's up
        # with a message:"Time's up"
        if (temp == 0):
            messagebox.showinfo("BJJ scoredboard", "TIME: Your match is over ")
            reset_both()
        # after every one sec the value of temp will be decremented
        # by one
        temp -= 1
 
# button widget
btn = tk.Button(window, text='Enter time\n and then click here\n to begin your match',
             command= submit,width= 15)
btn.grid(row=5, column=3)

#functions
def min_5():
    hour.set("00")
    minute.set("05")
    second.set("0")
    submit()
    
def red_2():
	global score_a
	score_a = score_a + 2
	display_a.config(text = str(score_a))

def red_3():
	global score_a
	score_a = score_a + 3
	display_a.config(text = str(score_a))
 
def red_4():
	global score_a
	score_a = score_a + 4
	display_a.config(text = str(score_a))

def blue_2():
	global score_b
	score_b = score_b + 2
	display_b.config(text = str(score_b))
 
def blue_3():
	global score_b
	score_b = score_b + 3
	display_b.config(text = str(score_b))

def blue_4():
	global score_b
	score_b = score_b + 4
	display_b.config(text = str(score_b))

def red_min1():
	global score_a
	score_a = score_a - 1
	display_a.config(text = str(score_a))

def blue_min1():
	global score_b
	score_b = score_b - 1
	display_b.config(text = str(score_b))

def reset_a():
	global score_a
	score_a = 0
	display_a.config(text = str(score_a))

def reset_b():
	global score_b
	score_b = 0
	display_b.config(text = str(score_b))
 
def reset_both():
	global score_b
	score_b = 0
	display_b.config(text = str(score_b))

	global score_a
	score_a = 0
	display_a.config(text = str(score_a))

 
def kill():
    window.destroy()
    return None


#scoreboard labels
tk.Label(window, text = "Red corner", font=("Helvetica", 35, 'bold')).grid(row = 1, column = 0, sticky = "nsew")
tk.Label(window, text = "Blue corner", font=("Helvetica", 35, 'bold')).grid(row = 1, column = 1, sticky = "nsew")
tk.Label(window, text = "Hour", font=("Helvetica", 35, 'bold')).grid(row = 1, column = 5)
tk.Label(window, text = "mins", font=("Helvetica", 35, 'bold')).grid(row = 2, column = 5)
tk.Label(window, text = "secs", font=("Helvetica", 35, 'bold')).grid(row = 3, column = 5)
#Team A Score Display
display_a = tk.Label(window, text = str(score_a), font=("Helvetica", 125))
display_a.grid(row = 2, column = 0)
#Team B Score Display
display_b = tk.Label(window, text = str(score_b), font=("Helvetica", 125))
display_b.grid(row = 2, column = 1)



#score buttons
button1 = tk.Button(window, text = "+2 red", command = red_2,height = 3).grid(row = 3, column = 0, sticky = "nsew")
button1 = tk.Button(window, text = "+3 red", command = red_3,height = 3).grid(row = 4, column = 0, sticky = "nsew")
button1 = tk.Button(window, text = "+4 red", command = red_4,height = 3).grid(row = 5, column = 0, sticky = "nsew")
button2 = tk.Button(window, text = "+2 Blue ", command = blue_2).grid(row = 3, column = 1, sticky = "nsew")
button2 = tk.Button(window, text = "+3 Blue ", command = blue_3).grid(row = 4, column = 1, sticky = "nsew")
button2 = tk.Button(window, text = "+4 Blue ", command = blue_4).grid(row = 5, column = 1, sticky = "nsew")
button3 = tk.Button(window, text = "-1 red", command = red_min1,height = 3).grid(row = 6, column = 0, sticky = "nsew")
button3 = tk.Button(window, text = "-1 Blue", command = blue_min1).grid(row = 6, column = 1, sticky = "nsew")

#redo and kill buttons
redo_a = tk.Button(window, text = "Reset Red", command = reset_a,height = 3, width = 8).grid(row = 4, column = 2, sticky = "nsew")
redo_a = tk.Button(window, text = "Reset Blue", command = reset_b,height = 3).grid(row = 3, column = 2, sticky = "nsew")
redo_both = tk.Button(window, text = "Reset Both", command = reset_both,height = 3).grid(row = 5, column = 2, sticky = "nsew")
killbutton = tk.Button(window, text = "close program", command = kill,height = 3).grid(row = 6, column = 2, sticky = "nsew")
min5button = tk.Button(window, text = "5 min program", command = min_5,height = 3).grid(row = 4, column = 3, sticky = "nsew")

#main loop to keep gui window open
window.mainloop()
