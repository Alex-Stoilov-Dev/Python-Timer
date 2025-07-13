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
        TimeLabel.config(text=f"Time left: {hrs}h {mins}m {secs}s")
        totalSeconds -= 1
        hrs = totalSeconds // 3600
        mins = (totalSeconds % 3600) // 60
        secs = totalSeconds % 60
        root.after(1000, countdown, hrs, mins, secs)
    else:
        TimeLabel.config(text="Time left: 0h 0m 0s")
        root.after(1000, lambda: TimeLabel.config(text="Time left: 0h 0m 0s"))
        StartTimeBtn.config(state='normal')

# Set UI title and geometry.
root = Tk()
root.title("My Timer")
root.geometry("300x300")

# Create frame to contain all spinboxes
spinboxFrame = ttk.Frame(root)
spinboxFrame.grid(column=0,row=2)

# Create frames for each combination of spinbox and letter
hoursFrame = ttk.Frame(spinboxFrame)
hoursFrame.grid(column=0,row=2)

minsFrame = ttk.Frame(spinboxFrame)
minsFrame.grid(column=1,row=2)

secsFrame = ttk.Frame(spinboxFrame)
secsFrame.grid(column=2,row=2)

# Spinboxes for hours, minutes, seconds with StringVar for binding

h = StringVar()
hrs = ttk.Spinbox(
    hoursFrame, 
    from_=0, 
    to=24, 
    width=2, 
    textvariable=h
    )
hrs.grid(column=0, row=2, pady=5)
hrs.set(0)
hoursLabel = ttk.Label(hoursFrame, text="h")
hoursLabel.grid(column=1,row=2)

m = StringVar()
mins = ttk.Spinbox(
    minsFrame, 
    from_=0, to=60, 
    width=2, 
    textvariable=m
    )
mins.grid(column=2, row=2, pady=5)
mins.set(0)
minsLabel = ttk.Label(minsFrame, text="m")
minsLabel.grid(column=3,row=2)

s = StringVar()
secs = ttk.Spinbox(
    secsFrame, 
    from_=0, 
    to=60, 
    width=2, 
    textvariable=s
    )
secs.grid(column=4, row=2, pady=5)
secs.set(0)
secsLabel = ttk.Label(secsFrame, text="s")
secsLabel.grid(column=5,row=2)

StartTimeBtn = ttk.Button(
    root, 
    text="Start Countdown",
    command=startcountdown
    )
StartTimeBtn.grid(column=0, row=3,padx=50)

# Label to show the countdown timer
TimeLabel = ttk.Label(
    spinboxFrame, 
    text="",
    justify='center'
    )
TimeLabel.grid(column=1, row=1,sticky="n")

root.mainloop()
