import tkinter
import os

app = tkinter.Tk()

def getInfo():
	info = text.get()
	os.system("python tesseract.py -i " + info)

text = tkinter.Entry(app)
btn = tkinter.Button(app, text = "ok", command = getInfo)

text.grid(row = 1, column = 1)
btn.grid(row = 2, column = 1)
app.mainloop()
