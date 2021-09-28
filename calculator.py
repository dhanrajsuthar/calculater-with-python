# calculater-with-python
I have doveloped a calculator software program with python tkinter library.
from tkinter import*
import tkinter.messagebox as tmsg

def btnclick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator = ""
    text_Input.set("")

def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""

def aboutme():
    a = tmsg.showinfo("about me","HELLO MR/MRS......    I AM DHANRAJ SUTHAR I HOPE THAT THIS CALCULATOR WILL BE HELPFULL FOR YOU IN COUNTING , thanks for open DHANRAJ'S CALCULATOR")
def Help():
    b= tmsg.showinfo("help" ,"FIRST CLICK A NUMBER THEN SELECT + or - or * or / . AFTER THIS CHOOSE YOUR SECOND NUMBER THEN CLICK ON EQUIL'=' YOU WILL GET YOUR REJULT ")

def Rate():
    c = tmsg.askquestion("Rate", "was this calculater helpfull for you? ")

    print("thanks for rate",user)
    

user=input("what is your name?")
print("hello",user)

cal = Tk()
cal.title("DHANRAJ'S CALCULATOR")
operator=""
text_Input = StringVar()



txtDisplay = Entry(cal, text="",font=('cambria',20,'bold'), textvariable = text_Input, bd = 30,
                   insertwidth = 3, bg = "cyan", justify = 'right').grid(columnspan=4)
label=Label(cal, text="hello").grid(row=0,column=0)
label=Label(cal, text=user,bg='cyan',fg="yellow",font=('algerian',20,'bold')).grid(row=0,column=1)

button7 = Button(cal, padx=16,pady=16, bd=8, fg="orange", bg = "blue", font=('cambria',20,'bold'), text="7",
                 command = lambda:btnclick(7))
button7.grid(row=1,column=0)

button8 = Button(cal, padx=16,pady=16, bd=8, fg="orange", bg = "purple", font=('cambria',20,'bold'), text="8",
                 command = lambda:btnclick(8))
button8.grid(row=1,column=1)

button9 = Button(cal, padx=16,pady=16, bd=8, fg="orange",bg = "grey", font=('cambria',20,'bold'), text="9",
                 command = lambda:btnclick(9))
button9.grid(row=1,column=2)

buttonAdd = Button(cal, padx=16,pady=16, bd=8, fg="orange", font=('cambria',20,'bold'), text="+",
                 command = lambda:btnclick("+"))
buttonAdd.grid(row=1,column=3)

#######################################################################################################################################

button6 = Button(cal, padx=16,pady=16, bd=8, fg="white", bg = "green", font=('cambria',20,'bold'), text="6",
                 command = lambda:btnclick(6))
button6.grid(row=2,column=0)

button5 = Button(cal, padx=16,pady=16, bd=8, fg="white",bg = "green", font=('cambria',20,'bold'), text="5",
                 command = lambda:btnclick(5))
button5.grid(row=2,column=1)

button4 = Button(cal, padx=16,pady=16, bd=8, fg="white",bg = "green", font=('cambria',20,'bold'), text="4",
                 command = lambda:btnclick(4))
button4.grid(row=2,column=2)

buttonSub = Button(cal, padx=16,pady=16, bd=8, fg="white",bg = "green", font=('cambria',20,'bold'), text="-",
                 command = lambda:btnclick("-"))
buttonSub.grid(row=2,column=3)

#########################################################################################################################

button3 = Button(cal, padx=16,pady=16, bd=8, fg="green", font=('cambria',20,'bold'), text="3",
                 command = lambda:btnclick(3))
button3.grid(row=3,column=0)

button2 = Button(cal, padx=16,pady=16, bd=8, fg="green",bg = "grey", font=('cambria',20,'bold'), text="2",
                 command = lambda:btnclick(2))
button2.grid(row=3,column=1)

button1 = Button(cal, padx=16,pady=16, bd=8, fg="green",bg = "purple", font=('cambria',20,'bold'), text="1",
                 command = lambda:btnclick(1))
button1.grid(row=3,column=2)

buttonMulti = Button(cal, padx=16,pady=16, bd=8, fg="green", bg = "blue", font=('cambria',20,'bold'), text="X",
                 command = lambda:btnclick("*"))
buttonMulti.grid(row=3,column=3)

######################################################################################################################################

button0 = Button(cal, padx=16,pady=16, bd=8, fg="blue", bg = "black", font=('cambria',20,'bold'), text="0",
                 command = lambda:btnclick(0))
button0.grid(row=4,column=0)

buttonEqu = Button(cal, padx=16,pady=16, bd=8, fg="blue",bg = "black", font=('cambria',20,'bold'), text="=",
                 command = lambda:btnEquals())
buttonEqu.grid(row=4,column=1)

buttonClr = Button(cal, padx=16,pady=16, bd=8, fg="blue",bg = "black", font=('cambria',20,'bold'), text="C",
                 command = lambda:btnClear())
buttonClr.grid(row=4,column=2)

buttonDiv = Button(cal, padx=16,pady=16, bd=8, fg="blue",bg = "black", font=('cambria',20,'bold'), text="/",
                 command = lambda:btnclick("/"))
buttonDiv.grid(row=4,column=3)

mymenu = Menu(cal)
mymenu.add_command(label="about me",command=aboutme)
mymenu.add_command(label="help",command=Help)
mymenu.add_command(label="Rate",command=Rate)
mymenu.add_command(label="Hello")
mymenu.add_command(label=user)
cal.config(menu=mymenu,)






cal.mainloop()
