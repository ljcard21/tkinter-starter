# A starter program for Python with Tkinter


from tkinter import * # import Tkinter library
window = Tk()         # Create the application window

# Add a label with the text "Hello"
lbl = Label(window, text="Why hello there. I'm in a programming class." , font=("Arial Bold", 30))
lbl.grid(column=0, row=0)

zxc = Label(window, text="I'm 15 yrs old." , font=("Arial Bold", 38))
zxc.grid(column=1, row=1)
score = 0

def addToScore():
  message = txt.get()
  if message == "Leo":
    lbl['text'] = "go away"
  else:
    lbl['text'] = "hello"

# Add a label with the text "Hello"
lbl = Label(window, text=score, font=("Arial Bold", 50))
lbl.grid(column=0, row=0)

btn = Button(window, text="Click", command=addToScore)
btn.grid(column = 0 , row = 1)

txt = Entry(window,width=10)
txt.grid(column=1, row=0)



window.mainloop()     # Keep the window open


