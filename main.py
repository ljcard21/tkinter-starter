# A starter program for Python with Tkinter


from tkinter import * # import Tkinter library
window = Tk()         # Create the application window

# Add a label with the text "Hello"
lbl = Label(window, text="Why hello there. I'm in a programming class." , font=("Arial Bold", 30))
lbl.grid(column=0, row=0)

zxc = Label(window, text="I'm 15 yrs old." , font=("Arial Bold", 38))
zxc.grid(column=1, row=1)



window.mainloop()     # Keep the window open
