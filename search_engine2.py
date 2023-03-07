import tkinter as tk
from tkinter import *
import tkinter.messagebox as box
root=Tk()

root.geometry ('400x350')
root.title('Search Engine')
label=Label(root, text='Search',font=('Helvetica 17 bold'))
label.grid(column=0, row=0, sticky=tk.E, padx=5, pady=5)

root.columnconfigure (0, weight=2)
root.columnconfigure (1, weight=3)
search=Entry (root)
search.grid(column=0, row=1, sticky=tk.E, padx=5, pady=5)
def solve():
    file=open('words.txt','r')
    word=search.get()
    reference=file.readlines()
    file.close()
    length=len(word);s=set()
    sets=set(word)
    for ele in word:
        for item in reference:
            if sets.issubset(item):
                s.add(item)

    msg=Text(root, height=10, width=18, font = ( "Helvetica 9"))
    msg.grid(column=0,row=3, sticky=tk.E )
    for x in s:
        msg.insert(END, x)
def key_press(e):
    command=solve()
def key_release (e):
    command=solve()
root.bind('<KeyPress>',key_press)
root.bind('<KeyRelease>',key_release)
but=Button(root,text='search',command=solve)
but.grid(column=1,row=1,sticky=tk.W,padx=5,pady=5)

help=Label(root, text='Add Words', font=('Courier 8 bold'))
help.grid(column=0, row=7, sticky=tk.W, padx=50,pady=5)
def yes():
    add=Entry(root)
    add.grid(column=0, row=8, sticky=tk.E, padx=5, pady=5)

    def adds():
        file=open('words.txt','a')
        file.write(add.get()+'\n')
        file.close()
    button=Button(root,text="Add",command=adds)
    button.grid(column=0,row=8,sticky=tk.E,padx=5,pady=5)

def no():
    Lab=Label(root, text='Thanks', font=('courier 12 bold'))
    Lab.grid(column=0, row=8, sticky=tk.E, padx=5, pady=5)

yesbut=Button(root, text='Yes', command=yes)
yesbut.grid(column=0, row=7, sticky=tk.E, padx=5, pady=5)
nobut=Button(root, text=' No ', command=no)
nobut.grid(column=1, row=7, sticky=tk.W,padx=5, pady=5)

root.mainloop()


