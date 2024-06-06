import tkinter as tk
import Logic as log
from pynput.keyboard import Key, Listener


def keyInput(key):
    if key.char=="\r":
        MainDisplay.config(text=str(log.Calculate(var, oper))), var.clear(), oper.clear(), var.append(
            MainDisplay.cget("text"))
    elif key.char=="\x1b":
        MainDisplay.config(text=""), var.clear(), oper.clear()
    elif(key.char!=""):
        Input(key.char)
        print(oper)
        print(var)


def DecimalPlaces(a):
    b=0
    while (a/(pow(10,(b-1))))>1:
        b+=1
    return b-1

def Input(a):
    if str(a).isdigit():
        if len(var)>len(oper):
            var[len(var)-1]=var[len(var)-1]*10+a
        else:
            var.append(a)
    else:
        oper.append(a)
    Display(a)

def Display(a):
    temp=MainDisplay.cget("text")
    MainDisplay.config(text=temp+""+str(a))

var = [ ]
oper = [ ]
b=0

#region UI
root = tk.Tk()
root.title("4Tea - Python Calculator 2024")
root.configure(background="grey")
root.minsize(400, 600)  # width, height
root.maxsize(400, 600)
root.geometry("300x300+50+50")  # width x height + x + y

CopyrightText = tk.Label(root, text="4TeaSoftware 2024\nAll rights reserved")
CopyrightText.place(x=150,y=550)

MainDisplay = tk.Label(root, text="")
MainDisplay.place(x=75,y=75, height=50, width=250)
root.state("zoomed")
#endregion

#region Buttons
for i in range(3):
    for j in range(3):
        Btn=tk.Button(root, text =1+i+j*3, command=lambda a=1+i+3*j: Input(a), height=2, width=4)
        Btn.place(x=100+75*i,y=200+75*j)

Btn=tk.Button(root, text ="0", command=lambda a=0: Input(a), height=2, width=4)
Btn.place(x=175,y=425)

Btn=tk.Button(root, text ="+", command=lambda a="+": Input(a), height=2, width=4)
Btn.place(x=325,y=200)

Btn=tk.Button(root, text ="-", command=lambda a="-": Input(a), height=2, width=4)
Btn.place(x=325,y=275)

Btn=tk.Button(root, text ="*", command=lambda a="*": Input(a), height=2, width=4)
Btn.place(x=325,y=350)

Btn=tk.Button(root, text ="/", command=lambda a="/": Input(a), height=2, width=4)
Btn.place(x=325,y=425)

Btn=tk.Button(root, text ="=", command=lambda: [MainDisplay.config(text=str(log.Calculate(var, oper))), var.clear(), oper.clear(), var.append(MainDisplay.cget("text"))], height=2, width=4)
Btn.place(x=325,y=500)

Btn=tk.Button(root, text ="clear", command=lambda: [MainDisplay.config(text=""), var.clear(), oper.clear()], height=2, width=4)
Btn.place(x=75,y=500)
#endregion

root.bind('<Key>', keyInput)
root.mainloop()

