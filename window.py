import tkinter

def main():
	a = tkinter.Tk()
	a.title('Window')
	a.geometry('500x500')
	b = tkinter.Label(text='label one',fg='red',bg='yellow').place(x=100,y=100)
	#place moves the lable around the x and y axis in the window.
	c = tkinter.Label(text='second lable testing',fg='blue',bg='green')
	c.pack() #where the label appears in the windows
	#fg = frontground #bg = background
	#d = tkinter.Label(text='3rd label',fg='yellow',bg='blue')
	#d.grid(rows=1,column=1)
	#Grid allows label to be placed defined by row and colums.
	#Note: cannot use grid with pack.
	a=tkinter.mainloop()

main()