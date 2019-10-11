import Tkinter as tk
import time2
import show
import time
import ddemail
from datetime import datetime 
show.sp()
root=tk.Tk()
a=[]
time1=[]
root.title("TO-DO")
root.geometry("600x100")
s1=tk.StringVar()
s2=tk.StringVar()
t1=tk.StringVar()
t2=tk.StringVar()
tk.Label(root,text="OFFICE_WORK").grid(row=0)
tk.Entry(root,width=30,textvariable=s1).grid(row=0,column=1)
tk.Label(root,text="   START_TIME").grid(row=0,column=2)
tk.Entry(root,width=10,textvariable=t1).grid(row=0,column=3)
def ss():
	if len(s1.get())!=0:
		a.append(s1.get())
		time1.append(t1.get())
	if len(s2.get())!=0:
		a.append(s2.get())
		time1.append(t2.get())
	s2.set("")
	s1.set("")
	t1.set("")
	t2.set("")
tk.Label(root,text="OFFICE_WORK").grid(row=1)
tk.Entry(root,width=30,textvariable=s2).grid(row=1,column=1)
tk.Label(root,text="  START_TIME").grid(row=1,column=2)
tk.Entry(root,width=10,textvariable=t2).grid(row=1,column=3)
tk.Button(root, text="NEXT_TASKS", command=ss,width=25).grid(row=2,column=0)
def printf():
	if len(s1.get())!=0:
		a.append(s1.get())
		time1.append(t1.get())
	if len(s2.get())!=0:
		a.append(s2.get())
		time1.append(t2.get())
	#tkMessageBox.showinfo( "message","List saved.")
	root.destroy()
	
tk.Button(root, text="FINISH", fg ="red", command=printf , width=25).grid(row=2,column=3)
root.mainloop()
sec_time=[]
def dif_time(time1):
	diff_time=[]
	time1.sort()
	temp=str(datetime.now().time())
	diff_time.append(temp[:len(temp)-7])
	diff_time+=time1
	time1=diff_time
	diff_time=[]	
	fmt='%H:%M:%S'
	for i in range(len(time1)-1):
		s1=str(time1[i])
		s2=str(time1[i+1])
		tdelta=datetime.strptime(s2,fmt)-datetime.strptime(s1,fmt)
		diff_time.append(str(tdelta))
	for i in range(len(diff_time)):
		sec=time2.time12(diff_time[i])
		sec_time.append(int(sec))	
dif_time(time1)
_email=""
def take_email():
		reet = tk.Tk()
		reet.title("DAD's E-MAIL")
		tk.Label(reet, text="EMAIL ADDRESS").grid(row=0)
		nm=tk.StringVar()
		tk.Entry(reet,textvariable=nm,width=40).grid(row=0,column=1)
		def s_s():
			_email=str(nm.get())
			reet.destroy()
		tk.Button(reet, text='Ok', command=s_s).grid(row=1,column=2)
		reet.mainloop( )
take_email()
def sleep():
	for i in range(len(sec_time)):
		temp=sec_time[i]
		print "WAITING FOR THE UPCOMING EVENT..."
		time.sleep(temp)
		rt = tk.Tk()
		rt.title("REMINDER")
		tk.Label(rt, text="RICHIE YOU HAVE TO Do "+str(a[i])).grid(row=0,column=2)
		def sss():
   			rt.destroy()
			ddemail.em(str(_email),str(a[i]))
		tk.Button(rt, text='Ok', command=sss).grid(row=1,column=2)
		rt.mainloop( )
sleep()
