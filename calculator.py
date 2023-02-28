#............importing library........

import tkinter
from tkinter import *
from tkinter import messagebox
from math import pi, e, sin, cos, tan, log


windows=Tk()
windows.title("CALCULATOR")
windows.minsize(width=150, height=373)
windows.resizable(False,False)
l1=Label(windows, text="CALCULATOR", fg="red").pack()



#.................functioin implementation...............

expression = ""
inputText = StringVar()

def detail():
    messagebox.showinfo('user guidelines',"\n \n  AC : this button clear the all the result \n C : This button clear result one by one  \n PI : This button provide value of pi i.e. 3.141.... \n Exp : This button provide value of exponent i.e. 2.718... \n SIN,COS,TAN : These provide radian value of the given no. example: sin(45 radian) = 0.85090..... \n LOG : This provide logirithmic value of any no \n")

def connect():
    messagebox.showinfo('Contact me for any query:',"\n \n WhatsApp no : +917479996015 \n Instagram id : mr.nerds \n Email id: erajeet.kumar0000@gmail.com\n ") 

def clickButton(item):
    global expression
    inputText.set(inputText.get()+(str(item)))

def clearButton():
    global expression
    expression = ""
    inputText.set(inputText.get()[0:-1])

def clearAll():
    inputText.set("")

def sqrt(self):
    self.expression=str(eval(f"{self.expression}**0.5"))

def equalButton():
    result = ""
    try:
        result = eval(inputText.get())
        inputText.set(result)
    except:
        result = "ERROR..."
        inputText.set(result)




inputFrame = Frame(windows, width=20, height=2, bd=2, highlightbackground="black", highlightcolor="red",
                    highlightthickness=2)
inputFrame.pack(side=TOP)
inputField = Entry(inputFrame, font=('arial',22, ), textvariable=inputText, width=15,fg="black", bg="seagreen", bd=2,
                    justify=RIGHT)
inputField.grid(row=0, column=0)
inputField.pack(ipady=13)

#............calculator menubar designing..........

menubar = Menu(windows,bg="yellow",fg="black")
filemenu = Menu(menubar, tearoff=0,bg="blue",fg="white")

menubar.add_cascade(label="Edit", menu=filemenu)
#filemenu.add_command(label="Copy", command=copy)
#filemenu.add_command(label="Paste", command=paste)
#filemenu.add_separator()
filemenu.add_command(label="Exit", command=windows.quit)

contactmenu = Menu(menubar, tearoff=0,bg="blue",fg="white")
menubar.add_cascade(label="Contact", menu=contactmenu)
contactmenu.add_command(label="connect",command=connect)

helpmenu = Menu(menubar, tearoff=0,bg="blue",fg="white")
menubar.add_cascade(label="Help",menu=helpmenu)
helpmenu.add_command(label="Detail",command=detail)



###########..........calculator button creation..............##############
bALLClear=Button(windows,text="AC",bg="Aqua",fg="black", height=2 , width=8 ,bd=2,  command=lambda: clearAll())
bALLClear.place(x=0,y=100)
bclear=Button(windows,text="C",bg="Aqua",fg="black",height=2 , width=8 ,bd=2, command=lambda: clearButton())
bclear.place(x=65,y=100)
bpercent=Button(windows, text="\u221a",bg="black", fg="white",height=2,width=8,bd=2, command=lambda:clickButton(sqrt))
bpercent.place(x=130,y=100)

bdiv=Button(windows,text="/",bg="black",fg="white" ,height=2 ,width=8,bd=2, command=lambda: clickButton("/"))
bdiv.place(x=195,y=100)

bMUL=Button(windows,text="*",bg="black",fg="white" ,height=2 , width=8,bd=2, command=lambda: clickButton("*"))
bMUL.place(x=195,y=140)
b9=Button(windows,text="9",bg="black",fg="white" ,height=2 , width=8,bd=2, command=lambda: clickButton("9"))
b9.place(x=130,y=140)
b8=Button(windows,text="8",bg="black",fg="white",height=2 , width=8,bd=2, command=lambda: clickButton("8"))
b8.place(x=65,y=140)
b7=Button(windows,text="7",bg="black",fg="white",height=2 , width=8,bd=2, command=lambda: clickButton("7"))
b7.place(x=0,y=140)

bSUB=Button(windows,text="-",bg="black",fg="white",height=2 , width=8,bd=2, command=lambda: clickButton("-"))
bSUB.place(x=195,y=180)
b6=Button(windows,text="6",bg="black",fg="white",height=2 , width=8,bd=2, command=lambda: clickButton("6"))
b6.place(x=130,y=180)
b5=Button(windows,text="5",bg="black",fg="white",height=2 , width=8,bd=2, command=lambda: clickButton("5"))
b5.place(x=65,y=180)
b4=Button(windows,text="4",bg="black",fg="white",height=2 , width=8,bd=2, command=lambda: clickButton("4"))
b4.place(x=0,y=180)

bADD=Button(windows,text="+",bg="black",fg="white" ,height=2 , width=8,bd=2, command=lambda: clickButton("+"))
bADD.place(x=195,y=210)
b3=Button(windows,text="3",bg="black",fg="white",height=2 , width=8,bd=2, command=lambda: clickButton("3"))
b3.place(x=130,y=210)
b2=Button(windows,text="2",bg="black",fg="white",height=2 , width=8,bd=2, command=lambda: clickButton("2"))
b2.place(x=65,y=210)
b1=Button(windows,text="1",bg="black",fg="white" ,height=2 , width=8,bd=2, command=lambda: clickButton("1"))
b1.place(x=0,y=210)

bEqual=Button(windows,text="=",bg="orange",fg="black" ,height=2, width=8,bd=2,command=lambda: equalButton())
bEqual.place(x=195,y=250)
bDOT=Button(windows,text=".",bg="black",fg="white",height=2, width=12,bd=2, command=lambda: clickButton("."))
bDOT.place(x=100,y=250)
b0=Button(windows,text="0",bg="black",fg="white",height=2, width=14,bd=2, command=lambda: clickButton("0"))
b0.place(x=0,y=250)

bparenthesis1=Button(windows,text="(",bg="black",fg="white" ,height=2 , width=8,bd=2, command=lambda: clickButton("("))
bparenthesis1.place(x=0,y=290)
bparenthesis2=Button(windows,text=")",bg="black",fg="white",height=2 , width=8,bd=2, command=lambda: clickButton(")"))
bparenthesis2.place(x=65,y=290)
pie=3.1415
bpi=Button(windows,text="PI",bg="black",fg="white",height=2 , width=8,bd=2, command=lambda: clickButton(pie))
bpi.place(x=130,y=290)

exp= 2.7182
bexponent=Button(windows,text="Exp",bg="black",fg="white" ,height=2 , width=8,bd=2, command=lambda: clickButton(exp))
bexponent.place(x=195,y=290)

bsin=Button(windows,text="SIN",bg="black",fg="white" ,height=2 , width=8,bd=2, command=lambda: clickButton("sin"))
bsin.place(x=0,y=330)
bcos=Button(windows,text="COS",bg="black",fg="white",height=2 , width=8,bd=2, command=lambda: clickButton("cos"))
bcos.place(x=65,y=330)
btan=Button(windows,text="TAN",bg="black",fg="white",height=2 , width=8,bd=2, command=lambda: clickButton("tan"))
btan.place(x=130,y=330)
blog=Button(windows,text="LOG",bg="black",fg="white" ,height=2 , width=8,bd=2, command=lambda: clickButton("log"))
blog.place(x=195,y=330)


windows.config(bg="black", menu=menubar)
windows.mainloop()
