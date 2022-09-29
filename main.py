# importing whole module
from tkinter import *
from tkinter.ttk import *

# importing strftime function to
# retrieve system's time
from time import strftime

# Impor json
import json

# creating tkinter window
root = Tk()
root.title('Digital Clock')


# This function is used to
# display time on the label
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)

# Open json file with color configuration
with open('configuration.json', 'r') as f:
    configuration = json.load(f)

# Default colors are purple for background
# and white for foreground
user_background = configuration['background']
user_foreground = configuration['foreground']

# Styling the label widget so that clock
# will look more attractive
lbl = Label(root, font=('courier', 35, 'bold'),
            background=user_background,
            foreground=user_foreground)

# Placing clock at the centre
# of the tkinter window
lbl.pack(anchor='center')
time()

mainloop()
