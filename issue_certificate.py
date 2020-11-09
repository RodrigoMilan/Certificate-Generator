import tkinter as tk
from functools import partial
from tkinter import filedialog
import certificator

def run():
	try:
		certificator.main(username.get(), password.get(), excelFile, certificate)
		certificateEntry.delete(0,tk.END)
		excelEntry.delete(0,tk.END)
		usernameEntry.delete(0,tk.END)
		passwordEntry.delete(0,tk.END)

		nw = tk.Tk()
		nw.title('DONE')
		nw.geometry("100x50")
		message = tk.Label(nw, text="It's done").pack()
		button = tk.Button(nw, text='OK', command=nw.destroy).pack()
		nw.mainloop()
	except:
		nw = tk.Tk()
		nw.title('ERROR')
		nw.geometry("400x100")
		message = tk.Label(nw, text='An error has occurred, please try again').pack(pady=20)
		button = tk.Button(nw, text='OK', command=nw.destroy).pack(pady=8)

def excelButton():	
	global excelFile
	excelFile = filedialog.askopenfilename()
	excelEntry.delete(1, tk.END)
	excelEntry.insert(0, excelFile)

def certificateFile():
	global certificate
	certificate = filedialog.askopenfilename()
	certificateEntry.delete(1, tk.END)
	certificateEntry.insert(0, certificate)

window = tk.Tk()
window.title('Certicator')

top_frame = tk.Frame(window)
middle_frame = tk.Frame(window)
bottom_frame = tk.Frame(window)
line1 = tk.Frame(window, height=1, width=400, bg="grey80", relief="groove")
line2 = tk.Frame(window, height=1, width=400, bg="grey80", relief="groove")

usernameLabel = tk.Label(top_frame, text='Insert your Email:')
username = tk.StringVar()
usernameEntry = tk.Entry(top_frame, textvariable=username, width=40)

passwordLabel = tk.Label(top_frame, text="Insert your Password:")
password = tk.StringVar()
passwordEntry = tk.Entry(top_frame, textvariable=password, show='*')

excelLabel = tk.Label(middle_frame, text='Excel file:')
excelPath = tk.StringVar()
excelEntry = tk.Entry(middle_frame, textvariable=excelPath, width=40, text="" )
button1 = tk.Button(middle_frame, text='Browse', command=lambda: excelButton())

certificateLabel = tk.Label(middle_frame, text='Certificate Layout:')
certificate = tk.StringVar()
certificateEntry = tk.Entry(middle_frame, textvariable=certificate, width=40, text="")
button2 = tk.Button(middle_frame, text='Browse', command=lambda: certificateFile())

runButton = tk.Button(bottom_frame, text='run', command=lambda: run())

top_frame.pack(side=tk.TOP)
line1.pack(pady=10)
middle_frame.pack(side=tk.TOP)
line2.pack(pady=10)
bottom_frame.pack(side=tk.BOTTOM)

usernameLabel.pack(pady=5)
usernameEntry.pack(pady=5, fill=tk.X)

passwordLabel.pack(pady=5)
passwordEntry.pack(pady=5, fill=tk.X)

excelLabel.pack(pady=5)
excelEntry.pack(pady=5)
button1.pack(pady=5)

certificateLabel.pack(pady=5)
certificateEntry.pack(pady=5)
button2.pack(pady=5)

runButton.pack(pady=10, fill=tk.X)
window.mainloop()
