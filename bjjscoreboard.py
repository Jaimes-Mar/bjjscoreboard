import tkinter

# window setup()
window = tkinter.Tk()
window.title("BJJ Scoreboard")
window.geometry('1080x720')

#global score variables
score_a = 0
score_b = 0

#functions
def red_2():
	global score_a
	score_a = score_a + 2
	display_a.config(text = str(score_a))
	display_a.grid(row = 2, column = 0)
 
def red_3():
	global score_a
	score_a = score_a + 3
	display_a.config(text = str(score_a))
	display_a.grid(row = 2, column = 0)
 
def red_4():
	global score_a
	score_a = score_a + 4
	display_a.config(text = str(score_a))
	display_a.grid(row = 2, column = 0)

def blue_2():
	global score_b
	score_b = score_b + 2
	display_b.config(text = str(score_b))
	display_b.grid(row = 2, column = 1)
 
def blue_3():
	global score_b
	score_b = score_b + 3
	display_b.config(text = str(score_b))
	display_b.grid(row = 2, column = 1)

def blue_4():
	global score_b
	score_b = score_b + 4
	display_b.config(text = str(score_b))
	display_b.grid(row = 2, column = 1)

def red_min1():
	global score_a
	score_a = score_a - 1
	display_a.config(text = str(score_a))
	display_a.grid(row = 2, column = 0)

def blue_min1():
	global score_b
	score_b = score_b - 1
	display_b.config(text = str(score_b))
	display_b.grid(row = 2, column = 1)

def reset_a():
	global score_a
	score_a = 0
	display_a.config(text = str(score_a))
	display_a.grid(row = 2, column = 0)

def reset_b():
	global score_b
	score_b = 0
	display_b.config(text = str(score_b))
	display_b.grid(row = 2, column = 1)
 
def reset_both():
	global score_b
	score_b = 0
	display_b.config(text = str(score_b))
	display_b.grid(row = 2, column = 1)
	global score_a
	score_a = 0
	display_a.config(text = str(score_a))
	display_a.grid(row = 2, column = 0)
 
def kill():
    window.destroy()
    return None


#scoreboard labels
tkinter.Label(window, text = "Red corner", font=("Helvetica", 35, 'bold')).grid(row = 1, column = 0)
tkinter.Label(window, text = "Blue corner", font=("Helvetica", 35, 'bold')).grid(row = 1, column = 1)

#Team A Score Display
display_a = tkinter.Label(window, text = str(score_a), font=("Helvetica", 125))
display_a.grid(row = 2, column = 0)
#Team B Score Display
display_b = tkinter.Label(window, text = str(score_b), font=("Helvetica", 125))
display_b.grid(row = 2, column = 1)



#score buttons
button1 = tkinter.Button(window, text = "+2 red", command = red_2).grid(row = 3, column = 0, sticky = "nsew")
button1 = tkinter.Button(window, text = "+3 red", command = red_3).grid(row = 4, column = 0, sticky = "nsew")
button1 = tkinter.Button(window, text = "+4 red", command = red_4).grid(row = 5, column = 0, sticky = "nsew")
button2 = tkinter.Button(window, text = "+2 Blue ", command = blue_2).grid(row = 3, column = 1, sticky = "nsew")
button2 = tkinter.Button(window, text = "+3 Blue ", command = blue_3).grid(row = 3, column = 1, sticky = "nsew")
button2 = tkinter.Button(window, text = "+4 Blue ", command = blue_4).grid(row = 4, column = 1, sticky = "nsew")
button3 = tkinter.Button(window, text = "-1 red", command = red_min1).grid(row = 6, column = 0, sticky = "nsew")
button3 = tkinter.Button(window, text = "-1 Blue", command = blue_min1).grid(row = 5, column = 1, sticky = "nsew")

#redo and kill buttons
redo_a = tkinter.Button(window, text = "Reset Red", command = reset_a).grid(row = 6, column = 2)
redo_a = tkinter.Button(window, text = "Reset Blue", command = reset_b).grid(row = 5, column = 2)
redo_both = tkinter.Button(window, text = "Reset Both", command = reset_both).grid(row = 7, column = 2)
killbutton = tkinter.Button(window, text = "close program", command = kill).grid(row = 8, column = 2)

#main loop to keep gui window open
window.mainloop()
