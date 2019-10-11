import Tkinter as tk
def sp():
	moot = tk.Tk()
	moot.title("HElP DesK")
	tk.Label(moot, text="WELCOME RICHIE SIR!\n I will help you to manage your daily tasks... \n wish you a good day \n\n\n ").pack()
	def ss():
	   moot.destroy()
	but=tk.Button(moot, text='Ok', command=ss)
	but.pack()
	moot.mainloop( )

	root1 = tk.Tk()
	root1.title("HElP DesK")
	tk.Label(root1, text="\n Now enter TASK and it's respective TIME(hh:mm:ss) for the reminder! \n\n click next to add more tasks").pack()
	#Label(master, text="Last Name").grid(row=1)

	#e1 = Entry(master)
	#e2 = Entry(master)

	#e1.grid(row=0, column=1)
	#e2.grid(row=1, column=1)
	def ss():
	   root1.destroy()
	but=tk.Button(root1, text='Ok', command=ss)
	but.pack()
	root1.mainloop( )
