from tkinter import *
from tkinter import ttk
from os import listdir
from PIL import Image,ImageTk
import random




rootdir="/images/"
import random,os
which=random.choice(os.listdir(rootdir))
print(which)
rootdir+=which
csvname=f'captions/{which}.txt'

import sys
from antarctic_captions.antartic import caption_image
print('done')

dones=[]
try:
    csv=open(csvname,'r')
    

    for i in csv:
        dones.append(i.split('\t')[0])
except:
    pass

csv=open(csvname,'a')
yets=set(listdir(rootdir)).difference(dones)


class Window(Frame):

    def __init__(self,master=False):
        Frame.__init__(self,master)
        self.pack()

        self.master=master

    def create_widgets(self):
        #Canvas
        self.canvas1 = Canvas(self)
        self.canvas1.configure(width=960, height=720,bg='white')
        self.canvas1.grid(column=0, row=0)
        self.canvas1.grid(padx=20)
        self.load()

    def suggest(self):
        self.suggestion=caption_image(f'{rootdir}/{self.dir}')
        suggestion_text.set(self.suggestion)

    def load(self):
        while True:
            try:
                self.dir=random.choice(list(yets))
                image=Image.open(f'{rootdir}/{self.dir}').resize((960,720))
                break
            except:
                if not yets:
                    return
        #if image.size[0]>
        #image.show()
        self.image=ImageTk.PhotoImage(image)
        
        self.canvas1.create_image(960,720, image=self.image,anchor=SE)
        button_text.set(f"{len(yets)} left, {len(dones)} done")

        self.suggest()
        

    def next(self,a=''):
        print(self.dir,name.get())
        if name.get():
            csv.write(f'{self.dir}\t"{name.get()}"\n')
            csv.flush()
            yets.remove(self.dir)
            dones.append(self.dir)
            name.set("")
        
        self.load()

    def pick_suggestion(self,a=''):
        print(self.dir,self.suggestion)
        csv.write(f'{self.dir}\t"{self.suggestion}"\n')
        csv.flush()
        yets.remove(self.dir)
        dones.append(self.dir)
        name.set("")
        
        self.load()

        

        

root=Tk()

name = StringVar()
button_text=StringVar()
suggestion_text=StringVar()

app=Window(root)
app.create_widgets()


nameEntered = ttk.Entry(app, width = 70, textvariable = name)
nameEntered.grid(column = 0, row = 1)

#File open and Load Image
button_open = ttk.Button(app,textvariable=button_text,width=25)
button_open.grid(column=0, row=2)
button_open.configure(command=app.next)

#suggest caption
button_suggest = ttk.Button(app,textvariable=suggestion_text,width=100)
button_suggest.grid(column=0, row=3)
button_suggest.configure(command=app.pick_suggestion)

#retry caption
button_suggest = ttk.Button(app,text="retry",width=10)
button_suggest.grid(column=0, row=4)
button_suggest.configure(command=app.suggest)



#app.minsize(600,400)
app.mainloop()
