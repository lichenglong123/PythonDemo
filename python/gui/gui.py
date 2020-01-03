from tkinter import *
from  tkinter import scrolledtext

def load():
    with open(fileName.get()) as  file:
        contents.delete('1.0',END)
        contents.insert(INSERT,file.read())
def save():
    with open(fileName.get(),'w') as file:
        file.write(contents.get('1.0',END))

top=Tk()
top.title('editor')
contents=scrolledtext.ScrolledText()
contents.pack(side=BOTTOM,expand=True,fill=BOTH)
fileName=Entry()
fileName.pack(side=LEFT,expand=True,fill=X)
# Button(text='open',command=load).pack(side=RIGHT)
# Button(text='save',command=save).pack(side=RIGHT)
top.mainloop()




