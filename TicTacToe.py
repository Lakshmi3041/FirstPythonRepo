import tkinter
win = tkinter.Tk()

def check_progress():
	if B1.cget('bg')==B2.cget('bg')==B3.cget('bg') == 'red' or B1.cget('bg')==B2.cget('bg')==B3.cget('bg') == 'green' \
	or B1.cget('bg')==B5.cget('bg')==B9.cget('bg') == 'red' or B1.cget('bg')==B5.cget('bg')==B9.cget('bg') == 'green' \
	or B1.cget('bg')==B4.cget('bg')==B7.cget('bg') == 'red' or B1.cget('bg')==B4.cget('bg')==B7.cget('bg') == 'green' \
	or B3.cget('bg')==B5.cget('bg')==B7.cget('bg') == 'red'	or B3.cget('bg')==B5.cget('bg')==B7.cget('bg') == 'green' \
	or B4.cget('bg')==B5.cget('bg')==B6.cget('bg') == 'red'	or B4.cget('bg')==B5.cget('bg')==B6.cget('bg') == 'green' \
	or B7.cget('bg')==B8.cget('bg')==B9.cget('bg') == 'red'	or B7.cget('bg')==B8.cget('bg')==B9.cget('bg') == 'green' \
	or B2.cget('bg')==B5.cget('bg')==B8.cget('bg') == 'red'	or B2.cget('bg')==B5.cget('bg')==B8.cget('bg') == 'green' \
	or B3.cget('bg')==B6.cget('bg')==B9.cget('bg') == 'red'	or B3.cget('bg')==B6.cget('bg')==B9.cget('bg') == 'green' :
		print('game over')
i=0

def change_colour1():
	global i
	i=i+1
	if i==1 or i==3 or i==5 or i==7 or i==9:
		B1['bg'] ='red'
	else:
		B1['bg']= 'green'
	check_progress()
def change_colour2():
	global i
	i=i+1
	if i==1 or i==3 or i==5 or i==7 or i==9:
		B2['bg'] ='red'
	else:
		B2['bg']= 'green'
	check_progress()
def change_colour3():
	global i
	i=i+1
	if i==1 or i==3 or i==5 or i==7 or i==9:
		B3['bg'] ='red'
	else:
		B3['bg']= 'green'
	check_progress()
def change_colour4():
	global i
	i=i+1
	if i==1 or i==3 or i==5 or i==7 or i==9:
		B4['bg'] ='red'
	else:
		B4['bg']= 'green'
	check_progress()
def change_colour5():
	global i
	i=i+1
	if i==1 or i==3 or i==5 or i==7 or i==9:
		B5['bg'] ='red'
	else:
		B5['bg']= 'green'
	check_progress()
def change_colour6():
	global i
	i=i+1
	if i==1 or i==3 or i==5 or i==7 or i==9:
		B6['bg'] ='red'
	else:
		B6['bg']= 'green'
	check_progress()
def change_colour7():
	global i
	i=i+1
	if i==1 or i==3 or i==5 or i==7 or i==9:
		B7['bg'] ='red'
	else:
		B7['bg']= 'green'
	check_progress()
def change_colour8():
	global i
	i=i+1
	if i==1 or i==3 or i==5 or i==7 or i==9:
		B8['bg'] ='red'
	else:
		B8['bg']= 'green'
	check_progress()
def change_colour9():
	global i
	i=i+1
	if i==1 or i==3 or i==5 or i==7 or i==9:
		B9['bg'] ='red'
	else:
		B9['bg']= 'green'
	check_progress()
B1 = tkinter.Button(win,text='			', command = change_colour1)
B1.grid(row=0, column=0)			
B2 = tkinter.Button(win,text='			', command = change_colour2)
B2.grid(row=0, column=1)			
B3 = tkinter.Button(win,text='			', command = change_colour3)
B3.grid(row=0, column=2)			
B4 = tkinter.Button(win,text='			', command = change_colour4)
B4.grid(row=1, column=0)			
B5 = tkinter.Button(win,text='			', command = change_colour5)
B5.grid(row=1, column=1)			
B6 = tkinter.Button(win,text='			', command = change_colour6)
B6.grid(row=1, column=2)			
B7 = tkinter.Button(win,text='			', command = change_colour7)
B7.grid(row=2, column=0)			
B8 = tkinter.Button(win,text='			', command = change_colour8)
B8.grid(row=2, column=1)			
B9 = tkinter.Button(win,text='			', command = change_colour9)
B9.grid(row=2, column=2)


win.mainloop(  )