#!/usr/bin/env python
# encoding: utf-8

import tkinter as tk
from functools import partial
from tkinter import filedialog
import certificator


def run():
	try:
		teste.main(username.get(), password.get(), excelFile, certificate)
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


def checkbox_func(box, value):
	if value.get() == 1:
		box.config(state='normal')
		box.config(bg='white')
	box.delete("1.0",tk.END)
	if value.get() == 0:
		box.config(state='disable')
		box.config(bg='#a6a6a6')

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

def moreOptions():
	global messageValue

	optionsScreen = tk.Tk()
	optionsScreen.geometry("500x500")
	optionsScreen.title('Advanced options')

	optionsScreen.tk.call('encoding', 'system', 'utf-8')
	

	topFrame = tk.Frame(optionsScreen)
	bottomFrame = tk.Frame(optionsScreen)
	lineOption = tk.Frame(optionsScreen, height=1, width=600, bg="grey80", relief="groove")

	messageValue = tk.IntVar(topFrame)
	messageCheckbox = tk.Checkbutton(topFrame, text='Message', variable=messageValue, command=lambda: checkbox_func(messageText,messageValue))
	messageText = tk.Text(topFrame, state="disable", bg="#a6a6a6", height=10, width=50)

	subjectValue = tk.IntVar(bottomFrame)
	subjectCheckbox = tk.Checkbutton(bottomFrame, text='Subject', variable=subjectValue, command=lambda: checkbox_func(subjectText,subjectValue))
	subjectText = tk.Text(bottomFrame, state="disable", bg="#a6a6a6", height=2, width=50)

	topFrame.pack(side=tk.TOP)
	lineOption.pack(pady=15)
	bottomFrame.pack(side=tk.TOP)

	messageCheckbox.pack()
	messageText.pack()

	subjectCheckbox.pack()
	subjectText.pack()

	optionsScreen.mainloop()


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

runButton = tk.Button(bottom_frame, text='run', width=5, command=lambda: run())
optionsButton = tk.Button(bottom_frame, text='options', width=5, command=lambda: moreOptions())


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

runButton.pack(pady=10, padx=2, fill=tk.X, side=tk.LEFT)
optionsButton.pack(pady=10, fill=tk.X, side=tk.RIGHT)
window.mainloop()