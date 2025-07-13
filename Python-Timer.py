from tkinter import *
from tkinter import ttk

# This function takes the values of each Spinbox.
# Disables the start button so it can't be clicked multiple times 
# Starts the countdown
def startcountdown():
    try:
        hrs = int(h.get())
        mins = int(m.get())
        secs = int(s.get())
        StartTimeBtn.config(state='disabled')
        countdown(hrs, mins, secs)
    except ValueError:
        TimeLabel.config(text="Enter a valid number")

# Takes in the time the users wants to countdown. 
# Displays the time and updates it to a label (TimeLabel)
# And sets the Start Countdown button on
def countdown(hrs, mins, secs):
    totalSeconds = hrs * 3600 + mins * 60 + secs

    if totalSeconds > 0:
        TimeLabel.config(text=f"Time left: {hrs} h {mins} m {secs} s")
        totalSeconds -= 1
        hrs = totalSeconds // 3600
        mins = (totalSeconds % 3600) // 60
        secs = totalSeconds % 60
        root.after(1000, countdown, hrs, mins, secs)
    else:
        TimeLabel.config(text="Time left: 0 h 0 m 0 s")
        root.after(1000, lambda: TimeLabel.config(text="Time's up!"))
        StartTimeBtn.config(state='normal')

# Set UI title and geometry.
root = Tk()
root.title("My Timer")
root.geometry("300x300")

# Create frame for Spinboxes in particular
spinboxFrame = ttk.Frame(root)
spinboxFrame.grid(column=0,row=2,columnspan=3)

# Spinboxes for hours, minutes, seconds with StringVar for binding
h = StringVar()
hrs = ttk.Spinbox(
    spinboxFrame, 
    from_=0, 
    to=24, 
    width=2, 
    textvariable=h
    )
hrs.grid(column=0, row=2, pady=5)
hrs.set(0)

m = StringVar()
mins = ttk.Spinbox(
    spinboxFrame, 
    from_=0, to=60, 
    width=2, 
    textvariable=m
    )
mins.grid(column=1, row=2, pady=5)
mins.set(0)

s = StringVar()
secs = ttk.Spinbox(
    spinboxFrame, 
    from_=0, 
    to=60, 
    width=2, 
    textvariable=s
    )
secs.grid(column=2, row=2, pady=5)
secs.set(0)

StartTimeBtn = ttk.Button(
    root, 
    text="Start Countdown"
    )
StartTimeBtn.grid(column=0, row=3,padx=50)

# Label to show the countdown timer
TimeLabel = ttk.Label(
    root, 
    text="Time Left: ",
    )
TimeLabel.grid(column=0, row=1,padx=0)

root.mainloop()
