#importing every methods from the tkinter module

from tkinter import *  

#creating master

s=Tk()

#declaring variable

var1=IntVar() 

def option1():

#this function will display the option 1

      L1.config(text="you selected option 1")

def option2():

#this function will display the option 2

      L1.config(text="you selected option 2")

def option3():

#this function will display the option 3

      L1.config(text="you selected option 3")

#creating radio buttons

r1=Radiobutton(s,text="option1",variable=var1,command=option1,value=1)
r2=Radiobutton(s,text="option2",variable=var1,command=option2,value=2)
r3=Radiobutton(s,text="option3",variable=var1,command=option3,value=3)

#placing the radiobuttons

r1.grid(row=0,column=0) 
r2.grid(row=1,column=0)
r3.grid(row=2,column=0)
#creating label

L1=Label(s)
L1.grid(row=3,column=0)
if var1==1:
      print("option is 1")
